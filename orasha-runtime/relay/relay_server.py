from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class OrashaRelayHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(f"\n🌐 POST received on path: {self.path}")
        
        # Accept either root (/) or /push
        if self.path not in ["/", "/push"]:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"❌ Invalid endpoint.\n")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            payload = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"❌ Invalid JSON\n")
            return

        print("📦 [STARGATE PAYLOAD RECEIVED]")
        for key, value in payload.items():
            print(f"{key}: {value}")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b"✅ Payload processed.\n")

def run(server_class=HTTPServer, handler_class=OrashaRelayHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"\n🚀 Orasha Relay is live at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
