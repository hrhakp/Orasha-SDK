from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class OrashaRelayHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/push":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data)
                print("\n🔐 [RECEIVED PAYLOAD]")
                for key, value in data.items():
                    print(f"{key}: {value}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"✅ Payload received and processed.\n")
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"❌ JSON Error: {str(e)}".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"❌ Invalid endpoint.\n")

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, OrashaRelayHandler)
    print("🚀 Orasha Relay listening on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
