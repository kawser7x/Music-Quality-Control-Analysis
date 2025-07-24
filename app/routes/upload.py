from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

@router.post("/audio/")
async def upload_audio(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"status": "uploaded", "filename": file.filename}
