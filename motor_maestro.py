import os
import requests
import json

# Búnker Doble Frente - Operación Coordinada
NUMERO_DATOS_CENTRAL = "+573177222608"
NUMERO_FRENTE_FACEBOOK = "+573123833064"

OLLAMA_API_URL = "http://localhost:11434/api/generate"
CARPETA_VIDEOS = "./data/videos"


def activar_bunker_doble_frente():
    print(f"[*] Central de datos blindada en: {NUMERO_DATOS_CENTRAL}")
    print(
        f"[*] Frente de choque y bulla en redes activado para: {NUMERO_FRENTE_FACEBOOK}"
    )

    if not os.path.exists(CARPETA_VIDEOS):
        os.makedirs(CARPETA_VIDEOS)
        print(f"[+] Carpeta asegurada en: {CARPETA_VIDEOS}")

    # LA ORDEN MAESTRA CON LOS DOS NÚMEROS Y SUS ROLES BIEN DEFINIDOS:
    instruccion_exacta = (
        f"Actúa como un estratega de marketing de guerrilla y operaciones digitales autónomas. "
        f"La central operativa y de datos reside en la línea {NUMERO_DATOS_CENTRAL}, mientras que la cara visible para hacer bulla, "
        f"dar lora y romper algoritmos en Facebook opera desde la línea {NUMERO_FRENTE_FACEBOOK}. "
        "Tu tarea al procesar el material de video es: "
        "1. Generar la traducción multilingüe automática para mercados internacionales. "
        "2. Diseñar subtítulos dinámicos de nivel cinematográfico con sincronización de labios perfecta (lip-sync). "
        "3. Inyectar logotipos, branding y ganchos de publicidad digital avanzada que enamoren y atraigan tráfico. "
        "4. Asegurar que la pauta y los llamados a la acción salgan a nombre del frente de Facebook sin exponer la central."
    )

    payload = {"model": "llama3", "prompt": instruccion_exacta, "stream": False}

    try:
        print("[*] Despachando directiva de doble frente al motor local...")
        respuesta = requests.post(OLLAMA_API_URL, json=payload)

        if respuesta.status_code == 200:
            resultado = respuesta.json().get("response", "")
            print("\n[+] ¡Estrategia de doble frente inyectada con éxito!")
            print("--------------------------------------------------")
            print(resultado)
            print("--------------------------------------------------")
        else:
            print(
                "[-] Error: El motor local no respondió. Revise que Ollama esté arriba."
            )

    except Exception as e:
        print(f"[-] Falla crítica en el enlace del búnker: {e}")


if __name__ == "__main__":
    activar_bunker_doble_frente()
    print("[+] Operación sincronizada. El frente de Facebook está listo para dar lora.")
