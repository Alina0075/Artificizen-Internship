import fitz

def extract_pdf(file_path:str):
    doc=fitz.open(file_path)
    text=""
    for page in doc:
        text+=page.get_text()
    doc.close()
    return [text]