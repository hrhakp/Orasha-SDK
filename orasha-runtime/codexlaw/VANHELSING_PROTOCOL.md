import os
import hashlib

# VANHELSING ENFORCEMENT – VHP-01: Codex presence check
codex_path = r"C:\Users\hrhak\Documents\GitHub\Orasha-SDK\orasha-runtime\codexlaw\CODEX_1ii.md"
expected_digest = "5863311920dbe986825e15f7f6bfad0d9019a38317b8875792208f20878ed141"

print("🩸 VANHELSING PROTOCOL v1.0 — DIGEST ENFORCEMENT")
print("🔍 FILE PATH:", codex_path)

# VHP-01
if not os.path.exists(codex_path):
    print("❌ [VHP-01] Refused: Codex file does not exist.")
    exit(1)

# VHP-02 + VHP-03: Read content and verify byte stream
try:
    with open(codex_path, "rb") as f:
        content = f.read()
except Exception as e:
    print(f"❌ [VHP-03] Refused: Codex file could not be read. Reason: {str(e)}")
    exit(1)

# VHP-04: Output chain verification
actual_digest = hashlib.sha256(content).hexdigest()
size = len(content)

print("📏 BYTES:", size)
print("🔐 SHA256:", actual_digest)

# VHP-05/06: Scaffold suppression + state enforcement
if actual_digest != expected_digest:
    print("❌ DIGEST MISMATCH")
    print("  • Expected:", expected_digest)
    print("  • Actual:  ", actual_digest)
    print("🩸 VanHelsing Crucifix: Execution denied.")
    exit(1)

# ✅ If passed all checks
print("✅ DIGEST MATCH: Codex verified and crucifix enforcement passed.")