import requests
from datetime import datetime, timezone

payload = {
    "triggered_by": "orasha-protocol",
    "event": "github_trigger",
    "source": "orasha-runtime/relay/github_push.py",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "repo": "hrhakp/Orasha-SDK",
    "action": "manual_test_push",
    "xkey_verified": True
}

response = requests.post("http://localhost:8080", json=payload)
print("[RESPONSE]", response.status_code, response.text)
