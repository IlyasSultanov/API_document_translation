from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.responses import FileResponse

from ...connect_api.connect_api import translate_text
from ...service.translate import (
    process_docx,
    create_translated_docx
)


router = APIRouter(tags=["Translate-docx"])


@router.post("/translate_docx/")
async def translate_docx(file: UploadFile = File(...)):
    """Основной endpoint для перевода docx файлов"""
    if not file.filename.endswith('.docx'):
        raise HTTPException(status_code=400, detail="Only .docx files are accepted")

    original_text = await process_docx(file)

    translated_text = await translate_text(original_text)

    file.file.seek(0)
    output_path = await create_translated_docx(file, translated_text)

    return FileResponse(
        output_path,
        filename="translated_" + file.filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
