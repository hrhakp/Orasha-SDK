import json
import base64
import datetime
import requests

def create_push_payload(file_path, content_str, commit_message):
    payload = {
        "triggered_by": "founder",
        "file_path": file_path,
        "content": base64.b64encode(content_str.encode()).decode(),
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "authored_by": "Orasha",
        "commit_message": commit_message,
        "session_id": "codex-thread",
        "codex_validation": True,
        "xkey_verified": True
    }
    return payload

def send_push_payload(payload, relay_url):
    headers = {"Content-Type": "application/json"}
    response = requests.post(relay_url, data=json.dumps(payload), headers=headers)
    return response.status_code, response.text

# Example Usage (stub)
if __name__ == "__main__":
    test_file_path = "orasha-runtime/test/example.md"
    test_content = "This is a test payload from Stargate."
    test_commit = "Test Stargate push relay logic"

    payload = create_push_payload(test_file_path, test_content, test_commit)
    print("[STARGATE PAYLOAD]", json.dumps(payload, indent=2))
    
    # Example relay URL (stubbed)
    # relay_url = "http://localhost:8000/relay"
    # status, response = send_push_payload(payload, relay_url)
    # print(f"[RELAY RESPONSE] {status}: {response}")
