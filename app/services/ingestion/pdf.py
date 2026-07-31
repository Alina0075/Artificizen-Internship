import fitz


def extract_pdf(file_path: str):
    doc = fitz.open(file_path)
    pages = []

    for page_number, page in enumerate(doc, start=1):

        text = page.get_text("text").strip()

        if text:
            pages.append(
                f"Page {page_number}:\n{text}"
            )

    doc.close()

    return pages