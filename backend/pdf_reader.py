import pdfplumber
from io import BytesIO
def get_text_from_pdf(pdf_data):
    my_text = ""
    pdf_file = pdfplumber.open(BytesIO(pdf_data))
    for one_page in pdf_file.pages:
        words_on_page = one_page.extract_text()
        if words_on_page:
            my_text = my_text + words_on_page + "\n"
    pdf_file.close()
    return my_text