# Dir2md Current Feature Status

Last verified: 2025-10-09

## Open Source (MIT) Capabilities
- CLI available via source install (`pip install .`) with presets `iceberg`, `pro`, and `raw`.
- Token budgeting and head/tail sampling implemented with manifest support (`--emit-manifest`).
- Basic masking covers AWS keys, bearer tokens, and PEM private keys; improvements from 1.0.2 retained.
- Custom masking regex patterns can be supplied through `--mask-pattern` or `[tool.dir2md].mask_patterns`.
- Gitignore-aware directory traversal with include, exclude, and omit globs using gitwildmatch semantics.
- Simhash duplicate detection and drift scoring present in current code base.
- Project-level configuration loading from `pyproject.toml` available; falls back to CLI arguments.
- **Raw preset disables manifest output** by forcing `emit_manifest=False`, so manifest files are unavailable when that preset is selected.

## Distribution and Versioning
- `pyproject.toml` advertises version 1.0.4, but package `__version__` remains 1.0.3 (`src/dir2md/__init__.py`).
- No 1.0.4 changelog or release notes committed; last documented release is 1.0.3 (2025-10-06).
- PyPI package not published; installation currently limited to cloning the repository and installing from source.

## Documentation Coverage
- README outlines OSS vs Pro positioning but references available guides (`CURRENT_FEATURES.md`, `USAGE_EXAMPLES.md`).
- `FEATURES.md` now uses ASCII-safe markers so it renders correctly on Windows cp949 locales.
- PROJECT_BLUEPRINT.md generated with `dir2md --preset pro` verifies repository contents as of 2025-10-09.

## Pro Feature Parity
- Advanced masking, parallel processing, caching, export formats, and CI add-ons described in README/FEATURES.md are not present in this repository.
- License validation hooks referenced in documentation are not implemented in the open source code.

## Open Issues to Resolve Before 1.0.4 Release
1. Align version strings (`pyproject.toml` and `__init__.py`) and capture deltas in `CHANGELOG.md` and `release_notes/`.
2. Publish wheels and source distributions to PyPI after passing automated tests (`pytest`) and smoke runs of `dir2md`.
3. Update README links or add missing documentation files (`CURRENT_FEATURES.md`, `USAGE_EXAMPLES.md`) with ASCII-safe formatting.
4. Sanitize existing docs to remove non-ASCII characters to prevent cp949 encoding failures. (DONE)
5. Regenerate PROJECT_BLUEPRINT.md only after the above fixes are merged to reflect the final 1.0.4 state.
