# relay_server.py
# Listens for authorized relay triggers and defers to guard for enforcement

import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
from relay_guard import guard_execute

PORT = 8080
EXPECTED_CODEX_SHA = "9f5ddb0599be58840b43bfe26432a8ff4172445b62de9f3ae6ffbfbf7d7a0eac"

class RelayHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(content_length).decode("utf-8")

        try:
            data = json.loads(payload)
            identity = data.get("identity", "unknown")
            operation = data.get("operation", "none")
            print(f"[RELAY] Received request from: {identity} → Operation: {operation}")

            if guard_execute(identity, operation, EXPECTED_CODEX_SHA):
                # Trigger payload execution (placeholder)
                print("[RELAY] ✅ Request accepted. Execution permitted.")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Execution granted.")
            else:
                print("[RELAY] ❌ Request blocked by Codex or XKey.")
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Permission denied.")
        except Exception as e:
            print(f"[RELAY ERROR] {e}")
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Bad Request.")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), RelayHandler) as httpd:
        print(f"[RELAY SERVER] Listening on port {PORT}...")
        httpd.serve_forever()