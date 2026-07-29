import easyocr

def extract_image(file_path):
    reader = easyocr.Reader(["en"])

    results = reader.readtext(file_path)

    text = "\n".join([item[1] for item in results])

    return [text]