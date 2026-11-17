
from pathlib import Path
from pypdf import PdfReader
from docx import Document


DOCS_DIR = Path(__file__).resolve().parents[2] / "docs"


def load_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def load_docx(file_path):
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def load_documents():
    documents = []

    for file_path in DOCS_DIR.iterdir():

        if file_path.suffix.lower() == ".pdf":
            content = load_pdf(file_path)

        elif file_path.suffix.lower() == ".docx":
            content = load_docx(file_path)

        else:
            continue

        documents.append({
            "filename": file_path.name,
            "content": content
        })
    
    
    return documents


