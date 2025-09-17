# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-09-17

### Fixed
- **Critical Import Issue** in masking module accessibility
  - Fixed `ImportError` when importing `apply_masking` from package root level
  - Added missing exports in `__init__.py` for core functions (`apply_masking`, `Config`, `generate_markdown_report`)
  - Previously masking.py existed but wasn't accessible via `from dir2md import apply_masking`
- **Markdown Code Block Formatting**
  - Fixed incorrect fence pairing where directory tree and file content blocks used `````(4 backticks) to close instead of ```` (3 backticks)
  - Ensures proper Markdown rendering in generated reports
- **CLI Exclude Pattern Logic**
  - Fixed issue where custom `--exclude-glob` patterns completely replaced default exclusions
  - Now custom patterns are added to defaults (`.git`, `__pycache__`, `node_modules`, etc.) instead of overriding them
- **Stats Flag Control**
  - Fixed `--stats` flag that was always evaluating to `True` due to `bool(ns.stats or True)` logic
  - Now `--stats` flag properly controls whether Summary section is included in output

### Improved
- Enhanced package-level API accessibility for library usage
- Better default behavior preservation when using custom CLI options
- Improved Markdown output formatting consistency

### Testing
- All 4 test cases continue to pass: `test_budget_and_modes`, `test_ref_mode_manifest`, `test_inline_sampling`, `test_masking`
- Verified masking functionality works correctly (e.g., `Bearer token` → `[*** MASKED_SECRET ***]`)
- CLI functionality preserved across all modes and options

### Technical Details
- Package now properly exports core functions in `__init__.py`
- Masking module with AWS key, Bearer token, and private key detection fully operational
- License-based feature gating implemented for basic vs advanced masking
- Markdown fence consistency ensures proper code syntax highlighting

## [0.0.1] - Initial Release
- Core directory scanning and Markdown generation
- Token budget optimization with LLM modes (off, ref, summary, inline)
- Basic masking capabilities for sensitive data
- Gitignore integration and file filtering
- Manifest generation and statistics reporting