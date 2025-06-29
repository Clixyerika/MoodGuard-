from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from app.services.streaming_asr import recognize_stream
from app.services.emotion import analyze_emotion
from app.services.speech import synthesize_speech

import os
os.makedirs("temp_audio", exist_ok=True)
router = APIRouter()

@router.websocket("/ws/speech")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    buffer = b""

    try:
        while True:
            chunk = await websocket.receive_bytes()
            buffer += chunk

            # When buffer is big enough (~5 sec @ 16kHz PCM)
            if len(buffer) >= 16000 * 2 * 5:  # 16kHz * 2 bytes/sample * 5 sec
                text = recognize_stream(buffer)
                emotion_result = analyze_emotion(text)
                response_text = f"You said: '{text}'. You sound {emotion_result['emotion']}."

                # TTS
                audio_path = synthesize_speech(response_text, filename="ws_response.mp3")

                # Send back JSON + URL to audio
                await websocket.send_json({
                    "transcript": text,
                    "emotion": emotion_result["emotion"],
                    "response": response_text,
                    "audio_url": "/ws_speech/response-audio"
                })

                buffer = b""

    except WebSocketDisconnect:
        print("Client disconnected")


@router.get("/ws_speech/response-audio")
async def get_response_audio():
    return FileResponse("temp_audio/ws_response.mp3", media_type="audio/mpeg")
