from fastapi import APIRouter, UploadFile, File

from app.services.upload_service import UploadService

router = APIRouter()

service = UploadService()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    conversations = service.upload(file.file)

    return conversations
