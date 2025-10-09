import re
from typing import Iterable
from .license import license_manager

# Basic masking rules (available in OSS version)
BASIC_MASKING_RULES = {
    "AWS_ACCESS_KEY_ID": r"AKIA[0-9A-Z]{16}",
    "BEARER_TOKEN": r"[Bb]earer\s+[A-Za-z0-9\-\._~\+\/]+=*",
    "PRIVATE_KEY": r"-----BEGIN ((EC|RSA|OPENSSH) )?PRIVATE KEY-----.*?-----END ((EC|RSA|OPENSSH) )?PRIVATE KEY-----",
    "GENERIC_API_KEY": r"(?i)(api[_-]?key|x-api-key|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{20,64}['\"]?",
    "DATABASE_URL": r"(?i)(postgres|mysql|mariadb|mongodb(\+srv)?|sqlserver|redis)://[^\s]+",
    "JWT_TOKEN": r"[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}\.[A-Za-z0-9_-]{16,}",
    "OAUTH_CLIENT_SECRET": r"(?i)(client[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{8,64}['\"]?",
}

# Advanced masking rules (Pro version only)
ADVANCED_MASKING_RULES = {
    "AWS_SECRET_ACCESS_KEY": r"(?i)aws_secret_access_key\s*=\s*['\"]?[A-Za-z0-9/+=]{40}['\"]?",
    "GENERIC_API_KEY": r"(?i)api[_-]?key\s*=\s*['\"]?[A-Za-z0-9_.-]{32,45}['\"]?",
    "SLACK_TOKEN": r"xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32}",
    "GITHUB_TOKEN": r"ghp_[0-9a-zA-Z]{36}",
    "GITHUB_PAT": r"gh[pousr]_[0-9A-Za-z]{36}",
    # Pro version would have many more patterns
    "AZURE_KEY": r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "GCP_KEY": r"(?i)google[_-]?api[_-]?key\s*=\s*['\"]?[A-Za-z0-9_.-]{39}['\"]?",
}

MASK_REPLACEMENT = "[*** MASKED_SECRET ***]"
PRO_MASK_REPLACEMENT = "[*** MASKED_SECRET_PRO ***]"
CUSTOM_MASK_REPLACEMENT = "[*** MASKED_SECRET ***]"

def get_active_masking_rules(mode: str = "basic"):
    """Get masking rules based on mode and license level"""
    rules = BASIC_MASKING_RULES.copy()

    # Only add advanced rules if both mode and license allow it
    if mode == "advanced" and license_manager.check_feature('advanced_masking'):
        rules.update(ADVANCED_MASKING_RULES)

    return rules

# Global flag to show message only once per session
_upgrade_message_shown = False

def apply_masking(text: str, mode: str = "basic", custom_patterns: Iterable[str] | None = None) -> str:
    """Applies masking rules to the given text based on license level and optional custom patterns."""
    global _upgrade_message_shown
    
    if mode == "off":
        rules = {}
    else:
        rules = get_active_masking_rules(mode)
    
    # Apply custom patterns first so project-specific rules run before bundled ones.
    if custom_patterns:
        for pattern in custom_patterns:
            try:
                text = re.sub(pattern, CUSTOM_MASK_REPLACEMENT, text, flags=re.DOTALL)
            except re.error as exc:
                print(f"[WARN] Skipping invalid custom mask pattern: {pattern!r} ({exc})")

    # Show upgrade message only once if trying to use advanced features without license
    if mode == "advanced" and not license_manager.check_feature('advanced_masking') and not _upgrade_message_shown:
        print("[INFO] Advanced masking requires dir2md Pro. Using basic masking rules.")
        print("       Visit https://dir2md.com/pro for more comprehensive security patterns.")
        _upgrade_message_shown = True
    
    for rule_name, pattern in rules.items():
        replacement = PRO_MASK_REPLACEMENT if rule_name in ADVANCED_MASKING_RULES else MASK_REPLACEMENT
        # Use DOTALL flag for private keys to match across newlines
        if rule_name == "PRIVATE_KEY":
            text = re.sub(pattern, replacement, text, flags=re.DOTALL)
        else:
            text = re.sub(pattern, replacement, text)

    return text
