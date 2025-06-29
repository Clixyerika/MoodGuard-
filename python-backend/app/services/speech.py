import whisper
from gtts import gTTS
import os
from app.services.emotion import analyze_emotion

model = whisper.load_model("base")

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]

def generate_response(emotion: str) -> str:
    # Very simple mood-based response
    if emotion == "happy":
        return "You sound happy! Keep smiling!"
    elif emotion == "sad":
        return "I'm here for you. Want to talk about it?"
    else:
        return f"I noticed you're feeling {emotion}. Let's chat more!"

def synthesize_speech(text: str, filename: str = "response.mp3") -> str:
    tts = gTTS(text)
    output_path = f"temp_audio/{filename}"
    tts.save(output_path)
    return output_path

def handle_speech(audio_path: str):
    text = transcribe_audio(audio_path)
    emotion_result = analyze_emotion(text)
    response_text = generate_response(emotion_result["emotion"])
    audio_response_path = synthesize_speech(response_text)
    return {
        "text": text,
        "emotion": emotion_result["emotion"],
        "confidence": emotion_result["confidence"],
        "response_text": response_text,
        "audio_response_path": audio_response_path
    }
