from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import datetime

class RelayHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/push":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        try:
            payload = json.loads(body)
            timestamp = datetime.datetime.utcnow().isoformat()
            with open("stargate_push_log.json", "a") as log:
                log.write(json.dumps({"received_at": timestamp, "payload": payload}) + "\n")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"STARGATE push received.\n")

        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RelayHandler)
    print("[STARGATE] Relay server listening on http://localhost:8080/push")
    httpd.serve_forever()
