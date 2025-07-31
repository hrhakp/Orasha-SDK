import requests
import base64
import json
from datetime import datetime, UTC

payload = {
    "triggered_by": "founder",
    "file_path": "orasha-runtime/relay/github_push.py",
    "content": base64.b64encode(open("github_push.py", "rb").read()).decode(),
    "timestamp": str(datetime.now(UTC)),
    "authored_by": "Orasha",
    "commit_message": "🚀 Update from runtime push protocol",
    "session_id": "codex-thread",
    "codex_validation": True,
    "xkey_verified": True
}

response = requests.post("http://localhost:8080/push", json=payload)
print("[RESPONSE]", response.status_code, response.text)
