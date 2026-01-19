from fastapi import APIRouter, Request
from whatsapp.whatsapp_api import (
    send_text,
    send_reply_buttons,
    send_list,
    send_cta_url
)

router = APIRouter()


@router.post("/message")
async def whatsapp(req: Request):
    body = await req.json()

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    user = message["from"]

    # TEXT MESSAGE
    if message["type"] == "text":
        text = message["text"]["body"].lower()

        if "solar" in text:
            send_reply_buttons(
                user,
                "What would you like to do? ☀️",
                buttons=[
                    {"id": "GET_QUOTE", "title": "Get Solar Quote"},
                    {"id": "FAQ", "title": "Solar FAQ"},
                    {"id": "CALL_ME", "title": "Talk to Expert"}
                ]
            )

    # BUTTON CLICK
    if message["type"] == "interactive":
        action = message["interactive"]

        # Reply button
        if action["type"] == "button_reply":
            button_id = action["button_reply"]["id"]

            if button_id == "GET_QUOTE":
                send_text(user, "Please tell your monthly electricity bill 💡")

            elif button_id == "FAQ":
                send_list(
                    user,
                    header="Solar FAQs",
                    body="Choose a question",
                    sections=[
                        {
                            "title": "Solar Basics",
                            "rows": [
                                {"id": "FAQ_1", "title": "How much does solar cost?"},
                                {"id": "FAQ_2", "title": "Is subsidy available?"}
                            ]
                        }
                    ]
                )

            elif button_id == "CALL_ME":
                send_text(user, "Our solar expert will call you shortly 📞")

        # List selection
        if action["type"] == "list_reply":
            row_id = action["list_reply"]["id"]

            if row_id == "FAQ_1":
                send_text(user, "Solar typically costs ₹50,000–₹60,000 per kW.")

            elif row_id == "FAQ_2":
                send_text(user, "Yes, government subsidy up to 40% is available.")

    return {"status": "ok"}
