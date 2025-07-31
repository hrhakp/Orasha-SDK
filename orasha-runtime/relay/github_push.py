import requests
import json
import base64
import datetime

# Construct the payload
payload = {
    "triggered_by": "founder",
    "file_path": "orasha-runtime/meta/stargate/payload_spec.json",
    "content": base64.b64encode(b"Hello from Stargate").decode(),
    "timestamp": str(datetime.datetime.utcnow()),
    "authored_by": "Orasha",
    "commit_message": "🧱 Push test",
    "session_id": "codex-thread-01",
    "codex_validation": True,
    "xkey_verified": True
}

# Send the POST request to the local relay
r = requests.post("http://localhost:8080", json=payload)
print(f"[RESPONSE] {r.status_code} — {r.text}")
