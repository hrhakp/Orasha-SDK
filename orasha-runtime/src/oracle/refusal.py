import yaml
from pathlib import Path

def load_xkey():
    path = Path(__file__).resolve().parent.parent.parent / 'auth' / 'xkey.yaml'
    with open(path, 'r') as f:
        return yaml.safe_load(f)

xkey = load_xkey()

def is_user_authorized(user_role):
    return user_role in xkey.get('authorized_roles', [])

# Example usage (placeholder):
current_user_role = "founder"

if not is_user_authorized(current_user_role):
    raise PermissionError("Access denied: unauthorized role signature.")
