from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse, RedirectResponse
from app.models.qrcodes import QrcodeModel
from app.service.qrcodes import gerador_qrcode_imagem, decodificar_qrcode


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
    
@router.post("/ler-qrcode/")
async def ler_qrcode(file: UploadFile = File(...)):

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")

    contents = await file.read()

    resultado = decodificar_qrcode(contents)

    if resultado:
        return {
            "status": "sucesso", 
            "conteudo": resultado,
            "filename": file.filename
        }
    
    raise HTTPException(status_code=404, detail="Nenhum QR Code encontrado na imagem.")

@router.post("/scan-and-redirect/")
async def scan_and_redirect(file: UploadFile = File(...)):
    """
    Recebe uma imagem, tenta ler o QR Code e, se for um link (http/https), 
    retorna um Redirecionamento (303) para o site.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")

    contents = await file.read()
    resultado = decodificar_qrcode(contents)

    if resultado:
        # Verifica se o conteúdo é uma URL válida
        if resultado.startswith("http://") or resultado.startswith("https://"):
            return RedirectResponse(url=resultado, status_code=303)
        
        return {
            "status": "sucesso",
            "conteudo": resultado,
            "mensagem": "O conteúdo do QR Code não é um link."
        }
    
    raise HTTPException(status_code=404, detail="Nenhum QR Code encontrado na imagem.")