# github_push.py

import relay_guard
import subprocess

def push_to_github():
    print("[GITHUB PUSH] Initiating Git commit...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "relay: Codex-sealed commit"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[GITHUB PUSH] Completed successfully.")
    except subprocess.CalledProcessError as e:
        print("[GITHUB PUSH] Git push failed:", str(e))

if __name__ == "__main__":
    relay_guard.run_relay_guard()
    push_to_github()