import hashlib
import subprocess
import os

def validate_codex_integrity():
    codex_path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
    expected_digest = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

    if not os.path.isfile(codex_path):
        print("[RELAY PUSH] ❌ Codex file not found.")
        return False

    try:
        with open(codex_path, "rb") as f:
            content = f.read()
    except Exception as e:
        print("[RELAY PUSH] ❌ Failed to read Codex file:", str(e))
        return False

    actual_digest = hashlib.sha256(content).hexdigest()

    if actual_digest == expected_digest:
        print("[RELAY PUSH] ✅ Digest match. Codex integrity validated.")
        return True
    else:
        print("[RELAY PUSH] ❌ Digest mismatch.")
        print("  Expected:", expected_digest)
        print("  Actual:  ", actual_digest)
        return False

def execute_push():
    print("[RELAY PUSH] 🧱 Executing Git push...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "relay: Codex-sealed commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[RELAY PUSH] ✅ Push complete.")
    except subprocess.CalledProcessError as e:
        print("[RELAY PUSH] ❌ Git error:", str(e))

if __name__ == "__main__":
    if validate_codex_integrity():
        execute_push()
    else:
        print("[RELAY PUSH] ❌ Aborted: Codex validation failed.")