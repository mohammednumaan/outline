from pypdf import PdfReader
import os

# currently, i only support pdf files
# but in the future, i should support more file types such as EPUB.
def read_pdf_file(file_path: str):

    reader = PdfReader(file_path)
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text()

    return full_text


def read_document(file_path: str):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == ".pdf":
        return read_pdf_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


