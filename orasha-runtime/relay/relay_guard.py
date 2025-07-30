import yaml
from pathlib import Path

def load_xkey():
    path = Path(__file__).resolve().parents[1] / "auth" / "xkey.yaml"
    with open(path, 'r') as f:
        return yaml.safe_load(f)

xkey = load_xkey()

def is_signed(session_role):
    return session_role in xkey.get("authorized_roles", [])

def authorize_execution(session_role):
    if not is_signed(session_role):
        raise PermissionError(f"Execution blocked for: {session_role}")
    print(f"[AUTHORIZED] Execution allowed for: {session_role}")

# Placeholder execution trigger
if __name__ == "__main__":
    authorize_execution("external_request")
