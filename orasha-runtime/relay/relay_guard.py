# relay_guard.py
# Enforces Codex protocol compliance for all relay-triggered operations

import os
import json
import hashlib

# Path to xkey.yaml (update if needed)
XKEY_PATH = "orasha-runtime/src/protocol/xkey.yaml"

def hash_file(path):
    """Generate SHA256 hash of the provided file"""
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                sha.update(chunk)
        return sha.hexdigest()
    except FileNotFoundError:
        return None

def validate_codex_integrity(expected_digest):
    """Ensure Codex file hasn't been tampered with"""
    actual_digest = hash_file("codexlaw/CODEX.md")
    if actual_digest != expected_digest:
        return False, actual_digest
    return True, actual_digest

def load_xkey():
    """Parse xkey.yaml and return as dictionary"""
    try:
        import yaml
        with open(XKEY_PATH, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load xkey.yaml: {e}")
        return {}

def check_permission(requesting_identity, operation):
    """Check if the identity has permission to execute the operation"""
    xkey = load_xkey()
    roles = xkey.get("roles", {})
    for role_name, details in roles.items():
        members = details.get("members", [])
        allowed = details.get("permissions", [])
        if requesting_identity in members and operation in allowed:
            return True
    return False

def guard_execute(requesting_identity, operation, codex_digest):
    """Final gatekeeper before any Git push or server action"""
    print(f"[GUARD] Identity: {requesting_identity}")
    print(f"[GUARD] Requested Operation: {operation}")

    codex_ok, actual_digest = validate_codex_integrity(codex_digest)
    if not codex_ok:
        print("[BLOCKED] Codex integrity check failed.")
        print(f"[Digest mismatch] Expected: {codex_digest} | Actual: {actual_digest}")
        return False

    if not check_permission(requesting_identity, operation):
        print("[BLOCKED] Permission denied by XKey.")
        return False

    print("[GRANTED] Execution approved by Codex + XKey.")
    return True

# Example (for manual test)
if __name__ == "__main__":
    # Replace with real values during integration
    identity = "Ante Pavelic"
    operation = "push"
    expected_codex_sha = "9f5ddb0599be58840b43bfe26432a8ff4172445b62de9f3ae6ffbfbf7d7a0eac"
    result = guard_execute(identity, operation, expected_codex_sha)
    print("✅ PASS" if result else "❌ DENIED")
