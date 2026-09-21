import http.server
import socketserver
import json

PORT = 8000

class ABMHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            payload = json.loads(post_data.decode('utf-8'))
            
            # Procesamiento de la matriz de contenido B2B
            empresa = payload.get("empresa", "Corporativo")
            vector = payload.get("vector", "Distribución Directa")
            
            respuesta = {
                "status": "OK",
                "destino": empresa,
                "vector_activo": vector,
                "mensaje": "Matriz ABM inyectada correctamente en el ecosistema"
            }
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(respuesta).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

with socketserver.TCPServer(("", PORT), ABMHandler) as httpd:
    print(f"[Monacho] Motor ABM activo y escuchando en el puerto {PORT}...")
    httpd.serve_forever()
