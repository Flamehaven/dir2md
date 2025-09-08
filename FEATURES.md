# Dir2md Feature Comparison: Open Source vs Pro

> **Transform your codebase into LLM-optimized markdown blueprints**

Dir2md follows an **Open-Core** model - providing essential functionality for free while offering advanced features for professional teams and power users.

## 🎯 Quick Comparison

| Feature Category | Open Source (Free) | Pro Version |
|------------------|-------------------|-------------|
| **Basic Functionality** | ✅ Full Access | ✅ Enhanced |
| **Security & Masking** | ✅ Basic Patterns | ✅ Advanced + Custom |
| **Performance** | ✅ Single-threaded | ✅ Parallel + Caching |
| **Export Options** | ✅ Markdown Only | ✅ HTML, PDF, Slides |
| **Team Features** | ❌ Individual Use | ✅ CI/CD Integration |
| **Language Support** | ✅ Basic Analysis | ✅ Smart Plugins |

---

## 🔓 Open Source Features (MIT License)

### Core Functionality
- **📁 Directory Scanning**: Complete file tree analysis with `.gitignore` support
- **🎯 Smart Filtering**: Include/exclude/omit glob patterns
- **📊 Token Optimization**: Head/tail sampling with configurable budgets
- **🔄 Duplicate Detection**: SimHash-based content deduplication 
- **📋 Manifest Generation**: JSON metadata with file hashes and statistics
- **⏰ Deterministic Output**: `--no-timestamp` for reproducible builds
- **🎨 Multiple Presets**: `iceberg`, `pro`, `raw` (default: `raw` for developers)

### Basic Security
- **🛡️ Essential Masking**: Protection for common secrets
  - AWS Access Keys (`AKIA[0-9A-Z]{16}`)
  - Bearer Tokens (`Bearer <token>`)
  - Private Keys (`-----BEGIN ... PRIVATE KEY-----`)

### Output Modes
- **📝 Reference Mode**: File listings with metadata
- **📖 Summary Mode**: Condensed content overview
- **📄 Inline Mode**: Full content inclusion (within token budget)

### CLI & Integration
- **⚡ Command Line Interface**: Full-featured CLI with help system
- **🔧 Configurable Options**: Extensive customization via arguments
- **📦 Easy Installation**: `pip install dir2md`

---

## 🔒 Pro Version Features

### Advanced Security & Compliance
- **🛡️ Comprehensive Masking**: 25+ built-in patterns
  - Cloud Provider Keys (AWS, Azure, GCP)
  - API Tokens (Slack, GitHub, GitLab)
  - Database Connections & Credentials
  - Custom Pattern Support
- **🔍 Smart Detection**: File-type aware masking
- **✅ False Positive Reduction**: Context-aware pattern matching
- **📝 Audit Logging**: Security scanning reports

### Performance & Scale
- **⚡ Parallel Processing**: Multi-threaded file analysis
- **💾 Incremental Caching**: `.dir2md_cache/` for faster re-runs
- **📈 Large Repository Support**: Optimized for 10,000+ files
- **🚀 Streaming Processing**: Memory-efficient for massive codebases

### Advanced Analysis
- **🧠 Language Plugins**: Smart code analysis
  - **Python**: AST parsing, function/class extraction
  - **JavaScript/TypeScript**: ES module analysis, export detection
  - **Go**: Package structure, type definitions
  - **Java**: Class hierarchy, annotation extraction
- **📊 Drift Detection**: Compare blueprint versions
- **🎯 Impact Scoring**: Identify critical changes

### Export & Sharing
- **📄 Multiple Formats**: HTML, PDF, PowerPoint slides
- **🎨 Custom Templates**: Branded output with Jinja2
- **📱 Responsive HTML**: Mobile-friendly documentation
- **🖨️ Print Optimization**: Publication-ready PDFs

### Team & CI/CD Integration
- **🤖 GitHub Actions**: Automated blueprint generation
- **💬 PR Comments**: Automatic documentation updates  
- **🔗 GitLab Integration**: Pipeline integration support
- **📋 Status Checks**: Quality gates for documentation
- **👥 Team Templates**: Standardized output formats

### Developer Experience
- **🖥️ Terminal UI (TUI)**: Interactive file selection
- **🔍 Live Preview**: Real-time output preview
- **⚙️ Advanced Configuration**: Team-wide settings
- **📊 Analytics Dashboard**: Usage metrics and insights

---

## 💰 Pricing & Licensing

### Open Source (MIT)
- **Price**: Free forever
- **Use Case**: Individual developers, small projects
- **Support**: Community via GitHub Issues
- **License**: MIT - commercial use allowed

### Pro Version
- **Individual**: $29/month or $290/year
- **Team (5 users)**: $99/month or $990/year  
- **Enterprise**: Custom pricing with on-premise options
- **Support**: Priority email support + documentation
- **License**: Commercial license with usage analytics opt-out

---

## 🚀 Usage Examples

### Open Source Quick Start

```bash
# Install from PyPI
pip install dir2md

# Basic usage with security masking
dir2md ./my-project --masking basic --preset raw

# Generate with manifest for CI/CD
dir2md . --emit-manifest --no-timestamp --output blueprint.md
```

### Pro Version Examples

```bash
# Set Pro license
export DIR2MD_LICENSE="PRO-your-license-key"

# Advanced masking with custom patterns
dir2md . --masking advanced --preset pro

# Parallel processing with caching
dir2md ./large-repo --parallel --use-cache

# Generate multiple formats
dir2md . --export html,pdf --template branded
```

### GitHub Actions Integration

**Open Source:**
```yaml
- name: Generate Blueprint
  run: |
    pip install dir2md
    dir2md . --no-timestamp --output docs/blueprint.md
```

**Pro Version:**
```yaml
- name: Generate Pro Blueprint  
  env:
    DIR2MD_LICENSE: ${{ secrets.DIR2MD_PRO_LICENSE }}
  run: |
    pip install dir2md-pro
    dir2md . --masking advanced --export html --pr-comment
```

---

## 🎯 When to Upgrade to Pro

### Individual Developers
- Working with sensitive codebases requiring advanced security
- Need faster processing for large repositories (1000+ files)
- Want professional-looking exports for client presentations
- Require language-specific code analysis

### Teams & Organizations  
- Standardizing documentation across multiple projects
- Integrating with CI/CD pipelines for automatic updates
- Need compliance features for security auditing
- Want team analytics and usage insights

### Enterprise Users
- On-premise deployment requirements
- SSO/SAML integration needs
- Custom security patterns and compliance rules
- Dedicated support and SLA requirements

---

## 🛠️ Technical Implementation

### Open-Core Architecture
```
dir2md-core (OSS)           dir2md-pro (Commercial)
├── CLI Interface           ├── Advanced Masking
├── File Scanning           ├── Language Plugins  
├── Token Optimization      ├── Parallel Engine
├── Basic Masking           ├── Export Templates
├── Manifest Generation     ├── Team Integration
└── Markdown Output         └── License Validation
```

### License Validation
- **Runtime Check**: Environment variable `DIR2MD_LICENSE`
- **Offline Validation**: Ed25519 signature verification
- **Graceful Degradation**: Falls back to OSS features if invalid
- **No Phone Home**: All validation happens locally

### Plugin System
```python
# Pro Plugin Example
class PythonAnalyzer(LanguagePlugin):
    extensions = {'.py'}
    
    def analyze(self, content: str) -> Dict[str, Any]:
        return {
            'functions': self.extract_functions(content),
            'classes': self.extract_classes(content),
            'imports': self.extract_imports(content)
        }
```

---

## 🆚 Comparison with Alternatives

| Tool | Open Source | Pro Features | License Model |
|------|-------------|--------------|---------------|
| **dir2md** | ✅ Full core functionality | ✅ Advanced security, performance, team features | Open-Core (MIT + Commercial) |
| tree + cat | ✅ Basic listing | ❌ No advanced features | Free (but manual) |
| Proprietary doc tools | ❌ Closed source | ✅ Enterprise features | Subscription only |
| Custom scripts | ✅ DIY solution | ❌ No standardization | Time investment |

---

## 📞 Get Started

### Try Open Source
```bash
pip install dir2md
dir2md --help
```

### Evaluate Pro Features
```bash
# 14-day free trial
export DIR2MD_LICENSE="TRIAL-request-at-dir2md.com"
pip install dir2md-pro
dir2md --masking advanced --parallel
```

### Purchase Pro License
- **Individual**: [Buy now for $29/month](https://dir2md.com/buy/individual)
- **Team**: [Start team trial](https://dir2md.com/buy/team)  
- **Enterprise**: [Contact sales](https://dir2md.com/contact)

---

## 🤝 Contributing

Dir2md's open-source core welcomes contributions:

- **Bug Reports**: [GitHub Issues](https://github.com/your-org/dir2md/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/your-org/dir2md/discussions)
- **Code Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Documentation**: Help improve our guides and examples

Pro features are developed in-house but benefit from community feedback and OSS improvements.

---

*Made with ❤️ for developers who value great documentation*