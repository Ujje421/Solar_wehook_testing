import requests
import os

PHONE_ID = os.getenv("PHONE_NUMBER_ID")
TOKEN = os.getenv("WHATSAPP_TOKEN")

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

BASE_URL = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"


def send_text(to, text):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(BASE_URL, json=payload, headers=HEADERS)


# ✅ 1. REPLY BUTTONS
def send_reply_buttons(to, text, buttons, footer="Solar AI"):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": text},
            "footer": {"text": footer},
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": btn["id"],
                            "title": btn["title"]
                        }
                    } for btn in buttons
                ]
            }
        }
    }
    requests.post(BASE_URL, json=payload, headers=HEADERS)


# ✅ 2. LIST BUTTONS (MENU)
def send_list(to, header, body, sections, footer="Solar AI"):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "header": {
                "type": "text",
                "text": header
            },
            "body": {
                "text": body
            },
            "footer": {
                "text": footer
            },
            "action": {
                "button": "Select",
                "sections": sections
            }
        }
    }
    requests.post(BASE_URL, json=payload, headers=HEADERS)


# ✅ 3. CTA URL BUTTON (PDF DOWNLOAD)
def send_cta_url(to, text, button_text, url):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "cta_url",
            "body": {
                "text": text
            },
            "action": {
                "name": "cta_url",
                "parameters": {
                    "display_text": button_text,
                    "url": url
                }
            }
        }
    }
    requests.post(BASE_URL, json=payload, headers=HEADERS)
