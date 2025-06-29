This Python backend connects with several AI services to power MoodGuard:

- **HuggingFace**: For advanced natural language processing and model inference.
- **AssemblyAI**: For robust speech-to-text transcription.
- **OpenAI Whisper**: For high-quality automatic speech recognition.
- **ElevenLabs**: For realistic text-to-speech synthesis.

These integrations enable seamless voice and text interactions for users, ensuring accessibility and a smooth conversational experience.



python-backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   └── speech.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── emotion.py
│   │   └── speech.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schema.py
├── requirements.txt


