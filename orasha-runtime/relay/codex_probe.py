import os
import hashlib

# 👇 Update this if your file is in a different path or named differently
path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
expected = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

print("🔍 PATH:", path)
print("📁 EXISTS:", os.path.exists(path))
print("📄 IS FILE:", os.path.isfile(path))

if not os.path.isfile(path):
    print("❌ ERROR: FILE NOT FOUND OR INVALID.")
    exit(1)

try:
    with open(path, "rb") as f:
        content = f.read()
except Exception as e:
    print("❌ ERROR: Could not read file. Reason:", str(e))
    exit(1)

actual = hashlib.sha256(content).hexdigest()
size = len(content)

print("\n📦 DIGEST CHECK")
print(" • Size (bytes):", size)
print(" • Computed Digest:", actual)

if actual == expected:
    print("✅ DIGEST MATCH: CODEX VERIFIED.")
else:
    print("❌ DIGEST MISMATCH.")
    print(" • Expected:", expected)
    print(" • Actual:  ", actual)