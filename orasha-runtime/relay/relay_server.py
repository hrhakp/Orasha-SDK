from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class OrashaRelay(BaseHTTPRequestHandler):
    def do_POST(self):
        print(f"\n🔌 Received POST on {self.path}")
        content_length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(content_length)

        try:
            payload = json.loads(data)
            print("✅ Payload:")
            print(json.dumps(payload, indent=2))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        except Exception as e:
            print("❌ Error:", str(e))
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, OrashaRelay)
    print("🛰️ Relay is live on http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
