import hashlib

def validate_codex_integrity():
    codex_path = r"C:\Users\hrhak\downloads\Orasha-SDK-main\orasha-runtime\codexlaw\CODEX_1.II.md"
    expected_digest = "9f5ddb0599be58840b43bfe26432a8ff4172445b62de9f3ae6ffbfbf7d7a0eac"

    try:
        with open(codex_path, "rb") as f:
            content = f.read()
            actual_digest = hashlib.sha256(content).hexdigest()
    except:
        return False

    return actual_digest == expected_digest

def run_relay_guard():
    if not validate_codex_integrity():
        print("[PUSH BLOCKED] Codex integrity validation failed.")
        exit(1)

    print("[RELAY GUARD] Validation passed. Proceeding with GitHub push authorization...")

if __name__ == "__main__":
    run_relay_guard()