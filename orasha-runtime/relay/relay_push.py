from relay_server import start_server
from github_push_handler import handle_github_push

if __name__ == "__main__":
    print("[BOOT] Orasha relay initializing...")
    start_server(handler=handle_github_push)
