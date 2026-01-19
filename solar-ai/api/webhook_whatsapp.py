from fastapi import APIRouter, Request
from whatsapp.whatsapp_api import send_whatsapp_text
from flask import Blueprint, request
from services.whatsapp import send_capacity_list

whatsapp_router = APIRouter()



whatsapp_bp = Blueprint("whatsapp", __name__)

@whatsapp_bp.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    data = request.json

    try:
        entry = data["entry"][0]
        change = entry["changes"][0]
        value = change["value"]
        message = value["messages"][0]

        from_number = message["from"]

        # BUTTON CLICK
        if message["type"] == "interactive":
            button_id = message["interactive"]["button_reply"]["id"]

            if button_id == "SOLAR_RESIDENTIAL":
                send_capacity_list(from_number)

            elif button_id == "SOLAR_COMMERCIAL":
                send_capacity_list(from_number)

    except Exception as e:
        print("Webhook error:", e)

    return "OK", 200


@whatsapp_router.post("/message")
async def receive_whatsapp(req: Request):
    data = await req.json()
    msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
    user = msg["from"]

    send_whatsapp_text(user, "Welcome to Solar AI ☀️")
    return {"status": "ok"}
