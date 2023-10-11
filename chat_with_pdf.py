# Import necessary libraries
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.llms import OpenAI


# Set up sidebar with various options
with st.sidebar.expander("🛠️ ", expanded=False):
    MODEL = st.selectbox(label='Model', options=['gpt-3.5-turbo','text-davinci-003','text-davinci-002','code-davinci-002'])
    K = st.number_input(' (#)Summary of prompts to consider',min_value=3,max_value=1000)

# Set up the Streamlit app layout
st.title("🤖 Chat with Your PDF🧠")
st.subheader(" Powered by 🦜 LangChain + OpenAI + Streamlit")

# Ask the user to enter their OpenAI API key
API_O = st.sidebar.text_input("API-KEY", type="password")

# Session state storage would be ideal
if API_O:
    # Create an OpenAI instance
    llm = OpenAI(temperature=0,
                openai_api_key=API_O, 
                model_name=MODEL, 
                verbose=False) 

else:
    st.sidebar.warning('API key required to try this app.The API key is not stored in any form.')
    # st.stop()

st.sidebar.markdown(
    """
    <style>
    .st-eb button {
        background-color: #FF5722;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# PDF File Upload and Embedding
pdf = st.file_uploader("Upload your PDF", type="pdf")
pdf_text = ""
chain = None  # Initialize the chain instance

if pdf is not None:
    pdf_reader = PdfReader(pdf)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    # Split the PDF text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    pdf_chunks = text_splitter.split_text(pdf_text)

    # Create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=API_O)
    knowledge_base = FAISS.from_texts(pdf_chunks, embeddings)
    # Ask the user to enter a question about the PDF
    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:
        # Perform similarity search to get relevant document chunks
        docs = knowledge_base.similarity_search(user_question)
# Generate the output using the ConversationChain object and the user input, and add the input/output to the session
if docs is not None and user_question:
    # Incorporate PDF-based QA with chatbot interaction using the same `llm.chain` instance
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)  # Print OpenAI callback
    st.write(response)  # Display PDF-based QA response
        