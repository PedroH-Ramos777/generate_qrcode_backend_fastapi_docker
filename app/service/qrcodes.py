from fastapi.responses import StreamingResponse
from app.models.qrcodes import QrcodeModel
from io import BytesIO 
import qrcode
import cv2
import numpy as np



def gerador_qrcode_imagem(data: QrcodeModel):

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data.url) 
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG") 
        buffer.seek(0)


        return StreamingResponse(
            content=buffer,
            media_type="image/png",
            headers={"Content-Disposition": f"attachment; filename={data.titulo}.png"}
        )

    except Exception as e:
        print(f"Erro ao gerar o QR Code: {e}")
        raise e
    

def decodificar_qrcode(conteudo_arquivo: bytes):
    """
    Recebe os bytes de uma imagem e tenta extrair o conteúdo de um QR Code.
    """
 # Converte bytes para o formato OpenCV
    nparr = np.frombuffer(conteudo_arquivo, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return None

    # Detector de QR Code
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    
    return data if data else None