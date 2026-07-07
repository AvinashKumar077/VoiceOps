from fastapi import APIRouter, UploadFile, File
import time

from app.services.upload_service import UploadService

router = APIRouter()

service = UploadService()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    start = time.perf_counter()

    conversations = service.upload(file.file)

    print(f"Total: {time.perf_counter() - start:.3f}s")

    return conversations