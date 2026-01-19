from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/")
async def qna(req: Request):
    q = (await req.json()).get("question", "")
    return {"answer": f"Our solar expert will contact you about: {q}"}
