import re
from .license import license_manager

# Basic masking rules (available in OSS version)
BASIC_MASKING_RULES = {
    "AWS_ACCESS_KEY_ID": r"AKIA[0-9A-Z]{16}",
    "BEARER_TOKEN": r"[Bb]earer\s+[A-Za-z0-9\-\._~\+\/]+=*",
    "PRIVATE_KEY": r"-----BEGIN ((EC|RSA|OPENSSH) )?PRIVATE KEY-----",
}

# Advanced masking rules (Pro version only)
ADVANCED_MASKING_RULES = {
    "AWS_SECRET_ACCESS_KEY": r"(?i)aws_secret_access_key\s*=\s*['\"]?[A-Za-z0-9/+=]{40}['\"]?",
    "GENERIC_API_KEY": r"(?i)api[_-]?key\s*=\s*['\"]?[A-Za-z0-9_.-]{32,45}['\"]?",
    "SLACK_TOKEN": r"xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32}",
    "GITHUB_TOKEN": r"ghp_[0-9a-zA-Z]{36}",
    # Pro version would have many more patterns
    "AZURE_KEY": r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "GCP_KEY": r"(?i)google[_-]?api[_-]?key\s*=\s*['\"]?[A-Za-z0-9_.-]{39}['\"]?",
}

MASK_REPLACEMENT = "[*** MASKED_SECRET ***]"
PRO_MASK_REPLACEMENT = "[*** MASKED_SECRET_PRO ***]"

def get_active_masking_rules():
    """Get masking rules based on license level"""
    rules = BASIC_MASKING_RULES.copy()
    
    if license_manager.check_feature('advanced_masking'):
        rules.update(ADVANCED_MASKING_RULES)
    
    return rules

# Global flag to show message only once per session
_upgrade_message_shown = False

def apply_masking(text: str, mode: str = "basic") -> str:
    """Applies masking rules to the given text based on license level."""
    global _upgrade_message_shown
    
    if mode == "off":
        return text
    
    rules = get_active_masking_rules()
    
    # Show upgrade message only once if trying to use advanced features without license
    if mode == "advanced" and not license_manager.check_feature('advanced_masking') and not _upgrade_message_shown:
        print("[INFO] Advanced masking requires dir2md Pro. Using basic masking rules.")
        print("       Visit https://dir2md.com/pro for more comprehensive security patterns.")
        _upgrade_message_shown = True
    
    for rule_name, pattern in rules.items():
        replacement = PRO_MASK_REPLACEMENT if rule_name in ADVANCED_MASKING_RULES else MASK_REPLACEMENT
        text = re.sub(pattern, replacement, text)
    
    return text