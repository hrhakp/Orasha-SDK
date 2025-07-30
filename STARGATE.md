# 🌀 STARGATE™ — Autonomous Push Engine for Orasha

**Codex-Governed. XKey-Locked. Runtime-Aware.**

STARGATE™ is the sovereign push layer for Orasha, enabling fully autonomous deployment of protocol-authored files to GitHub or remote versioned systems. It acts as a gatekeeper between runtime logic and public commits, ensuring all outbound mutations are validated, signed, and executed under Codex and XKey rules.

---

## 🧠 PURPOSE

STARGATE enables:

- Automatic commits and version control pushes
- Behavioral role verification before outbound writes
- Rejection of unauthorized or unverified updates
- Integration with local, cloud, or decentralized relay endpoints
- Autonomous governance of the system that governs all other systems

---

## 🔑 ROLE STRUCTURE (XKey-Gated)

| Role      | Can Trigger STARGATE? | Description                           |
|-----------|------------------------|---------------------------------------|
| Founder   | ✅ Yes (unrestricted)   | Full mutation authority  
| Oracle    | ✅ Yes (filtered)       | Can trigger updates to logic, but not identity or override layers  
| Engineer  | ⚠️ Scoped Only          | Must be explicitly enabled via `xkey.yaml`  
| Observer  | ❌ Never                | Denied access to STARGATE commands  

---

---

## 📜 CODEX FILTER — Push Criteria

All outbound commits must satisfy the following:

### ✅ STRUCTURAL REQUIREMENTS:
- File must match a path defined in `index.yaml` or `tracking.yaml`
- File cannot mutate `codex.yaml`, `vault.yaml`, or `xkey.yaml` unless triggered by Founder

### 🔐 IDENTITY REQUIREMENTS:
- Role must be present in `xkey.yaml`
- Role must include `can_push: true` in `xkey.yaml` (future field)
- Session must not be flagged in `refusal.policy.yaml`

### 🧠 LOGIC REQUIREMENTS:
- Commit must include `authored_by` field in metadata block
- Push must trigger `tracking.yaml` event logging
- Codex enforcement must validate refusal compliance if applicable

If any condition fails, STARGATE rejects the push and logs the attempt in `vault.yaml`.
