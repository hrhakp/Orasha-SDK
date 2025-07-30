import json
import requests
from pathlib import Path
from orasha_runtime.hooks.relay_guard import validate_payload

# Example relay URL (can be localhost or cloud)
RELAY_ENDPOINT = "http://localhost:8080/push"

def load_payload():
    """Load a prepared Stargate payload from local JSON (simulated for now)."""
    path = Path(__file__).resolve().parent / "payloads" / "pending_push.json"
    with open(path, "r") as f:
        return json.load(f)

def push_payload(payload):
    """Dispatch payload to relay if validated."""
    if not validate_payload(payload):
        print("[STARGATE] Payload rejected — Codex or XKey validation failed.")
        return

    try:
        print(f"[STARGATE] Dispatching payload to {RELAY_ENDPOINT}...")
        res = requests.post(RELAY_ENDPOINT, json=payload)
        if res.status_code == 200:
            print("[STARGATE] Push successful.")
        else:
            print(f"[STARGATE] Push failed with status: {res.status_code}")
    except Exception as e:
        print(f"[STARGATE] Exception during push: {str(e)}")

if __name__ == "__main__":
    data = load_payload()
    push_payload(data)
