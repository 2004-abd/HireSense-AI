from io import BytesIO

from fastapi import HTTPException, UploadFile
from pypdf import PdfReader
from docx import Document

ALLOWED_EXTENSIONS = {".pdf", ".docx"}


async def extract_text_from_upload(file: UploadFile) -> str:
    filename = file.filename or ""
    extension = "." + filename.split(".")[-1].lower() if "." in filename else ""

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX resume files are allowed.",
        )

    content = await file.read()

    try:
        if extension == ".pdf":
            reader = PdfReader(BytesIO(content))
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        else:
            document = Document(BytesIO(content))
            text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not read the uploaded resume file.",
        )

    text = " ".join(text.split())

    if len(text) < 50:
        raise HTTPException(
            status_code=400,
            detail="Resume file text is too short or unreadable.",
        )

    return text