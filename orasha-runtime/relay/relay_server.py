from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class StargateRelayHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/push":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        print("\n🔐 [STARGATE] Payload received")
        print(json.dumps(payload, indent=2))

        # Respond
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "status": "success",
            "received": True
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run(server_class=HTTPServer, handler_class=StargateRelayHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🛰️ [STARGATE RELAY ACTIVE] Listening on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
