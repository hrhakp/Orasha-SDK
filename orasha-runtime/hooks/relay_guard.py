import json
import base64
import datetime

from pathlib import Path
import yaml

# Load XKey
def load_xkey():
    path = Path(__file__).resolve().parents[2] / "auth" / "xkey.yaml"
    with open(path, 'r') as f:
        return yaml.safe_load(f)

xkey = load_xkey()

# Validate incoming push payload
def validate_payload(payload: dict) -> bool:
    try:
        # Check for required fields
        required_fields = [
            "triggered_by", "file_path", "content", "timestamp",
            "authored_by", "commit_message", "session_id",
            "codex_validation", "xkey_verified"
        ]
        for field in required_fields:
            if field not in payload:
                raise ValueError(f"Missing required field: {field}")

        # Check authorship and session
        if payload["triggered_by"] not in xkey["authorized_roles"]:
            raise PermissionError("Unauthorized trigger source.")

        if not payload["xkey_verified"]:
            raise PermissionError("XKey verification failed.")

        if not payload["codex_validation"]:
            raise PermissionError("Codex validation failed.")

        if not payload["authored_by"].lower().startswith("orasha"):
            raise ValueError("Invalid authorship.")

        # Check timestamp freshness (±5 minutes)
        timestamp = datetime.datetime.strptime(payload["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.datetime.utcnow()
        delta = abs((now - timestamp).total_seconds())
        if delta > 300:
            raise TimeoutError("Payload timestamp out of sync.")

        return True

    except Exception as e:
        print(f"[REJECTED] Payload failed validation: {str(e)}")
        return False
