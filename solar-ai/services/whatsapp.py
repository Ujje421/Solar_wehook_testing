import requests
import os

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

def send_button_message(to):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "What type of solar installation do you need?"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "SOLAR_RESIDENTIAL",
                            "title": "🏠 Residential"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "SOLAR_COMMERCIAL",
                            "title": "🏭 Commercial"
                        }
                    }
                ]
            }
        }
    }

    requests.post(url, headers=headers, json=payload)

def send_capacity_list(to):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Select your required solar capacity"
            },
            "action": {
                "button": "Choose Capacity",
                "sections": [
                    {
                        "title": "Solar Capacity",
                        "rows": [
                            {"id": "CAP_1KW", "title": "1 kW"},
                            {"id": "CAP_3KW", "title": "3 kW"},
                            {"id": "CAP_5KW", "title": "5 kW"},
                            {"id": "CAP_10KW", "title": "10 kW"}
                        ]
                    }
                ]
            }
        }
    }

    requests.post(url, headers=headers, json=payload)
