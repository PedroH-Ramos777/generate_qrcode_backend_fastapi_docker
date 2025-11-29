from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import qrcodes

app = FastAPI(
    title="Projeto QR Code",
    description="Projeto de aplicação FastAPI para geração de QR Codes a partir de urls.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qrcodes.router)