from pypdf import PdfReader

def read_txt(file_path:str)->str:
    with open(file_path,'r',encoding='utf-8') as file:
        return file.read()
    
def read_pdf(file_path:str)->str:
    reader=PdfReader(file_path)
    text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text+"\n"
    return text

def extract_text(file_path:str)->str:
    if file_path.endswith('.txt'):
        return read_txt(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    else:
        raise ValueError("Unsupported file type. Only .txt and .pdf files are supported.")