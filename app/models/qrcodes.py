from pydantic import BaseModel

class QrcodeModel(BaseModel):
    url: str    
    titulo: str
