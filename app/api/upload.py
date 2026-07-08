from fastapi import APIRouter, UploadFile, File
from services.upload_service import UploadService

router = APIRouter()

service = UploadService()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    return service.upload(file.file)