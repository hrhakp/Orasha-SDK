import os
import hashlib

# Exact Codex file path
path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
expected = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

print("[CODEX DIGEST TEST] Path:", path)
print("[CODEX DIGEST TEST] Exists:", os.path.exists(path))
print("[CODEX DIGEST TEST] Is File:", os.path.isfile(path))

if not os.path.isfile(path):
    print("[CODEX DIGEST TEST] ❌ File does not exist or is invalid.")
    exit(1)

try:
    with open(path, "rb") as f:
        content = f.read()
except Exception as e:
    print("[CODEX DIGEST TEST] ❌ Failed to read file:", str(e))
    exit(1)

actual = hashlib.sha256(content).hexdigest()
size = len(content)

print("[CODEX DIGEST TEST] File Size:", size, "bytes")
print("[CODEX DIGEST TEST] SHA256 Digest:", actual)

if actual == expected:
    print("[CODEX DIGEST TEST] ✅ Digest match. Codex verified.")
else:
    print("[CODEX DIGEST TEST] ❌ Digest mismatch.")
    print("Expected:", expected)
    print("Actual:  ", actual)
