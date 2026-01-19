from fastapi import APIRouter, Request
from solar.calculator import calculate
from solar.quotation_pdf import generate_pdf
from utils.generate_id import generate_id
from storage.local_storage import save_lead
from whatsapp.whatsapp_api import BASE_URL, send_cta_url


router = APIRouter()

@router.post("/solar")
async def solar_df(req: Request):
    body = await req.json()
    params = body["sessionInfo"]["parameters"]

    lead_id = generate_id()
    quote = calculate(params)
    pdf = generate_pdf(lead_id, "Customer", quote)

    save_lead({
        "lead_id": lead_id,
        "params": params,
        "quote": quote
    })
    send_cta_url(
    to=params["phone"],
    text="Your solar quotation is ready ☀️",
    button_text="Download PDF",
    url=f"{BASE_URL}/download/{lead_id}"
)


    return {
        "fulfillment_response": {
            "messages": [
                {"text": {"text": [
                    f"Your solar quotation is ready ☀️\nFinal Cost: ₹{quote['final_cost']}"
                ]}}
            ]
        },
        "sessionInfo": {
            "parameters": {
                "lead_id": lead_id,
                "pdf_path": pdf
            }
        }
    }
