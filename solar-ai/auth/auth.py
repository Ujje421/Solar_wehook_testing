from fastapi import APIRouter, Request
import os

router = APIRouter()

@router.post("/login")
async def login(req: Request):
    body = await req.json()
    if body["user"] == os.getenv("ADMIN_USER") and body["pass"] == os.getenv("ADMIN_PASS"):
        return {"token": "admin-token"}
    return {"error": "invalid"}
