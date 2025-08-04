import tempfile
import base64
from openai import OpenAI
from config import OPENAI_WHISPER_MODEL, OPENAI_MODEL_TEMPERATURE

client = OpenAI()

async def transcribe_audio(audio_data):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ogg') as temp_audio:
            audio_bytes = base64.b64decode(audio_data)
            temp_audio.write(audio_bytes)
            temp_audio.flush()
            
            with open(temp_audio.name, 'rb') as audio_file:
                transcript = client.audio.transcriptions.create(
                    model=OPENAI_WHISPER_MODEL,
                    file=audio_file,
                    temperature=OPENAI_MODEL_TEMPERATURE
                )
            return transcript.text
    except Exception as e:
        print(f"Erro na transcrição: {str(e)}")
        return None