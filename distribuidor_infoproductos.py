import http.server
import socketserver
import json

PORT = 8080

class VentaHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            payload = json.loads(post_data.decode('utf-8'))
            
            comprador = payload.get("email", "cliente@dominio.com")
            producto = payload.get("infoproducto", "Matriz Base B2B")
            
            # Lógica de despacho de ticket digital
            print(f"[VENTA DETECTADA] Despachando {producto} para {comprador}")
            
            respuesta = {
                "status": "DESPACHADO",
                "mensaje": f"Acceso al infoproducto {producto} enviado con éxito.",
                "destino": comprador
            }
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(respuesta).encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

with socketserver.TCPServer(("", PORT), VentaHandler) as httpd:
    print(f"[VPS RUNTIME] Servidor de infoproductos activo en puerto {PORT}...")
    httpd.serve_forever()
