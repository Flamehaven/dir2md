from __future__ import annotations
import json, tempfile
from pathlib import Path
from dir2md.core import Config, generate_markdown_report


def _make_repo(tmp: Path) -> Path:
    (tmp/"src").mkdir(parents=True, exist_ok=True)
    # Make this file long enough to trigger truncation
    long_content = "\n".join([f"    print('line {i}')" for i in range(100)])
    (tmp/"src"/"a.py").write_text(f"""
import os

class A: pass

def foo():
{long_content}
    return 42
""", encoding="utf-8")
    (tmp/"src"/"b.py").write_text("""
import sys

def bar():
    return 43
""", encoding="utf-8")
    # Similar file (for deduplication testing)
    (tmp/"src"/"b_copy.py").write_text((tmp/"src"/"b.py").read_text(encoding="utf-8"), encoding="utf-8")
    (tmp/"README.md").write_text("# Title\n\nSome text\n", encoding="utf-8")
    return tmp


def test_budget_and_modes(tmp_path: Path):
    root = _make_repo(tmp_path)
    cfg = Config(
        root=root, output=root/"OUT.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=False, follow_symlinks=False, max_bytes=200_000, max_lines=2000,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode="summary", budget_tokens=200, max_file_tokens=1200, dedup_bits=16,
        sample_head=120, sample_tail=40, strip_comments=False, emit_manifest=True,
        preset="pro", explain_capsule=True,
    )
    md = generate_markdown_report(cfg)
    assert "Estimated tokens (prompt):" in md
    mpath = (root/"OUT.manifest.json")
    assert mpath.exists()
    man = json.loads(mpath.read_text(encoding="utf-8"))
    # b_copy.py likely to be excluded due to deduplication
    paths = {entry["path"] for entry in man["files"]}
    assert any(p.endswith("a.py") for p in paths)
    assert any(p.endswith("b.py") for p in paths)


def test_ref_mode_manifest(tmp_path: Path):
    root = _make_repo(tmp_path)
    cfg = Config(
        root=root, output=root/"OUT.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=False, follow_symlinks=False, max_bytes=200_000, max_lines=2000,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode="ref", budget_tokens=120, max_file_tokens=1200, dedup_bits=16,
        sample_head=120, sample_tail=40, strip_comments=False, emit_manifest=True,
        preset="pro", explain_capsule=False,
    )
    md = generate_markdown_report(cfg)
    man = json.loads((root/"OUT.manifest.json").read_text(encoding="utf-8"))
    assert "stats" in man
    assert "files" in man
    assert all("sha256" in e for e in man["files"])


def test_inline_sampling(tmp_path: Path):
    root = _make_repo(tmp_path)
    # Drastically reduced budget to trigger sampling
    cfg = Config(
        root=root, output=root/"OUT.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=False, follow_symlinks=False, max_bytes=200_000, max_lines=50,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode="inline", budget_tokens=50, max_file_tokens=30, dedup_bits=0,
        sample_head=5, sample_tail=3, strip_comments=False, emit_manifest=False,
        preset="pro", explain_capsule=True,
    )
    md = generate_markdown_report(cfg)
    assert "truncated middle" in md
    assert "why: inline" in md

def test_masking(tmp_path: Path):
    root = _make_repo(tmp_path)
    # Add a file with a secret
    secret_content = "My AWS key is AKIAIOSFODNN7EXAMPLE"
    (root / ".env").write_text(secret_content, encoding="utf-8")

    # Add a file with a private key
    private_key_content = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7VJTUt9Us8cKB
UmV1F2Cu5CX2jUcZdVRrVNjm/4Sk8DohVhQj4JY=
-----END PRIVATE KEY-----"""
    (root / "private_key.pem").write_text(private_key_content, encoding="utf-8")

    cfg = Config(
        root=root, output=root/"OUT.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=False, follow_symlinks=False, max_bytes=200_000, max_lines=2000,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode="inline", budget_tokens=1000, max_file_tokens=1000, dedup_bits=0,
        sample_head=120, sample_tail=40, strip_comments=False, emit_manifest=False,
        preset="pro", explain_capsule=False, no_timestamp=True,
        masking_mode="basic",
    )
    md = generate_markdown_report(cfg)

    # Check AWS key masking
    assert secret_content not in md
    assert "[*** MASKED_SECRET ***]" in md

    # Check private key masking - entire block should be masked
    assert private_key_content not in md
    assert "-----BEGIN PRIVATE KEY-----" not in md
    assert "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7VJTUt9Us8cKB" not in md
    assert "-----END PRIVATE KEY-----" not in md

    # Test with masking off
    cfg.masking_mode = "off"
    md_unmasked = generate_markdown_report(cfg)
    assert secret_content in md_unmasked
    assert private_key_content in md_unmasked
    assert "[*** MASKED_SECRET ***]" not in md_unmasked


def test_masking_pro_license_mode_respect(tmp_path: Path, monkeypatch):
    """Test that masking respects basic vs advanced mode even with Pro license"""
    from dir2md.masking import apply_masking

    # Mock Pro license to be available
    def mock_check_feature(feature_name):
        return feature_name == 'advanced_masking'

    monkeypatch.setattr('dir2md.masking.license_manager.check_feature', mock_check_feature)

    # Test content with both basic and advanced patterns
    github_token = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123"  # Advanced pattern
    aws_key = "AKIAIOSFODNN7EXAMPLE"  # Basic pattern
    test_content = f"GitHub token: {github_token}\nAWS key: {aws_key}"

    # Test basic mode - should only mask basic patterns even with Pro license
    basic_masked = apply_masking(test_content, mode="basic")
    assert aws_key not in basic_masked  # AWS key should be masked (basic pattern)
    assert github_token in basic_masked  # GitHub token should NOT be masked in basic mode
    assert "[*** MASKED_SECRET ***]" in basic_masked

    # Test advanced mode - should mask both basic and advanced patterns
    advanced_masked = apply_masking(test_content, mode="advanced")
    assert aws_key not in advanced_masked  # AWS key should be masked
    assert github_token not in advanced_masked  # GitHub token should be masked in advanced mode
    assert "[*** MASKED_SECRET ***]" in advanced_masked
    assert "[*** MASKED_SECRET_PRO ***]" in advanced_masked

    # Test off mode - should mask nothing
    off_masked = apply_masking(test_content, mode="off")
    assert aws_key in off_masked
    assert github_token in off_masked
    assert "[*** MASKED_SECRET ***]" not in off_masked
