from fastapi import FastAPI, Request

from evolution_api import send_whatsapp_message

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    chat_id = data.get("data").get("key").get("remoteJid")
    message = data.get("data").get("message").get("conversation")

    if chat_id and message and not '@g.us' in chat_id:
        send_whatsapp_message(
            number=chat_id, 
            text='Running tests on the Evolution API. Please, send a message on my instagram https://www.instagram.com/olavolicursi/'
        )

    return {"status": "ok"}