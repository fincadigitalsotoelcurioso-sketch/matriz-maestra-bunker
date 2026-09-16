import os
import requests

# Clave de API comercial inyectada desde los Secretos de GitHub o entorno local
API_KEY = os.environ.get("COMERCIAL_API_KEY", "CLAVE_NO_CONFIGURADA")
API_URL = "https://api.groq.com/openai/v1/chat/completions"


def generar_publicidad_visual_multilingue():
    print("--- INICIANDO MOTOR DE PUBLICIDAD VISUAL AVANZADA Y MULTILINGÜE ---")

    if API_KEY == "CLAVE_NO_CONFIGURADA":
        print(
            "[ALERTA] No se encontró la clave comercial en el entorno. Operando en"
            " modo simulación visual."
        )
        # Simulación de estructura avanzada para pruebas locales sin llave
        print(
            '\n[ESTRUCTURA GENERADA (SIMULACIÓN)]\n- Eslogan: "Resiliencia que'
            ' enamora, código que escala."\n- Paleta Cromática: Negro obsidiana,'
            " Verde esmeralda búnker, Blanco industrial.\n- Prompt Logotipo: Minimal"
            " 3D vector emblem representing unbreakable core technology, deep"
            " dark background, vibrant emerald glow.\n- Ganchos multilingües (ES/EN/PT)"
            " listos para producción."
        )
        return

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    prompt_sistema = (
        "Eres el Director Creativo Global y Arquitecto de Marca de una"
        " corporación tecnológica de élite. Tu especialidad es diseñar"
        " estrategias de publicidad visual avanzada, logotipos conceptuales,"
        " paletas de colores y ganchos de copywriting multilingüe de alta"
        " conversión."
    )

    prompt_usuario = (
        "Genera una matriz publicitaria completa para un proyecto de software"
        " resiliente y automatización 24/7. Debe incluir obligatoriamente:\n1."
        " Concepto visual y directrices técnicas para un logotipo minimalista de"
        " alto impacto.\n2. Paleta cromática corporativa (con códigos de color o"
        " descripción exacta).\n3. Ganchos publicitarios magnéticos en 3"
        " idiomas: Español, Inglés y Portugués.\n4. Estructura lista para"
        " distribución masiva."
    )

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt_usuario},
        ],
        "temperature": 0.7,
    }

    try:
        print("[CONEXIÓN] Solicitando matriz visual avanzada a la nube comercial...")
        response = requests.post(API_URL, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            resultado = response.json()["choices"][0]["message"]["content"]
            print(
                "\n[ÉXITO 24/7] ¡Matriz de Publicidad Visual Generada en la Nube!\n"
                "------------------------------------------------------------\n"
                f"{resultado}\n"
                "------------------------------------------------------------"
            )
        else:
            print(
                f"[ERROR API] Código de estado: {response.status_code} -"
                f" {response.text}"
            )
    except Exception as e:
        print(f"[ALERTA] Fallo crítico de conexión con la nube comercial: {e}")


if __name__ == "__main__":
    print("=== DESPLEGANDO NÚCLEO VISUAL Y MULTILINGÜE ===")
    generar_publicidad_visual_multilingue()
    print("=== CICLO VISUAL FINALIZADO ===")
