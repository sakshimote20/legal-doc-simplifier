# 
import pdfplumber
import docx
from PIL import Image
import pytesseract

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

def split_into_clauses(text):
    # Split clauses using newline or semicolon.
    # You can improve this logic later.
    clauses = [cl.strip() for cl in text.split("\n") if len(cl.strip()) > 20]
    return clauses

def get_full_text(file):
    try:
        if file.name.endswith(".pdf"):
            return extract_text_from_pdf(file)
        elif file.name.endswith(".docx"):
            return extract_text_from_docx(file)
        elif file.name.endswith((".jpg", ".jpeg", ".png")):
            return extract_text_from_image(file)
        else:
            return ""
    except Exception as e:
        print("Error reading file:", e)
        return None

def extract_text_from_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text.strip()
