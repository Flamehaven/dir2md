# Release v1.0.4

## Highlights
- Expanded the default masking set to cover GitHub personal access tokens, generic API keys, database URLs, JWTs, and OAuth client secrets.
- Added automatic `.env` discovery so license keys and shared presets load without manual exports.
- Introduced first-class support for custom masking patterns through CLI flags, external files, and `[tool.dir2md.masking]` configuration.

## Packaging
- Wheel: `dist/dir2md-1.0.4-py3-none-any.whl`
  - SHA256: _TBD after build_
- Source archive: `dist/dir2md-1.0.4.tar.gz`
  - SHA256: _TBD after build_

## Testing
- `pytest`
- Manual verification of custom masking pattern loading (JSON + text)
- Windows `file://` URI regression test

## Notes for GitHub Release
- Tag: `v1.0.4`
- Highlight the enhanced masking defaults and automatic `.env` loading.
- Remind users that advanced masking remains a Pro-only capability.
