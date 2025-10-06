# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2025-10-06

### Changed
- Promote the CLI configuration defaults and optional flag handling refinements for general availability.

### Notes
- Approved performance-focused guidance for faster pro preset runs (targeted excludes, tighter budgets, and optional manifest skips).

## [1.0.2] - 2025-10-06

### Added
- **Pyproject-driven defaults**: CLI now reads `[tool.dir2md]` configuration to seed argument defaults before parsing.
- **Legacy TOML support**: Bundled `tomli` for Python 3.10 and earlier so configuration loading works across environments.

### Changed
- **Optional flag handling**: CLI leaves optional switches unset unless provided, preserving config defaults and canonical output filenames.
### Fixed
- **CLI Option Functionality**
  - Fixed `--include-glob` having no effect during report generation
  - Fixed `--follow-symlinks` flag being ignored in directory walker
  - Added proper file filtering based on include patterns while preserving directory tree structure
  - Enhanced symlink detection to respect follow_symlinks setting for both directories and files
- **Masking Mode Selection Logic**
  - Fixed issue where Pro license users received advanced masking patterns even when using `mode="basic"`
  - Updated `get_active_masking_rules()` to respect both mode parameter and license availability
  - Now `mode="basic"` consistently uses only basic patterns regardless of license tier
  - Ensures users can choose their preferred masking level independent of license capabilities
- **Enhanced Private Key Security**
  - Upgraded `PRIVATE_KEY` regex to mask entire PEM blocks instead of just headers
  - Added `re.DOTALL` flag support for complete multiline private key content masking
  - Now fully masks private key body and footer, eliminating sensitive data leakage
  - Supports all PEM formats: `PRIVATE KEY`, `RSA PRIVATE KEY`, `EC PRIVATE KEY`

### Testing
- Enhanced `test_masking` with comprehensive private key validation
- Verifies complete masking of header, body, and footer content
- Tests multiple private key formats for thorough security coverage
- All 4 test suites continue to pass with enhanced security

## [1.0.1] - 2025-09-17

### Fixed
- **Missing masking.py File**
  - Restored missing `src/dir2md/masking.py` file that was excluded by `.gitignore`
  - Resolved critical ImportError preventing core masking functionality from working
  - Removed `masking.py` entry from `.gitignore` to allow proper git tracking
- **Incomplete Private Key Masking**
  - Enhanced `PRIVATE_KEY` regex to match entire PEM blocks instead of just headers
  - Added `re.DOTALL` flag support for multiline private key content masking
  - Now completely masks private key body and footer, preventing sensitive data leakage
  - Supports all PEM formats: `PRIVATE KEY`, `RSA PRIVATE KEY`, `EC PRIVATE KEY`
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





