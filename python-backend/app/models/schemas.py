from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    text: str
    emotion: str
    confidence: float
