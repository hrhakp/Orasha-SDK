#import subprocess
import relay_guard

def push_to_github():
    # This is your actual Git push logic
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Codex-verified commit"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    relay_guard.run_relay_guard()
    push_to_github()