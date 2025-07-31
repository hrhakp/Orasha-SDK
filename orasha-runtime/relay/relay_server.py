from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class GitHubRelay(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        try:
            payload = json.loads(data)
            print("\n🔔 [GITHUB RELAY RECEIVED]")
            print(json.dumps(payload, indent=2))

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"✅ GitHub event processed.\n")
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"❌ JSON Error: {str(e)}".encode())

def run():
    print("🛰️ GitHub relay live at http://localhost:8080")
    HTTPServer(("", 8080), GitHubRelay).serve_forever()

if __name__ == "__main__":
    run()
