import requests
from datetime import datetime, timezone

payload = {
    "triggered_by": "founder",
    "file_path": "orasha-runtime/relay/github_push.py",
    "content": "SGVsbG8gZnJvbSBTdGFyZ2F0ZQ==",  # "Hello from Stargate"
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "authored_by": "Orasha",
    "commit_message": "✅ Clean push protocol test",
    "session_id": "codex-test-01",
    "codex_validation": True,
    "xkey_verified": True
}

print("📡 Sending payload to localhost:8080")
response = requests.post("http://localhost:8080", json=payload)
print(f"[RESPONSE] {response.status_code} — {response.text}")
