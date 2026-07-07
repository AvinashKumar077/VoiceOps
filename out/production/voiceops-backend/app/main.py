from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="VoiceOps Intelligence Engine",
    version="0.1.0"
)

app.include_router(upload_router, prefix="/api/v1")
