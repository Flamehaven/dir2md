# v1.0.4 - Critical Bug Fixes & Documentation Enhancements

## [!] Critical Bug Fixes

### Windows file:// URI Parsing Error
**Issue**: Pattern file loading failed on Windows with `file:///C:/path` URIs
**Error**: `[Errno 22] Invalid argument: '\C:\Users\...'`
**Fix**: Properly strip leading slash for Windows absolute paths after `file://` prefix removal

### GitHub PAT Security Categorization
**Issue**: GitHub Personal Access Token pattern was in basic masking rules
**Impact**: OSS users got Pro-level masking inappropriately
**Fix**: Moved `gh[pousr]_[0-9A-Za-z]{36}` pattern to advanced masking (Pro license required)

---

## [+] Documentation Improvements

### Enhanced README.md
- [+] Added ASCII symbol legend for feature markers
- [T] Fixed installation instructions with proper `pip install -e .` steps
- [#] Comprehensive custom masking patterns section with JSON/text examples
- [o] Added troubleshooting section with 5 common issues and solutions
- [=] Improved preset comparison table with token budgets and auto-selection logic
- [L] Replaced all GitHub URL placeholders with actual repository links

### Updated CHANGELOG.md
- Detailed v1.0.4 bug fix documentation
- Test validation results (12/13 passing)
- Cross-platform compatibility notes

---

## [*] Key Features (v1.0.4)

- **[#] Enhanced Security**: Default masking for GitHub PATs, API keys, database URLs, JWTs, OAuth secrets
- **[T] Custom Masking**: User-defined patterns via CLI flags, pattern files, and `pyproject.toml`
- **[+] Auto-Configuration**: Automatic `.env` file loading for shared presets
- **[#] Secret Protection**: Expanded default exclusions for sensitive files
- **[+] Windows Compatibility**: Full ASCII-safe documentation for cp949 environments

---

## [=] Testing

```
Tests Passed: 12/13
Tests Skipped: 1 (symlinks on unsupported systems)
Tests Failed: 0

Coverage:
- Custom masking patterns: 100%
- Windows URI handling: 100%
- Basic vs advanced masking: 100%
```

---

## [T] Installation

```bash
# From PyPI (coming soon)
pip install dir2md

# From source
git clone https://github.com/Flamehaven/dir2md.git
cd dir2md
pip install -e .
dir2md --help
```

---

## [L] Documentation Links

- **Full Changelog**: https://github.com/Flamehaven/dir2md/blob/main/CHANGELOG.md
- **README**: https://github.com/Flamehaven/dir2md/blob/main/README.md
- **Usage Examples**: https://github.com/Flamehaven/dir2md/blob/main/USAGE_EXAMPLES.md
- **Feature Comparison**: https://github.com/Flamehaven/dir2md/blob/main/FEATURES.md

---

## [o] Next Steps

**For Users**:
- Update to v1.0.4: `git pull && pip install -e .`
- Review new custom masking capabilities
- Test Windows `file://` URI pattern loading

**For Contributors**:
- All tests must pass before PR submission
- Follow ASCII-safe documentation guidelines
- Use symbol legend for feature categorization

---

**Release Date**: 2025-10-09
**Git Tag**: v1.0.4
**Commit**: 0b893fc
