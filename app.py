from fastapi import FastAPI, Request

from message_buffer import buffer_message
from transcribe_audio import transcribe_audio

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get("data").get("key").get("remoteJid")
    message = data.get("data").get("message").get("conversation")
    audio_message = data.get("data").get("message").get("audioMessage")

    if chat_id and message and not '@g.us' in chat_id:
        await buffer_message(chat_id, message)

        # Verifica se é uma mensagem de áudio
    if chat_id and audio_message and not '@g.us' in chat_id:
        audio_data = data.get("data").get("message").get("base64")
        if audio_data:    
            transcribed_text = await transcribe_audio(audio_data)
            await buffer_message(chat_id, transcribed_text)

    return {"status": "ok"}