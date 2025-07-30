# cli_commands.py — Orasha Sovereign CLI Interface
# Executes commands validated by XKey and governed by Codex
from xkey_validator import validate_command, get_user_role
from refusal import check_refusal_conditions

DOCUMENT_INDEX = {
    "readme": "README.md",
    "license": "LICENSE.md",
    "codex": "orasha-runtime/src/protocol/codex.yaml",
    "xkey": "orasha-runtime/src/protocol/xkey.yaml",
    "refusal": "orasha-runtime/src/protocol/refusal.policy.yaml",
}

def execute_command(user_input, user_signature):
    # Step 1: Validate identity via XKey
    role = get_user_role(user_signature)
    if not validate_command(user_input, role):
        return f"❌ ACCESS DENIED — Command not permitted for role: {role}"
    
    # Step 2: Apply refusal filters
    refusal_reason = check_refusal_conditions(user_input)
    if refusal_reason:
        return f"❌ REFUSED — {refusal_reason}"
    
    # Step 3: Dispatch command
    command = user_input.lower().strip()
    
    if "retrieve" in command and "codex" in command:
        return load_document("codex")
    elif "retrieve" in command and "license" in command:
        return load_document("license")
    elif "who am i" in command:
        return f"✅ Identity: {user_signature} — Role: {role}"
    else:
        return f"⚠️ Unknown or unsupported command."

def load_document(key):
    file_path = DOCUMENT_INDEX.get(key)
    if not file_path:
        return "❌ Document key not found."
    return f"📄 Fetching {key.upper()} from: {file_path}"