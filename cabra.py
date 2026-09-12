import os
import json
from datetime import datetime

# ==========================================
# MATRIZ MAESTRA - NÚCLEO DE OPERACIONES
# ==========================================

DB_CRM = "clientes_matriz.json"

def inicializar_sistema():
    if not os.path.exists(DB_CRM):
        with open(DB_CRM, "w") as f:
            json.dump([], f)
    print("[MATRIZ EN LÍNEA]: Sistema base configurado y listo para operar.")

def registrar_cliente_local(nombre, email, valor):
    inicializar_sistema()
    cliente = {
        "nombre": nombre,
        "email": email,
        "valor": valor,
        "nivel": "VIP" if valor >= 500 else "Estándar",
        "fecha": str(datetime.now())
    }
    
    with open(DB_CRM, "r+") as f:
        data = json.load(f)
        data.append(cliente)
        f.seek(0)
        json.dump(data, f, indent=4)
        
    print(f"[REGISTRO EXITOSO]: Cliente {nombre} guardado en la base de datos local.")

if __name__ == "__main__":
    registrar_cliente_local("Prueba Operativa", "test@cabra.pe", 600)
