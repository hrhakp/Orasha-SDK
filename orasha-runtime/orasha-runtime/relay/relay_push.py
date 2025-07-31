import requests
from datetime import datetime, timezone

payload = {
    "triggered_by": "founder",
    "file_path": "orasha-runtime/meta/stargate/payload_spec.json",
    "content": "<base64-encoded-payload>",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "authored_by": "Orasha",
    "commit_message": "📦 Runtime push test",
    "session_id": "codex-thread-01",
    "codex_validation": True,
    "xkey_verified": True
}

url = "http://localhost:8080"
print(f"🔗 Posting to: {url}")
response = requests.post(url, json=payload)
print(f"[RESPONSE] {response.status_code} {response.reason}")
print(response.text)
