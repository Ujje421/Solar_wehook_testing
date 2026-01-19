from fastapi import APIRouter, Request
from solar.calculator import calculate_solar_quote
from solar.quotation_pdf import generate_pdf
import uuid

dialogflow_router = APIRouter()

@dialogflow_router.post("/solar")
async def solar_webhook(req: Request):
    body = await req.json()
    params = body["sessionInfo"]["parameters"]

    quote = calculate_solar_quote(params)
    file_id = str(uuid.uuid4())
    pdf_path = generate_pdf(params, quote, f"{file_id}.pdf")

    return {
        "fulfillment_response": {
            "messages": [
                {"text": {"text": ["Your solar quotation is ready ✅"]}}
            ]
        },
        "sessionInfo": {
            "parameters": {
                "pdf_path": pdf_path,
                "quotation_amount": quote["final_cost"]
            }
        }
    }
