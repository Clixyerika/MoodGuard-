from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.speech import handle_speech
from app.models.schema import SpeechResponse

import os
import shutil

router = APIRouter()

@router.post("/speech/analyze", response_model=SpeechResponse)
async def analyze_speech(file: UploadFile = File(...)):
    audio_path = f"temp_audio/{file.filename}"
    os.makedirs("temp_audio", exist_ok=True)
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = handle_speech(audio_path)
    os.remove(audio_path)

    # Return JSON with path to download response audio
    return {
        "text": result["text"],
        "emotion": result["emotion"],
        "confidence": result["confidence"],
        "response_text": result["response_text"],
        "audio_url": f"/speech/response-audio"
    }

@router.get("/speech/response-audio")
async def get_response_audio():
    return FileResponse("temp_audio/response.mp3", media_type="audio/mpeg")
