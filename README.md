# Chat with PDF: A Streamlit Application

This is a Streamlit application that allows users to upload a PDF file and query it for answers using OpenAI's GPT-3.5 Turbo model and LangChain. The code extracts text from the PDF, splits it into chunks, creates embeddings, and performs similarity search to answer questions.

## Requirement tools

- Python 3.7+
- [Streamlit](https://www.streamlit.io/)
- [PyPDF2](https://pypdf2.readthedocs.io/)
- [LangChain](https://python.langchain.com/)
- [OpenAi Api](https://platform.openai.com/docs/api-reference)

Make sure to install these libraries before running the code.

## Usage

1. Install the required libraries.
2. Run the application using Streamlit.

```bash
streamlit run chat_with_pdf.py
```

3. Open the application in your web browser.

4. In the sidebar, select the model to use (e.g., 'gpt-3.5-turbo') and specify the number of summary prompts to consider (K).

5. Enter your OpenAI API key in the provided input box. Note that the API key is not stored.

6. Upload a PDF file using the file upload widget.

7. The PDF text will be extracted and split into chunks for processing.

8. Enter a question related to the PDF in the text input field labeled "Ask a question about your PDF."

9. If you enter a question and have uploaded a PDF, the application will first answer the question using the PDF. Then, it will continue with a chatbot interaction using the GPT-3.5 Turbo model. The PDF-based QA response will be displayed in the application.

## Important Notes

- Make sure you have a valid OpenAI API key.
- The code uses OpenAI's GPT-3.5 Turbo model, but you can choose other models as well.
- This application combines PDF-based question-answering and chatbot interactions in a single interface.
- The OpenAI API key is not stored, and no user data is saved or used for any purpose beyond the application's runtime.

Enjoy using this application to chat with your PDF files and explore the capabilities of GPT-3.5 Turbo and LangChain!
