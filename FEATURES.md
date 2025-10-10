# Dir2md Feature Comparison: Open Source vs Pro

> Transform your codebase into LLM-optimized markdown blueprints.

Dir2md follows an open-core model: core functionality remains free, while advanced capabilities are available in the commercial Pro build.

## Quick Comparison

| Feature Category      | Open Source (Free)       | Pro Version                  |
|-----------------------|--------------------------|------------------------------|
| **Core Functionality** | [*] Full access          | [*] Extended presets         |
| **Security & Masking** | [#] Essential patterns   | [#] Advanced and custom      |
| **Performance**        | [=] Single-threaded      | [=] Parallel + caching       |
| **Export Options**     | [T] Markdown only        | [T] HTML, PDF, Slides        |
| **Team Features**      | [+] Individual workflows | [+] CI/CD integrations       |
| **Language Support**   | [T] Basic analysis       | [T] Smart language plugins   |

---

## Open Source Features (MIT License)

### Core Functionality
- [*] Directory scanning with `.gitignore` awareness.
- [*] Include, exclude, and omit glob filters using gitwildmatch semantics.
- [=] Token budgeting with configurable head and tail sampling.
- [*] SimHash-based duplicate detection to minimize repeated content.
- [=] Optional JSON manifest output with file hashes and statistics.
- [+] Deterministic builds via `--no-timestamp`.
- [*] Presets for `iceberg`, `pro`, and `raw` (raw disables manifest output).

### Basic Security
- [#] Built-in masking guardrails for common secrets:
  - AWS Access Keys (`AKIA[0-9A-Z]{16}`)
  - Bearer Tokens (`Bearer <token>`)
  - Private Keys (`-----BEGIN ... PRIVATE KEY-----` blocks with multiline masking)
  - GitHub Personal Access Tokens (`gh[pousr]_<36 chars>`)
  - Generic API key assignments (`api_key=...`, `x-api-key=...`)
  - Database URLs (`postgres://`, `mysql://`, `mongodb+srv://`, `redis://`, `sqlserver://`)
  - JWT tokens (`header.payload.signature`)
  - OAuth client secrets (`client_secret=...`)
- [#] Custom masking hooks via `--mask-pattern` CLI flag or `mask_patterns` in `pyproject.toml`.

### Output Modes
- [*] Reference mode: metadata-only entries for compact manifests.
- [*] Summary mode: condensed inline snippets.
- [*] Inline mode: sampled file content within token budgets.

### CLI & Integration
- [T] Full-featured CLI with contextual help.
- [T] pyproject-driven defaults via `[tool.dir2md]` configuration.
- [+] Automatic `.env` discovery for shared presets and licenses.
- [T] Dry-run hashing for quick pipeline checks.

---

## Pro Version Features

### Advanced Security & Compliance
- [#] 25+ masking patterns covering major cloud providers and SaaS platforms.
- [#] Custom pattern support with context-aware false-positive reduction.
- [#] Audit logs for compliance reporting.

### Performance & Scale
- [=] Parallel directory walkers for multi-threaded analysis.
- [=] Incremental caching (`.dir2md_cache/`) for faster re-runs.
- [=] Streaming mode to handle repositories with 10,000+ files.

### Advanced Analysis
- [T] Language-aware plugins (Python AST summaries, JS/TS export detection, Go packages, Java classes).
- [=] Drift detection to compare blueprint revisions.
- [=] Impact scoring to highlight critical changes.

### Export & Sharing
- [T] Multiple export formats: HTML, PDF, and slide decks.
- [T] Customizable templates (Jinja2) for branded output.
- [T] Responsive HTML optimized for mobile and print workflows.

### Team & CI/CD Integration
- [+] GitHub Actions and GitLab CI reference pipelines.
- [+] Pull request comments with blueprint excerpts.
- [+] Status checks and policy gates for documentation quality.
- [+] Team templates for consistent deliverables.

### Developer Experience
- [T] Interactive terminal UI for selective exports.
- [T] Live preview server for instant feedback.
- [=] Advanced configuration profiles for teams.
- [=] Analytics dashboard for usage insights.

---

## Pricing & Licensing

### Open Source (MIT)
- Price: free forever.
- Best for: individual developers and small projects.
- Support: community-driven via GitHub Issues.
- License: MIT with full commercial rights.

### Pro Version
- Individual: $29/month or $290/year.
- Team (5 users): $99/month or $990/year.
- Enterprise: custom pricing with on-premise deployment.
- Support: priority email assistance and extended documentation.
- License: commercial agreement with analytics opt-out.

---

## Usage Examples

### Open Source Quick Start

```bash
pip install dir2md
dir2md ./my-project --masking basic --preset raw
dir2md . --emit-manifest --no-timestamp --output blueprint.md
```

### Pro Evaluation

```bash
export DIR2MD_LICENSE="TRIAL-request-at-dir2md.com"
pip install dir2md-pro
dir2md . --masking advanced --parallel --export html
```

---

## GitHub Actions Integration

**Open Source**
```yaml
- name: Generate Blueprint
  run: |
    pip install dir2md
    dir2md . --no-timestamp --output docs/blueprint.md
```

**Pro Version**
```yaml
- name: Generate Pro Blueprint
  env:
    DIR2MD_LICENSE: ${{ secrets.DIR2MD_PRO_LICENSE }}
  run: |
    pip install dir2md-pro
    dir2md . --masking advanced --export html --pr-comment
```

---

## When to Upgrade to Pro

### Individual Developers
- Sensitive codebases needing extended masking catalogs.
- Large repositories where parallel processing saves minutes.
- Client deliverables that require polished PDF or slide outputs.
- Desire for language-specific insights beyond generic sampling.

### Teams & Organizations
- Standardized documentation in CI/CD pipelines.
- Compliance workflows requiring audit trails.
- Shared presets and analytics across multiple projects.
- Automated PR annotations for reviewers.

### Enterprise Users
- On-premise or air-gapped deployments.
- SSO and SAML integration requirements.
- Tailored masking policies with legal review.
- Dedicated support with SLAs.

---

## Technical Implementation

```
dir2md-core (OSS)           dir2md-pro (Commercial)
|-- CLI interface           |-- Advanced masking catalog
|-- File scanning           |-- Language plugins
|-- Token optimization      |-- Parallel engine
|-- Basic masking           |-- Export templates
|-- Manifest generation     |-- Team integrations
|-- Markdown output         |-- License validation
```

### License Validation (Pro)
- Runtime checks via the `DIR2MD_LICENSE` environment variable.
- Offline signature verification (Ed25519) with fallback to OSS mode.
- No telemetry or phone-home requests.

### Plugin Architecture (Pro)
```python
class PythonAnalyzer(LanguagePlugin):
    extensions = {".py"}

    def analyze(self, content: str) -> dict[str, object]:
        return {
            "functions": self.extract_functions(content),
            "classes": self.extract_classes(content),
            "imports": self.extract_imports(content),
        }
```

---

## Comparison with Alternatives

| Tool                 | Open Source | Pro Features | License Model            |
|----------------------|-------------|--------------|--------------------------|
| dir2md               | [*] Yes     | [#] Yes      | Open-core (MIT + commercial) |
| tree + cat           | [+] Partial | [-] None     | Free (manual workflows)  |
| Proprietary doc tools| [-] No      | [#] Enterprise | Subscription only        |
| Custom scripts       | [+] DIY     | [-] No       | Time and maintenance cost |

---

## Getting Started

### Try Open Source
```bash
pip install dir2md
dir2md --help
```

### Evaluate Pro Features
```bash
export DIR2MD_LICENSE="TRIAL-request-at-dir2md.com"
pip install dir2md-pro
dir2md --masking advanced --parallel
```

### Purchase Pro License
- Individual: https://dir2md.com/buy/individual
- Team: https://dir2md.com/buy/team
- Enterprise: https://dir2md.com/contact

---

## Contributing

Dir2md's open-source core welcomes contributions:
- Bug reports via GitHub Issues.
- Feature requests via GitHub Discussions.
- Code contributions following `CONTRIBUTING.md` guidelines.
- Documentation improvements and usage examples.

Pro enhancements are developed in-house but benefit from community feedback on the OSS foundation.

---

Made with care for developers who value great documentation.
