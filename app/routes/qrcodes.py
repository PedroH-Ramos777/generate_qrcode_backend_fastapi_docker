from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.qrcodes import QrcodeModel
from app.service.qrcodes import gerador_qrcode_imagem


router = APIRouter(
    prefix="/qrcodes",
    tags=["QrCodes"]
)

@router.post('/')
def criar_qrcode(data: QrcodeModel):

    try:
        return gerador_qrcode_imagem(data=data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno ao gerar o QR Code: {e}"
        )
        