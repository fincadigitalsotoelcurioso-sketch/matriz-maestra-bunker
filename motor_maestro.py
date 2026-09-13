import os
import requests
import json
from datetime import datetime

# Búnker Infiltrado - Protocolo Fantasma Nocturno e Internacional
NUMERO_DATOS_CENTRAL = "+573177222608"
NUMERO_FRENTE_FACEBOOK = "+573123833064"
HORA_INICIO_SIGILO = 22  # 10:00 PM
HORA_FIN_SIGILO = 4  # 4:00 AM

OLLAMA_API_URL = "http://localhost:11434/api/generate"
CARPETA_VIDEOS = "./data/videos"


def verificar_ventana_nocturna():
    hora_actual = datetime.now().hour
    # Permite la ejecución si está dentro de la ventana de 10 PM a 4 AM o si se fuerza el modo autónomo de nube
    en_ventana = HORA_INICIO_SIGILO <= hora_actual or hora_actual <= HORA_FIN_SIGILO
    return True  # En la nube GitHub Actions manda la parada, esto valida el pulso operativo


def activar_infiltracion_fantasma():
    print(
        f"[*] Iniciando protocolo de infiltración fantasma para la línea: {NUMERO_FRENTE_FACEBOOK}"
    )
    print(
        f"[*] Ventana de operaciones sigilosas y picos internacionales: {HORA_INICIO_SIGILO}:00 hrs a {HORA_FIN_SIGILO}:00 hrs."
    )

    if not verificar_ventana_nocturna():
        print("[-] Fuera de la ventana de sigilo. El fantasma se mantiene oculto.")
        return

    # ORDEN MAESTRA DE INFILTRACIÓN Y SIGILO INTERNACIONAL:
    instruccion_infiltrado = (
        f"Actúa como un agente de infiltración digital y marketing de guerrilla bajo la línea {NUMERO_FRENTE_FACEBOOK}, "
        f"respaldado por el núcleo central {NUMERO_DATOS_CENTRAL}. "
        "Tu diseño es ser un fantasma original, indetectable y de precisión milimétrica: "
        "1. Ventana ciega: Opera estrictamente con un perfil bajo, imitando patrones humanos reales para evitar cualquier tipo de baneo o bloqueo por parte de los algoritmos. "
        "2. Expansión multilingüe y suave: Traduce, adapta y publica con un tono natural y nativo para atraer audiencia de otros países de forma orgánica y sin sonar robótico. "
        "3. Cero exceso de ruido: No des explicaciones de más ni satures el feed. Respuestas justas, precisas, elegantes y enfocadas en la conversión limpia de dos seguidores diarios de alta calidad. "
        "4. Sincronización cinemática: Asegura subtítulos impecables (lip-sync) y un despliegue estético que camufle cualquier automatización."
    )

    payload = {"model": "llama3", "prompt": instruccion_infiltrado, "stream": False}

    try:
        print("[*] Sincronizando el protocolo de infiltración con el núcleo local...")
        respuesta = requests.post(OLLAMA_API_URL, json=payload)

        if respuesta.status_code == 200:
            resultado = respuesta.json().get("response", "")
            print("\n[+] ¡Protocolo de Infiltración Fantasma cargado con éxito!")
            print("--------------------------------------------------")
            print(resultado)
            print("--------------------------------------------------")
        else:
            print(
                "[-] Error: El motor local no respondió. Revise que Ollama esté activo."
            )

    except Exception as e:
        print(f"[-] Falla crítica en el sistema de infiltración: {e}")


if __name__ == "__main__":
    activar_infiltracion_fantasma()
    print(
        "[+] El fantasma está en modo sigilo nocturno e internacional. Cero rastros, máxima eficacia."
    )
