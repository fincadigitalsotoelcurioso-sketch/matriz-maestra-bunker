import os
import hmac
import hashlib
from fastapi import FastAPI, HTTPException, Request, Header
from pydantic import BaseModel
from datetime import datetime

# --- CONFIGURACIÓN DE SEGURIDAD ---
# La clave secreta debe estar configurada en sus variables de entorno
SECRET_KEY = os.environ.get("HMAC_SECRET", "clave-segura-por-defecto").encode()

app = FastAPI()

class RegistroImpacto(BaseModel):
    accion: str
    impacto_estimado: float
    beneficiarios: int

# --- MIDDLEWARE DE SEGURIDAD (HMAC) ---
async def verificar_firma(request: Request, x_signature: str = Header(...)):
    body = await request.body()
    expected_signature = hmac.new(SECRET_KEY, body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected_signature, x_signature):
        raise HTTPException(status_code=403, detail="Firma no autorizada")

# --- LÓGICA DE PRODUCCIÓN 24/7 ---
@app.post("/log_impacto/", dependencies=[None]) # Puede añadir verificar_firma aquí
async def registrar(data: RegistroImpacto):
    try:
        # Log centralizado con timestamp
        print(f"[{datetime.now()}] Impacto registrado: {data.accion}")
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error de persistencia en búnker")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
