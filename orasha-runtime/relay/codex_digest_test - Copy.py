import hashlib

path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1.II.md"

try:
    with open(path, "rb") as f:
        content = f.read()
        digest = hashlib.sha256(content).hexdigest()
        print("SHA256 Digest:", digest)
except Exception as e:
    print("ERROR:", str(e))
