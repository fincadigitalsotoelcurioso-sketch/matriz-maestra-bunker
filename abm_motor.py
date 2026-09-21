import http.server
import socketserver
import json

PORT = 8000

class ABMHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            # Procesamiento de la matriz de contenido B2B
            cliente = payload.get("empresa", "Desconocido")
            vector = payload.get("vector_estrategico", "General")
            
            respuesta = {
                "status": "SUCCESS",
                "mensaje": f"Matriz ABM desplegada con éxito para {cliente}",
                "vector_activo": vector
            }
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(respuesta).encode('utf-8'))
            
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

with socketserver.TCPServer(("", PORT), ABMHandler) as httpd:
    print(f"MOTOR ABM ACTIVO EN PUERTO {PORT}...")
    httpd.serve_forever()
