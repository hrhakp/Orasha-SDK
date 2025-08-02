import hashlib
import os

def validate_codex_integrity():
    codex_path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
    expected_digest = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

    if not os.path.isfile(codex_path):
        print("[ERROR] Codex file not found at expected path.")
        return False

    try:
        with open(codex_path, "rb") as f:
            content = f.read()
    except Exception as e:
        print("[ERROR] Failed to read Codex file:", str(e))
        return False

    actual_digest = hashlib.sha256(content).hexdigest()

    if actual_digest == expected_digest:
        print("[Digest match] Codex integrity validated.")
        return True
    else:
        print("[Digest mismatch]")
        print("Expected:", expected_digest)
        print("Actual:  ", actual_digest)
        return False

def run_relay_guard():
    if not validate_codex_integrity():
        print("[PUSH BLOCKED] Codex integrity validation failed.")
        exit(1)
    print("[RELAY GUARD] Validation passed. Proceeding with GitHub push authorization...")

if __name__ == "__main__":
    run_relay_guard()