# relay_push.py

import subprocess
import relay_guard

def execute_push():
    print("[RELAY PUSH] Executing Git push...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "relay: Codex-sealed commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[RELAY PUSH] Push complete.")
    except subprocess.CalledProcessError as e:
        print("[RELAY PUSH] Git push failed:", str(e))

if __name__ == "__main__":
    relay_guard.run_relay_guard()
    execute_push()