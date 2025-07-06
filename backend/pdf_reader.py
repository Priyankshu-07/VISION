import pdfplumber
from io import BytesIO

def get_text_from_pdf(pdf_data: bytes) -> str:
    all_text = ""
    with pdfplumber.open(BytesIO(pdf_data)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"
    return all_text.strip()
