from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RelayHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(content_length)

        try:
            payload = json.loads(data.decode('utf-8'))
            print("[RECEIVED PAYLOAD]")
            print(json.dumps(payload, indent=2))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"ERROR: {str(e)}".encode())

    def log_message(self, format, *args):
        return  # Suppress default logging

if __name__ == "__main__":
    print("Listening on http://localhost:8080")
    server = HTTPServer(("localhost", 8080), RelayHandler)
    server.serve_forever()
