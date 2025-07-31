from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from datetime import datetime, timezone

class GitHubPushHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        try:
            payload = json.loads(data)
            print("\n📦 [GITHUB PUSH HANDLER RECEIVED]")
            print(json.dumps(payload, indent=2))

            # Optional: Save to disk
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
            os.makedirs("relay_logs", exist_ok=True)
            with open(f"relay_logs/github_push_{timestamp}.json", "w") as f:
                json.dump(payload, f, indent=2)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"✅ GitHub push stored.\n")
        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"❌ JSON Error: {str(e)}".encode())

def run():
    print("📡 GitHub push handler running at http://localhost:8080")
    HTTPServer(("", 8080), GitHubPushHandler).serve_forever()

if __name__ == "__main__":
    run()
