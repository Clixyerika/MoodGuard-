from pydantic import BaseModel

class SpeechResponse(BaseModel):
    text: str
    emotion: str
    confidence: float
    response_text: str
    audio_url: str
