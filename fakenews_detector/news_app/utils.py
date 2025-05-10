import joblib
from PyPDF2 import PdfReader  # Changed import to PdfReader

def detect_fake_news(news_vector, model):
    news_dense = news_vector.toarray()  # Convert to dense array
    prediction = model.predict(news_dense)
    return prediction[0]

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)  # Changed PdfFileReader to PdfReader
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def vectorize_text(text, vectorizer):
    return vectorizer.transform([text])
