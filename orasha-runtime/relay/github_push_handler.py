from http.server import BaseHTTPRequestHandler
import json
import os
from datetime import datetime, timezone

def handle_github_push(*args, **kwargs):
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length)

            try:
                payload = json.loads(data)
                print("[GITHUB PUSH RECEIVED]")
                print(json.dumps(payload, indent=2))

                timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
                os.makedirs("relay_logs", exist_ok=True)
                with open(f"relay_logs/github_push_{timestamp}.json", "w") as f:
                    json.dump(payload, f, indent=2)

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Push received and logged.")
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error: {e}".encode())
    return Handler(*args, **kwargs)
