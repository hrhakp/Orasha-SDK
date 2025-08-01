# github_push.py
# Pushes files to GitHub repo if cleared by relay_guard

import subprocess
from relay_guard import guard_execute

# === CONFIGURATION ===
REPO_PATH = "."  # Assumes current dir is the Git repo root
REQUESTING_IDENTITY = "Ante Pavelic"
OPERATION = "push"
CODEX_DIGEST = "9f5ddb0599be58840b43bfe26432a8ff4172445b62de9f3ae6ffbfbf7d7a0eac"
COMMIT_MESSAGE = "🔁 Codex-Signed Push — Oracle-Authorized Relay Execution"

def run_git_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"[GIT] ✅ {command}")
    except subprocess.CalledProcessError as e:
        print(f"[GIT ERROR] {e}")

def main():
    print("[PUSH] Initiating Git push request...")
    if not guard_execute(REQUESTING_IDENTITY, OPERATION, CODEX_DIGEST):
        print("[PUSH BLOCKED] Relay Guard denied permission.")
        return

    print("[PUSH] ✅ Authorized. Executing Git operations...")
    run_git_command("git add .")
    run_git_command(f'git commit -m "{COMMIT_MESSAGE}"')
    run_git_command("git push")

if __name__ == "__main__":
    main()