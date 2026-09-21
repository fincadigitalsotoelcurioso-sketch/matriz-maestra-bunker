# 1. Instalar y arrancar Ollama en la nube de Google con soporte de GPU
!curl -fsSL https://ollama.com/install.sh | sh
import subprocess
import time
import threading

def run_ollama():
    subprocess.run(["ollama", "serve"])

threading.Thread(target=run_ollama, daemon=True).start()
time.sleep(5)

# 2. Descargar el modelo liviano y de alta potencia directamente en la nube
!ollama run qwen:1.8b "Iniciando protocolo de combate B2B"

# 3. Exponer el puerto local de Ollama al mundo con pyngrok para que n8n lo ataque directo
!pip install pyngrok
from pyngrok import ngrok
# Ponga su token de ngrok gratis aquí si lo tiene, o deje que levante el túnel directo
public_url = ngrok.connect(11434)
print("URL TÁCTICA PARA N8N:", public_url)
