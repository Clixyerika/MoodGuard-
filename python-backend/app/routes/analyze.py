# from fastapi import APIRouter
# from app.models.schema import TextInput, EmotionResponse
# from app.services.emotion import analyze_emotion

# router = APIRouter()

# @router.post("/analyze", response_model=EmotionResponse)
# async def analyze(input: TextInput):
#     return analyze_emotion(input.text)
