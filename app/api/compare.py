from fastapi import APIRouter, UploadFile, File
from app.services.compare_service import CompareService

router = APIRouter()

service = CompareService()

@router.post("/compare")
async def compare(
        previous_file: UploadFile = File(...),
        current_file: UploadFile = File(...),
):
    return service.compare(previous_file.file, current_file.file)
