from fastapi import FastAPI
from api.dialogflow_webhook import router as df_router
from api.whatsapp_webhook import router as wa_router
from api.open_qna import router as qna_router
from auth.auth import router as auth_router

app = FastAPI()

app.include_router(df_router, prefix="/dialogflow")
app.include_router(wa_router, prefix="/whatsapp")
app.include_router(qna_router, prefix="/qna")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def health():
    return {"status": "Solar AI running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)