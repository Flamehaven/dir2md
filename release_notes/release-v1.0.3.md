# Release v1.0.3

## Highlights
- Add repository-level import helpers so local runs and pytest sessions automatically detect the `src` layout.
- Restore gitwildmatch semantics for recursive glob patterns by preventing `**/` from matching root-level files.

## Packaging
- Wheel: `dist/dir2md-1.0.3-py3-none-any.whl`
  - SHA256: `C593567C535834B5BBDBEEEDBF565B60BFE3BBA753B5E64CBF21B47A18219656`
- Source archive: `dist/dir2md-1.0.3.tar.gz`
  - SHA256: `DD1B04C3E70D4858412EB459132BF80A37C3445A68D8982068CE45A05CDA6CA6`

## Testing
- `pytest tests/test_dir2md.py`

## Notes for GitHub Release
- Tag: `v1.0.3`
- Changelog excerpt: use the 1.0.3 section from `CHANGELOG.md`.
- Mention the packaging change warning from `python -m build` about migrating the license field to an SPDX string before Feb 2026.
