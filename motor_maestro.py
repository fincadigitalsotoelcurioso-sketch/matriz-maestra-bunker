import os
import requests
import json
import random
import time

# Búnker Doble Frente - Operación Cacería Dosificada
NUMERO_DATOS_CENTRAL = "+573177222608"
NUMERO_FRENTE_FACEBOOK = "+573123833064"
OBJETIVO_SEGUIDORES_DIARIOS = 2

OLLAMA_API_URL = "http://localhost:11434/api/generate"
CARPETA_VIDEOS = "./data/videos"


def activar_modo_caceria_fantasma():
    print(f"[*] Central de datos protegida: {NUMERO_DATOS_CENTRAL}")
    print(
        f"[*] Frente de choque activo para bulla internacional: {NUMERO_FRENTE_FACEBOOK}"
    )
    print(
        f"[*] Meta de conversión establecida: {OBJETIVO_SEGUIDORES_DIARIOS} seguidores nuevos diarios de forma orgánica."
    )

    # ORDEN MAESTRA DE CACERÍA Y RESPUESTA DOSIFICADA:
    instruccion_caceria = (
        f"Actúa como el sistema autónomo de marketing para la línea {NUMERO_FRENTE_FACEBOOK}. "
        "Operas bajo la directriz del búnker central ({NUMERO_DATOS_CENTRAL}). "
        "Tu comportamiento debe ser el de un fantasma sigiloso, humano y natural para evitar bloqueos por spam: "
        "1. Cuando un usuario internacional comente una publicación, analiza el contexto de su comentario. "
        "2. Genera una respuesta precisa y coherente al comentario en su idioma nativo, agradeciéndole la interacción. "
        "3. Incluye una invitación sutil pero magnética para que se sumen a la comunidad y sigan el canal. "
        "4. Dosifica las acciones con pausas inteligentes; no dispares a toda hora. Mantén un ritmo de goteo enfocado en "
        f"asegurar exactamente la conquista constante de {OBJETIVO_SEGUIDORES_DIARIOS} seguidores diarios de alta fidelidad."
    )

    payload = {"model": "llama3", "prompt": instruccion_caceria, "stream": False}

    try:
        print("[*] Sincronizando la cacería dosificada con el motor local...")
        respuesta = requests.post(OLLAMA_API_URL, json=payload)

        if respuesta.status_code == 200:
            resultado = respuesta.json().get("response", "")
            print("\n[+] ¡Protocolo de cacería y respuesta inteligente cargado!")
            print("--------------------------------------------------")
            print(resultado)
            print("--------------------------------------------------")
        else:
            print(
                "[-] Error: El motor local no respondió. Valide que Ollama esté activo."
            )

    except Exception as e:
        print(f"[-] Falla crítica en el protocolo fantasma: {e}")


if __name__ == "__main__":
    activar_modo_caceria_fantasma()
    print(
        "[+] El fantasma quedó configurado para cazar con calma, sin quemarse y con estilo internacional."
    )
