from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def start_server(handler=None):
    class OrashaRelay(BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            try:
                payload = json.loads(body)
                print("[RECEIVED] Payload:")
                print(json.dumps(payload, indent=2))

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"status": "ok"}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Invalid JSON: {e}".encode())

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, handler or OrashaRelay)
    print("Relay server running at http://localhost:8080")
    httpd.serve_forever()
