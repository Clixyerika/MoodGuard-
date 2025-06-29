from vosk import Model, KaldiRecognizer
import wave
import json
from pathlib import Path

model_dir = Path(__file__).parent.parent / "models" / "vosk-model-small-en-us-0.15"
print("Looking for model at:", model_dir)

model = Model(str(model_dir))

def recognize_stream(data: bytes) -> str:
    # Vosk expects raw PCM WAV-like chunks
    rec = KaldiRecognizer(model, 16000)
    rec.AcceptWaveform(data)
    result = json.loads(rec.FinalResult())
    return result.get("text", "")
