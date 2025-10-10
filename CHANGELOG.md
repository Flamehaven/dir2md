# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2025-10-09

### Added

#### Enhanced Security Masking
- Expanded default masking coverage to include GitHub personal access tokens, generic API keys, database URLs, JWTs, and OAuth client secrets in the open source build
- New patterns detected:
  - GitHub Personal Access Tokens: `ghp_*`, `gho_*`, `ghu_*`, `ghs_*`, `ghr_*`
  - Generic API Keys: `api_key=`, `apikey=`, `api-key=`
  - Database URLs: PostgreSQL, MySQL, MongoDB connection strings
  - JSON Web Tokens (JWTs): `eyJ*` base64-encoded tokens
  - OAuth Client Secrets: `client_secret=`, `oauth_secret=`

#### Automatic Environment Configuration
- Automatically load the nearest `.env` file when launching the CLI so license keys and shared defaults are available without manual exports
- Zero-configuration startup for teams using `.env` files
- Seamless Pro license activation

#### User-Defined Masking Patterns
- Support user-defined masking patterns via `--mask-pattern` flags, `--mask-pattern-file` for loading from files, and `[tool.dir2md.masking]` configuration in `pyproject.toml`
- Three flexible methods:
  1. Inline patterns: `--mask-pattern "regex"`
  2. Pattern files: JSON arrays or newline-delimited text via `file://` URIs
  3. Configuration: `[tool.dir2md.masking]` section in `pyproject.toml`

### Changed

#### Expanded Default Exclusions
- Extended the default exclusion set to skip common secret-bearing files such as `.env*`, certificate bundles, and private key formats before scanning directories
- New exclusions: `.env`, `.env.local`, `.env.*.local`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.crt`, `*.cer`, `*.der`

#### Windows Compatibility Improvements
- Sanitized the public documentation to use ASCII-only characters for Windows cp949 compatibility
- ASCII-safe replacements: `[#]`, `[!]`, `[+]`, `[*]`, `[T]` instead of emojis
- Prevents `illegal multibyte sequence` errors on Windows systems

#### Documentation Clarity
- Clarified relationship with IsaacBreen's `dir2md` (PyPI package)
- Added **Acknowledgments** section for community transparency
- Updated installation instructions to reflect GitHub-only distribution
- Removed "coming soon" language for PyPI availability

### Fixed

#### [CRITICAL] Windows file:// URI Parsing Error
- **Issue:** Windows `file://` URI handling for pattern files failed with `"Invalid argument: '\C:...'"` error due to incorrect path slicing
- **Root cause:** Path parsing didn't account for Windows absolute paths (`C:\...`)
- **Solution:** Properly strips leading slash for Windows absolute paths (`file:///C:/path` → `C:/path`)
- **Impact:** Custom masking pattern files now work correctly on Windows systems

#### [SECURITY] GitHub PAT Pattern Misplacement
- **Issue:** GitHub Personal Access Token pattern (`gh[pousr]_[0-9A-Za-z]{36}`) was incorrectly placed in basic masking rules instead of advanced (Pro-only)
- **Risk:** Open-source users received Pro-level pattern matching without license validation
- **Solution:** Moved GitHub PAT pattern to advanced masking rules, enforcing proper Pro license requirement
- **Impact:** Correct separation between OSS basic and Pro advanced masking tiers

#### Advanced Masking Notice Deduplication
- Ensure the advanced masking upgrade notice prints only once per session when advanced mode is requested without an active Pro license
- **Before:** Multiple notices during single CLI run
- **After:** Single notice at first invocation

### Testing

#### Automated Tests
- 12 tests passing (1 skipped for symlinks on systems without support)
- Full `pytest` suite coverage for core functionality
- Regression tests for Windows `file://` URI paths

#### Manual Verification
- Custom masking patterns load correctly from JSON files
- Custom masking patterns load correctly from text files
- Windows `file://` URI paths resolve properly (`file:///C:/...`)
- Basic vs advanced masking mode separation enforced
- `.env` auto-discovery works across different directory structures
- ASCII-safe documentation renders correctly on Windows cp949 systems

## [1.0.3] - 2025-10-06

### Changed
- Promote the CLI configuration defaults and optional flag handling refinements for general availability.
- Add repository-level import helpers so local runs and pytest sessions automatically discover the `src` layout without editable installs.

### Fixed
- Restore gitwildmatch semantics for recursive globs by preventing `**/` patterns from matching root-level files.

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
- Verified masking functionality works correctly (e.g., `Bearer token` -> `[*** MASKED_SECRET ***]`)
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





