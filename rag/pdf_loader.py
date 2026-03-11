import fitz

async def load_pdf(file):
    pdf_bytes = await file.read()
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""
    for page in pdf:
        text += page.get_text()

    return text