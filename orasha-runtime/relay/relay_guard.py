
import hashlib

def validate_codex_integrity():
    codex_path = r"C:\Users\hrhak\downloads\Orasha-SDK-main\orasha-runtime\codexlaw\CODEX_1.II.md"
    expected_digest = "9f5ddb0599be58840b43bfe26432a8ff4172445b62de9f3ae6ffbfbf7d7a0eac"

    print(">>> Attempting to read:", codex_path)

    try:
        with open(codex_path, "rb") as f:
            content = f.read()
            print(">>> File read: SUCCESS")
            print(">>> Byte length:", len(content))
            actual_digest = hashlib.sha256(content).hexdigest()
            print(">>> Computed digest:", actual_digest)
    except FileNotFoundError:
        print("[ERROR] Codex file not found at:", codex_path)
        return False
    except Exception as e:
        print("[ERROR] Digest validation error:", str(e))
        return False

    if actual_digest == expected_digest:
        print("[Digest match] Codex integrity validated.")
        return True
    else:
        print("[Digest mismatch]")
        print("[Expected]", expected_digest)
        print("[Actual]", actual_digest)
        return False

def run_relay_guard():
    print(">>> Running RELAY GUARD from:", __file__)
    if not validate_codex_integrity():
        print("[PUSH BLOCKED] Codex integrity validation failed.")
        exit(1)

    print("[RELAY GUARD] Validation passed. Proceeding with GitHub push authorization...")

if __name__ == "__main__":
    run_relay_guard()