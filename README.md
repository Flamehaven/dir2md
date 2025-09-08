# Dir2md

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

> Transform your codebase into LLM-optimized markdown blueprints

Dir2md analyzes directory structures and generates comprehensive markdown documentation optimized for Large Language Models. It intelligently samples content, removes duplicates, and provides token-budget control to create the perfect context for AI-assisted development.

## ✨ Key Features

- **🎯 Smart Content Sampling**: Head/tail sampling with configurable token budgets
- **🔄 Duplicate Detection**: SimHash-based deduplication to reduce noise
- **🛡️ Security First**: Built-in secret masking (basic OSS, advanced Pro)
- **📊 Multiple Output Modes**: Reference, summary, or full inline content
- **🔧 Highly Configurable**: Extensive filtering and customization options
- **⚡ Developer Friendly**: Raw mode default for complete code visibility

## 🚀 Quick Start

### Installation

```bash
# From source (current)
git clone https://github.com/your-org/dir2md.git
cd dir2md
python -m src.dir2md.cli --help

# Coming soon: PyPI installation
pip install dir2md
```

### Basic Usage

```bash
# Generate project blueprint (developer-friendly raw mode)
dir2md .

# With basic security masking
dir2md . --masking basic

# Generate with manifest for CI/CD
dir2md . --emit-manifest --no-timestamp

# Token-optimized for LLM context
dir2md . --budget-tokens 4000 --preset iceberg
```

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

## 📋 Available Presets

| Preset | Description | Best For |
|--------|-------------|-----------|
| `raw` | Full content inclusion | Development, code review |
| `iceberg` | Balanced sampling | General documentation |
| `pro` | Advanced optimization | Large projects, LLM context |

## 🔒 Open-Core Model

### Free (OSS) Features
- Complete directory analysis
- Token optimization and sampling
- SimHash deduplication
- Basic security masking (3 patterns)
- All output modes and presets
- Deterministic builds

### Pro Features
- Advanced security masking (9+ patterns)
- Parallel processing & caching
- Language-specific analysis plugins
- HTML/PDF export options
- Team integration (CI/CD, PR bots)
- Priority support

[Learn more about Pro features](FEATURES.md)

## 📖 Documentation

- **[Feature Comparison](FEATURES.md)** - Complete OSS vs Pro breakdown
- **[Current Status](CURRENT_FEATURES.md)** - What's implemented now
- **[Usage Examples](USAGE_EXAMPLES.md)** - Hands-on guide with examples

## 🛠️ CLI Reference

```bash
# Basic options
dir2md [path] -o output.md --preset [iceberg|pro|raw]

# Token control
--budget-tokens 6000          # Total token budget
--max-file-tokens 1200        # Per-file token limit
--sample-head 120             # Lines from file start
--sample-tail 40              # Lines from file end

# Filtering
--include-glob "*.py,*.md"    # Include patterns
--exclude-glob "test*,*.tmp"  # Exclude patterns
--only-ext "py,js,ts"         # File extensions only

# Security
--masking [off|basic|advanced] # Secret masking level

# Output
--emit-manifest              # Generate JSON metadata
--no-timestamp              # Reproducible output
--dry-run                   # Preview without writing
```

## 🤝 Contributing

We welcome contributions! Dir2md follows an open-core model:

- **Core functionality**: Open source (this repo)
- **Advanced features**: Commercial (separate repo)
- **Community**: All discussions welcome

### Development Setup

```bash
git clone https://github.com/your-org/dir2md.git
cd dir2md
python -m pytest -v  # Run tests
python -m src.dir2md.cli . --dry-run  # Test CLI
```

### Reporting Issues

- 🐛 **Bug reports**: [GitHub Issues](https://github.com/your-org/dir2md/issues)
- 💡 **Feature requests**: [GitHub Discussions](https://github.com/your-org/dir2md/discussions)
- 📧 **Security issues**: info@flamehaven.space

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Pro features are available under a separate commercial license.

## 🌟 Why Dir2md?

Traditional documentation approaches fall short when working with AI assistants:

- **Too much noise**: Raw `tree` + `cat` includes irrelevant files
- **Token waste**: Unoptimized content hits LLM context limits  
- **Security risks**: Accidental exposure of secrets and keys
- **No structure**: Difficult for AI to understand project layout

Dir2md solves these problems with intelligent analysis, sampling, and optimization specifically designed for the AI era.

---

*Made with ❤️ for developers who want their AI to understand their code*