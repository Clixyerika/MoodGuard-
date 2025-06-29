from fastapi import FastAPI
from app.routes import analyze, speech, ws_speech


app = FastAPI()

# app.include_router(analyze.router)
app.include_router(speech.router)
app.include_router(ws_speech.router)
