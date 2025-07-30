from orasha_runtime.hooks.relay_guard import guard_relay

# Simulated runtime caller role
cli_caller_role = "oracle"  # Change to test XKey behavior

def execute_command(command: str):
    # Relay enforcement: check if role is authorized
    guard_relay()

    print(f"[EXECUTED] {command}")

# Example execution trigger
if __name__ == "__main__":
    execute_command("generate-report")
