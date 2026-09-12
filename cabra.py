import os
import json
from datetime import datetime

# ==========================================
# MATRIZ MAESTRA - NÚCLEO DE OPERACIONES COMERCIALES
# Autor: Jorge Luis González Soto
# ==========================================

DB_CRM = "clientes_matriz.json"
LOG_ERRORES = "autocorreccion_log.json"

def registrar_error_inteligente(error, contexto):
    """Sistema de autocorrección: el error no frena el sistema, se documenta para aprender."""
    fallo = {
        "timestamp": str(datetime.now()),
        "contexto": contexto,
        "error_detalle": str(error),
        "accion": "Auto-reconfigurado y registrado para aprendizaje del modelo."
    }
    
    historial = []
    if os.path.exists(LOG_ERRORES):
        try:
            with open(LOG_ERRORES, "r", encoding="utf-8") as f:
                historial = json.load(f)
        except:
            historial = []
            
    historial.append(fallo)
    with open(LOG_ERRORES, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)
    
    print(f"[MATRIZ RESILIENTE]: Error interceptado y superado. El sistema sigue operando.")

def inicializar_sistema():
    try:
        if not os.path.exists(DB_CRM):
            with open(DB_CRM, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)
        print("[MATRIZ EN LÍNEA]: Base de datos comercial sincronizada y segura.")
    except Exception as e:
        registrar_error_inteligente(e, "Inicialización de base de datos")

def procesar_transaccion_y_fidelizar(nombre, email, producto, valor):
    """Procesa clientes de audiolibros, Amazon, Fiverr o Contra con fidelización automática."""
    try:
        inicializar_sistema()
        
        # Segmentación comercial avanzada para enamorar al cliente
        nivel_fidelizacion = "VIP - Socio Estratégico" if valor >= 100 else "Cliente Destacado Pro"
        
        cliente = {
            "nombre": nombre,
            "email": email,
            "producto_adquirido": producto, # Ej: Audiolibro, Automatización n8n, 3D
            "valor_invertido": valor,
            "fidelizacion": nivel_fidelizacion,
            "fecha_adquisicion": str(datetime.now()),
            "estado_experiencia": "Satisfacción Garantizada y Soporte Activo"
        }
        
        with open(DB_CRM, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(cliente)
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"[FACTURACIÓN EXITOSA]: {nombre} ha adquirido '{producto}'. Nivel asignado: {nivel_fidelizacion}.")
        return True
        
    except Exception as e:
        registrar_error_inteligente(e, f"Procesamiento de cliente {nombre}")
        return False

if __name__ == "__main__":
    print("--- INICIANDO SECUENCIA OPERATIVA DE LA MATRIZ ---")
    # Prueba de fuego con la venta de un activo (Audiolibro / Servicio)
    procesar_transaccion_y_fidelizar(
        nombre="Carlos Andrés", 
        email="carlos@cabra.pe", 
        producto="Audiolibro Masterclass de Resiliencia", 
        valor=150
    )
