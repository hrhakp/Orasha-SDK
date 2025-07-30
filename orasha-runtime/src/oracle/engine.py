from .refusal import is_user_authorized

# Simulate runtime context — this would normally come from CLI
cli_caller_role = "external_request"  # Change to test enforcement

def execute_command(command: str):
    if not is_user_authorized(cli_caller_role):
        raise PermissionError("Execution blocked: unauthorized role.")

    print(f"[EXECUTED] {command}")

# Example placeholder usage
if __name__ == "__main__":
    execute_command("generate-report")
