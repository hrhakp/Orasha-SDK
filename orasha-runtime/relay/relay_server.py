# relay_server.py

import relay_guard
import subprocess

def run_server_push():
    print("[RELAY SERVER] Push requested...")
    relay_guard.run_relay_guard()
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "relay: Codex-sealed commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[RELAY SERVER] Push completed.")
    except subprocess.CalledProcessError as e:
        print("[RELAY SERVER] Git push failed:", str(e))

if __name__ == "__main__":
    run_server_push()