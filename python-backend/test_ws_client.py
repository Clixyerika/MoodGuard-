import asyncio
import websockets

async def test_ws():
    uri = "ws://127.0.0.1:8000/ws/speech"

    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket!")

        # Load a sample PCM WAV file (mono, 16kHz)
        with open("test_audio/sample.wav", "rb") as f:
            chunk_size = 32000  # ~1 sec at 16kHz 16-bit mono
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                await websocket.send(chunk)
                print(f"Sent chunk of {len(chunk)} bytes")
                await asyncio.sleep(0.5)

        # Wait for backend reply
        response = await websocket.recv()
        print("Response:", response)

asyncio.run(test_ws())
