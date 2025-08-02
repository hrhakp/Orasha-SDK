import subprocess
import relay_guard
import hashlib
import os

def validate_codex_integrity():
    codex_path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
    expected_digest = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

    if not os.path.isfile(codex_path):
        print("[GITHUB PUSH] Codex file not found.")
        return False

    try:
        with open(codex_path, "rb") as f:
            content = f.read()
    except Exception as e:
        print("[GITHUB PUSH] Failed to read Codex:", str(e))
        return False

    actual = hashlib.sha256(content).hexdigest()
    if actual != expected_digest:
        print("[GITHUB PUSH] Digest mismatch.")
        print("  Expected:", expected_digest)
        print("  Actual:  ", actual)
        return False

    print("[GITHUB PUSH] Digest verified.")
    return True

def push_to_github():
    print("[GITHUB PUSH] Executing Git relay...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "relay: Codex-sealed commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[GITHUB PUSH] Push complete.")
    except subprocess.CalledProcessError as e:
        print("[GITHUB PUSH] Git push failed:", str(e))

if __name__ == "__main__":
    if validate_codex_integrity():
        push_to_github()
    else:
        print("[GITHUB PUSH] Push blocked: Codex validation failed.")