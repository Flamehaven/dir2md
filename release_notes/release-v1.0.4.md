# Release v1.0.4

## Overview

Dir2md v1.0.4 brings significant security enhancements, improved configuration management, and critical bug fixes. This release expands the default masking coverage, introduces user-defined pattern support, and resolves Windows-specific path handling issues.

**[#] Security** | **[T] Configuration** | **[!] Critical Fixes** | **[+] Documentation**

---

## Added

### Enhanced Security Masking
Expand default masking coverage to include GitHub personal access tokens, generic API keys, database URLs, JWTs, and OAuth client secrets in the open source build.

**New patterns detected:**
- GitHub Personal Access Tokens: `ghp_*`, `gho_*`, `ghu_*`, `ghs_*`, `ghr_*`
- Generic API Keys: `api_key=`, `apikey=`, `api-key=`
- Database URLs: PostgreSQL, MySQL, MongoDB connection strings
- JSON Web Tokens (JWTs): `eyJ*` base64-encoded tokens
- OAuth Client Secrets: `client_secret=`, `oauth_secret=`

### Automatic Environment Configuration
Automatically load the nearest `.env` file when launching the CLI so license keys and shared defaults are available without manual exports.

**Benefits:**
- Zero-configuration startup for teams using `.env` files
- Seamless Pro license activation
- Shared preset defaults across development environments

### User-Defined Masking Patterns
Support user-defined masking patterns via `--mask-pattern` flags, `--mask-pattern-file` for loading from files, and `[tool.dir2md.masking]` configuration in `pyproject.toml`.

**Three flexible methods:**
1. **Inline patterns:** `--mask-pattern "(?i)stripe_key\\s*=\\s*['\"]?sk_live_\\w+['\"]?"`
2. **Pattern files:** JSON arrays or newline-delimited text via `file://` URIs
3. **Configuration:** `[tool.dir2md.masking]` section in `pyproject.toml`

---

## Changed

### Expanded Default Exclusions
Extend the default exclusion set to skip common secret-bearing files such as `.env*`, certificate bundles, and private key formats before scanning directories.

**New exclusions:**
- `.env`, `.env.local`, `.env.*.local`
- `*.pem`, `*.key`, `*.p12`, `*.pfx`
- `*.crt`, `*.cer`, `*.der`

### Windows Compatibility Improvements
Sanitized the public documentation to use ASCII-only characters for Windows cp949 compatibility.

**ASCII-safe replacements:**
- Visual markers: `[#]`, `[!]`, `[+]`, `[*]`, `[T]` instead of emojis
- Prevents `illegal multibyte sequence` errors on Windows systems

### Documentation Clarity
- Clarified relationship with IsaacBreen's `dir2md` (PyPI package)
- Added **Acknowledgments** section for community transparency
- Updated installation instructions to reflect GitHub-only distribution
- Removed "coming soon" language for PyPI availability

---

## Fixed

### [CRITICAL] Windows file:// URI Parsing Error
**Issue:** Windows `file://` URI handling for pattern files failed with `"Invalid argument: '\C:...'"` error due to incorrect path slicing.

**Root cause:** Path parsing didn't account for Windows absolute paths (`C:\...`)

**Solution:** Properly strips leading slash for Windows absolute paths (`file:///C:/path` → `C:/path`)

**Impact:** Custom masking pattern files now work correctly on Windows systems.

### [SECURITY] GitHub PAT Pattern Misplacement
**Issue:** GitHub Personal Access Token pattern (`gh[pousr]_[0-9A-Za-z]{36}`) was incorrectly placed in basic masking rules instead of advanced (Pro-only).

**Risk:** Open-source users received Pro-level pattern matching without license validation.

**Solution:** Moved GitHub PAT pattern to advanced masking rules, enforcing proper Pro license requirement.

**Impact:** Correct separation between OSS basic and Pro advanced masking tiers.

### Advanced Masking Notice Deduplication
Ensure the advanced masking upgrade notice prints only once per session when advanced mode is requested without an active Pro license.

**Before:** Multiple notices during single CLI run
**After:** Single notice at first invocation

---

## Testing

### Automated Tests
- **12 tests passing** (1 skipped for symlinks on systems without support)
- Full `pytest` suite coverage for core functionality
- Regression tests for Windows `file://` URI paths

### Manual Verification
- [+] Custom masking patterns load correctly from JSON files
- [+] Custom masking patterns load correctly from text files
- [+] Windows `file://` URI paths resolve properly (`file:///C:/...`)
- [+] Basic vs advanced masking mode separation enforced
- [+] `.env` auto-discovery works across different directory structures
- [+] ASCII-safe documentation renders correctly on Windows cp949 systems

---

## Installation

### From Source (Recommended)
```bash
git clone https://github.com/Flamehaven/dir2md.git
cd dir2md
pip install -e .
dir2md --help
```

### From PyPI (IsaacBreen's Version)
Note: The PyPI `dir2md` package is maintained separately by IsaacBreen with different features. For LLM-optimized features, token budgeting, and advanced security masking, use Flamehaven's GitHub version.

```bash
pip install dir2md  # IsaacBreen's stable version
```

---

## Breaking Changes

**None.** This release maintains full backward compatibility with v1.0.3.

---

## Contributors

- **Flamehaven Team** - Core development and release management
- **IsaacBreen** - Inspiration from original `dir2md` concept (separate PyPI package)

---

## Upgrade Notes

### For Existing Users
1. Pull latest changes: `git pull origin main`
2. Reinstall package: `pip install -e .`
3. Verify version: `dir2md --version` (should show `1.0.4`)

### For New Users
Follow the **Installation** section above.

### Pro License Users
- `.env` auto-discovery now loads `DIR2MD_LICENSE` automatically
- No manual `export` commands required
- Advanced masking patterns now correctly enforce Pro license validation

---

## Known Limitations

- The `raw` preset always forces `--emit-manifest` off; use `iceberg` or `pro` presets when manifest output is needed
- This enhanced version is distributed via GitHub only; PyPI `dir2md` is a separate project by IsaacBreen
- README references Pro-only capabilities (advanced masking, parallel processing, export formats) not implemented in OSS build

---

## Resources

- **GitHub Repository:** https://github.com/Flamehaven/dir2md
- **Documentation:** [README.md](https://github.com/Flamehaven/dir2md#readme)
- **Feature Comparison:** [FEATURES.md](https://github.com/Flamehaven/dir2md/blob/main/FEATURES.md)
- **Usage Examples:** [USAGE_EXAMPLES.md](https://github.com/Flamehaven/dir2md/blob/main/USAGE_EXAMPLES.md)
- **Issue Tracker:** https://github.com/Flamehaven/dir2md/issues
- **Discussions:** https://github.com/Flamehaven/dir2md/discussions

---

## Next Release Preview (v1.1.0)

Planned features for the next release:
- Parallel directory scanning for large codebases
- Language-specific analysis plugins (Python, JavaScript, TypeScript)
- HTML/PDF export formats (Pro)
- Enhanced CI/CD integration with PR bots (Pro)
- Performance benchmarks and optimization

Stay tuned for updates!
