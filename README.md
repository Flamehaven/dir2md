---
license: mit
language:
- en
- ko
tags:
- python
- cli
- markdown
- llm
- developer-tools
- code-analysis
- open-core
title: dir2md Demo
emoji: ""
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.19.2
app_file: demo/app.py
pinned: false
---
# Dir2md

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

> Transform your codebase into LLM-optimized markdown blueprints.

Dir2md analyzes directory structures and generates comprehensive markdown documentation optimized for large language models. It intelligently samples content, removes duplicates, and provides token-budget control to create the perfect context for AI-assisted development.

**Legend**: [*] Core Feature | [#] Security | [!] Performance | [T] Configuration | [+] User Experience

## 1.0.4 Highlights

- **[#] Enhanced Security**: Default masking for GitHub PATs, API keys, database URLs, JWTs, and OAuth secrets
- **[T] Custom Masking**: User-defined patterns via `--mask-pattern` / `--mask-pattern-file` flags and `pyproject.toml` configuration
- **[+] Auto-Configuration**: CLI now loads nearest `.env` file automatically for shared presets and license keys
- **[#] Secret Protection**: Expanded default exclusions for `.env*`, certificates, and private key files
- **[+] Windows Compatibility**: ASCII-safe documentation for cp949 encoding environments
- **[!] Critical Fixes**: Windows `file://` URI parsing and GitHub PAT security categorization

## Key Features

- **[*] Smart Content Sampling**: Head/tail sampling with configurable token budgets.
- **[*] Duplicate Detection**: SimHash-based deduplication to reduce noise.
- **[#] Security First**: Enhanced secret masking for PEM blocks, AWS keys, bearer tokens, GitHub PATs, generic API keys, database URLs, JWTs, and OAuth secrets (advanced patterns in Pro).
- **[#] Custom Masking**: Add project-specific regular expressions via CLI flags, pattern files, or `pyproject.toml`.
- **[!] Multiple Output Modes**: Reference, summary, or full inline content.
- **[T] Highly Configurable**: Extensive filtering and customization options.
- **[+] Developer Friendly**: Raw mode default for complete code visibility.

## Why Dir2md?

Traditional documentation approaches fall short when working with AI assistants:

- Too much noise: raw `tree` plus `cat` includes irrelevant files.
- Token waste: unoptimized content hits LLM context limits.
- Security risks: accidental exposure of secrets and keys.

## Quick Start

### Try It Online

**[Try dir2md Demo on Hugging Face Spaces](https://huggingface.co/spaces/Flamehaven/dir2md-demo)**

Experience dir2md instantly in your browser:
- Convert any GitHub repository to markdown.
- See real-time directory structure analysis.
- Download generated markdown blueprints.
- No installation required.

### Installation

```bash
# From PyPI (recommended - coming soon)
pip install dir2md

# From source (current method)
git clone https://github.com/Flamehaven/dir2md.git
cd dir2md
pip install -e .  # Install in editable/development mode
dir2md --help     # CLI now available globally

# Or run directly without installation
python -m src.dir2md.cli --help
```

### Basic Usage

```bash
# Generate project blueprint (developer-friendly raw mode)
dir2md .

# With enhanced security masking (private keys, AWS keys, tokens)
dir2md . --masking basic

# Generate with manifest for CI/CD
dir2md . --emit-manifest --no-timestamp

# Token-optimized for LLM context
dir2md . --budget-tokens 4000 --preset iceberg
```

#### pyproject.toml defaults

Dir2md reads `[tool.dir2md]` from the nearest `pyproject.toml` so teams can share default presets, budgets, filters, and masking rules.

```toml
[tool.dir2md]
preset = "iceberg"
include_glob = ["src/**/*.py", "tests/**/*.py"]
exclude_glob = ["**/__pycache__/**"]
emit_manifest = true

[tool.dir2md.masking]
patterns = ["(?i)secret_key\\s*=\\s*['\\\"]?[A-Za-z0-9]{16,}['\\\"]?"]
pattern_files = ["file://./.dir2md/patterns.txt"]
```

Patterns use gitignore-style `gitwildmatch` semantics. Command-line flags still override any value loaded from the configuration file.

### Custom Masking Patterns

Dir2md supports project-specific secret patterns through multiple methods:

**Inline patterns** (repeatable flag):
```bash
dir2md . --mask-pattern "(?i)stripe_key\\s*=\\s*['\"]?sk_live_\\w+['\"]?"
```

**Pattern files** (JSON or text format):
```bash
# patterns.json (JSON array format)
["(?i)custom_token:\\s*[A-Za-z0-9_-]{32,}",
 "(?i)internal_key=\\S+"]

# patterns.txt (newline-delimited format)
(?i)stripe_key\s*=\s*['\"]?sk_live_\w+['\"]?
(?i)mailgun_api_key\s*=\s*['\"]?key-[a-z0-9]{32}['\"]?

# Load with file:// URI
dir2md . --mask-pattern-file file://./patterns.json
```

**Configuration file** (`pyproject.toml`):
```toml
[tool.dir2md.masking]
patterns = ["(?i)secret_key\\s*=\\s*[A-Za-z0-9]{16,}"]
pattern_files = ["file://./.dir2md/patterns.txt"]
```

**Key Features**:
- Custom rules run **before** built-in masking (project overrides win)
- Invalid regexes are skipped with warnings (other rules continue)
- Supports JSON arrays, JSON objects with `patterns` key, or newline-delimited text
- Cross-platform `file://` URI support (Windows: `file:///C:/path`, Unix: `file:///path`)

### Output Example

```markdown
# Project Blueprint

- Root: `/path/to/project`
- Generated: `2025-09-08 12:30:15`
- Preset: `raw`
- LLM mode: `inline`
- Estimated tokens (prompt): `6247`

## Directory Tree
[Complete file structure]

## Statistics
| Metric | Value |
|--------|-------|
| Total files | 42 |
| Estimated tokens | 6247 |

## File Contents
[Intelligently sampled content...]
```

## Available Presets

| Preset | Token Budget | LLM Mode | Dedup | Best For |
|--------|--------------|----------|-------|----------|
| `raw` | Unlimited | inline | Off | Development, full code review |
| `iceberg` | 6000 (auto-adjust) | Auto-select* | 16-bit | General documentation, CI/CD |
| `pro` | User-defined | User-defined | Custom | Large projects, fine-tuned control |

*`iceberg` mode auto-selects: `inline` (<200KB), `summary` (200KB-5MB), `ref` (>5MB)

## Limitations (Current OSS Build)
- The `raw` preset always forces `--emit-manifest` off; select `iceberg` or `pro` when you need manifest output.
- PyPI package is not yet published; install from source (`pip install .`) until the 1.0.4 release is finalized.
- README references Pro-only capabilities (advanced masking, parallel processing, export formats) that are not implemented in this repository.

## Open-Core Model

### Free (OSS) Features
- Complete directory analysis.
- Token optimization and sampling.
- SimHash deduplication.
- Enhanced security masking (AWS access keys, bearer tokens, private keys, GitHub PATs, generic API keys, database URLs, JWTs, OAuth secrets).
- All output modes and presets.
- Deterministic builds.

### Pro Features
- Advanced security masking (additional cloud and SaaS patterns).
- Parallel processing and caching.
- Language-specific analysis plugins.
- HTML/PDF export options.
- Team integration (CI/CD, PR bots).
- Priority support.
- Pricing and licensing: Individual $29/month or $290/year; Team (5 users) $99/month or $990/year; Enterprise plans available with custom commercial terms (see `FEATURES.md` for full details).

[Learn more about Pro features](FEATURES.md)

## Documentation

- **[Feature Comparison](FEATURES.md)** - Complete OSS vs Pro breakdown.
- **[Current Status](CURRENT_FEATURES.md)** - What's implemented now.
- **[Usage Examples](USAGE_EXAMPLES.md)** - Hands-on guide with examples.

## CLI Reference

```bash
# Basic options
dir2md [path] -o output.md --preset [iceberg|pro|raw]

# Token control
--budget-tokens 6000          # Total token budget
--max-file-tokens 1200        # Per-file token limit
--sample-head 120             # Lines from the file start
--sample-tail 40              # Lines from the file end

# Filtering
--include-glob "*.py"         # Gitignore-style include (gitwildmatch)
--exclude-glob "**/__pycache__/**"  # Gitignore-style exclude
--omit-glob "tests/**"        # Omit content but keep tree
--only-ext "py,js,ts"         # File extensions only

# Security
--masking [off|basic|advanced]         # Secret masking level (advanced requires Pro)
--mask-pattern "api_key\\s*=\\s*['\\\"]?[A-Za-z0-9]+['\\\"]?"  # Repeatable custom regex
--mask-pattern-file file://./patterns.json  # Load regex patterns (JSON array or newline list)

# Output
--emit-manifest              # Generate JSON metadata
--no-timestamp              # Reproducible output
--dry-run                   # Preview without writing
```

Note: the `raw` preset always forces `--emit-manifest` off. Use the `pro` preset with manual flags if you need inline output plus a manifest.

## Contributing

We welcome contributions! Dir2md follows an open-core model:

- Core functionality: open source (this repo).
- Advanced features: commercial (separate repo).
- Community: all discussions welcome.

### Development Setup

```bash
git clone https://github.com/Flamehaven/dir2md.git
cd dir2md
pip install -e ".[dev]"  # Install with dev dependencies
python -m pytest -v      # Run tests (12 tests should pass, 1 may skip)
python -m src.dir2md.cli . --dry-run  # Test CLI
```

### Reporting Issues

- Bug reports: [GitHub Issues](https://github.com/Flamehaven/dir2md/issues)
- Feature requests: [GitHub Discussions](https://github.com/Flamehaven/dir2md/discussions)
- Security issues: info@flamehaven.space

## Troubleshooting

### Common Issues

**Pattern file not loading (Windows)**
```bash
# Error: [WARN] Could not read mask pattern file
# Fix: Use proper file:// URI format
dir2md . --mask-pattern-file file:///C:/path/to/patterns.json  # Note the triple slash
```

**File encoding errors**
```bash
# Error: UnicodeDecodeError or cp949 codec errors
# Fix: Ensure files are UTF-8 encoded, or exclude problematic files
dir2md . --exclude-glob "**/*.bin" --exclude-glob "**/*.dat"
```

**Token budget exceeded**
```bash
# Symptom: Output is truncated or incomplete
# Fix: Increase budget or use more aggressive filtering
dir2md . --budget-tokens 10000 --only-ext "py,js,md"
```

**Manifest not generated**
```bash
# Symptom: .manifest.json file missing
# Cause: raw preset disables manifests by default
# Fix: Use iceberg/pro preset or explicitly enable
dir2md . --preset pro --emit-manifest
```

**Secrets still visible in output**
```bash
# Symptom: API keys or tokens not masked
# Fix: Verify masking mode is enabled and pattern matches
dir2md . --masking basic --dry-run  # Test first
# Add custom pattern if needed
dir2md . --masking basic --mask-pattern "your_custom_pattern"
```

### Getting Help

For additional support:
- Check [Usage Examples](USAGE_EXAMPLES.md) for detailed scenarios
- Review [Feature Documentation](FEATURES.md) for capability reference
- Search [GitHub Issues](https://github.com/Flamehaven/dir2md/issues) for similar problems
- Join discussions in [GitHub Discussions](https://github.com/Flamehaven/dir2md/discussions)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Pro features are available under a separate commercial license.

---

Made with care for developers who want their AI to understand their code.
