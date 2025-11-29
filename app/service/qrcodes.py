from fastapi.responses import StreamingResponse
from app.models.qrcodes import QrcodeModel
from io import BytesIO 
import qrcode


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