import datetime
import json

def log_push_event(payload):
    """
    Logs incoming GitHub push events with timestamp and minimal metadata.
    Intended for runtime signature verification and event auditing.
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    event_log = {
        "timestamp": timestamp,
        "repo": payload.get("repository", {}).get("full_name"),
        "pusher": payload.get("pusher", {}).get("name"),
        "commits": len(payload.get("commits", []))
    }
    with open("relay_push_log.json", "a") as log_file:
        log_file.write(json.dumps(event_log) + "\n")

# Example placeholder usage
if __name__ == "__main__":
    sample_payload = {
        "repository": {"full_name": "orasha/orasha-sdk"},
        "pusher": {"name": "hrhakp"},
        "commits": [{"id": 1}, {"id": 2}]
    }
    log_push_event(sample_payload)
