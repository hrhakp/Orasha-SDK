from refusal import is_user_authorized

# Simulated relay event
relay_caller_role = "oracle"  # Valid roles: founder, oracle, external_request

def guard_relay():
    if not is_user_authorized(relay_caller_role):
        raise PermissionError("Relay blocked: unauthorized caller")
    print("[RELAY AUTHORIZED] Relay action executed.")

# Placeholder execution
if __name__ == "__main__":
    guard_relay()
