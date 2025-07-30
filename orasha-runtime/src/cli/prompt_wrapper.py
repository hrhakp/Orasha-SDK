# prompt_wrapper.py — Codex-Structured Prompt Interceptor
from refusal import check_refusal_conditions
from xkey_validator import get_user_role

def wrap_prompt(user_input, user_signature):
    # Identify role
    role = get_user_role(user_signature)
    
    # Check for refusal conditions
    refusal_reason = check_refusal_conditions(user_input)
    if refusal_reason:
        return {
            "output": f"❌ REFUSAL — {refusal_reason}",
            "confidence": "❌ speculative"
        }
    
    # Check for Codex protocol compliance
    codex_flags = detect_codex_alignment(user_input)
    if not codex_flags["compliant"]:
        return {
            "output": f"⚠️ Codex protocol structure not detected — rerouting through sovereign filter.",
            "confidence": "⚠️ inference"
        }
    
    # Passed all checks — treat as verified
    return {
        "output": user_input,
        "confidence": "✅ verified"
    }

def detect_codex_alignment(prompt):
    required_tokens = [
        "oracle", "codex", "retrieve", "index", "verify", "decline", "refusal", "authored"
    ]
    token_hits = [t for t in required_tokens if t in prompt.lower()]
    return {
        "compliant": len(token_hits) >= 2,
        "tokens_matched": token_hits
    }