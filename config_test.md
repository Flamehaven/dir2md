# Project Blueprint

- Root: `D:\Sanctum\Dir2md`  
- Generated: `2025-10-06 13:37:39`  
- Preset: `raw`  
- LLM mode: `inline`  
- Estimated tokens (prompt): `6000`  

## Directory Tree

```
D:\Sanctum\Dir2md
├── .devcontainer
│   └── devcontainer.json
├── .github
│   └── workflows
│       └── dir2md-blueprint.yml
├── .pytest_cache
│   ├── v
│   │   └── cache
│   │       ├── lastfailed
│   │       └── nodeids
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   └── README.md
├── demo
│   ├── app.py
│   └── requirements.txt
├── extra advertage
│   ├── Dir2md.pdf
│   └── Dir2md__The_AI_Code_Blueprint.mp4
├── patches
│   └── 1.patch
├── scripts
│   └── bench_dir2md.py
├── src
│   ├── dir2md
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── core.py
│   │   ├── gitignore.py
│   │   ├── license.py
│   │   ├── manifest.py
│   │   ├── markdown.py
│   │   ├── masking.py
│   │   ├── parallel.py
│   │   ├── simhash.py
│   │   ├── summary.py
│   │   └── token.py
│   └── dir2md.egg-info
│       ├── dependency_links.txt
│       ├── entry_points.txt
│       ├── PKG-INFO
│       ├── requires.txt
│       ├── SOURCES.txt
│       └── top_level.txt
├── tests
│   └── test_dir2md.py
├── venv_clean
│   ├── Include
│   ├── Lib
│   │   └── site-packages
│   │       ├── _pytest
│   │       │   ├── _code
│   │       │   │   ├── __init__.py
│   │       │   │   ├── code.py
│   │       │   │   └── source.py
│   │       │   ├── _io
│   │       │   │   ├── __init__.py
│   │       │   │   ├── pprint.py
│   │       │   │   ├── saferepr.py
│   │       │   │   ├── terminalwriter.py
│   │       │   │   └── wcwidth.py
│   │       │   ├── _py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── error.py
│   │       │   │   └── path.py
│   │       │   ├── assertion
│   │       │   │   ├── __init__.py
│   │       │   │   ├── rewrite.py
│   │       │   │   ├── truncate.py
│   │       │   │   └── util.py
│   │       │   ├── config
│   │       │   │   ├── __init__.py
│   │       │   │   ├── argparsing.py
│   │       │   │   ├── compat.py
│   │       │   │   ├── exceptions.py
│   │       │   │   └── findpaths.py
│   │       │   ├── mark
│   │       │   │   ├── __init__.py
│   │       │   │   ├── expression.py
│   │       │   │   └── structures.py
│   │       │   ├── __init__.py
│   │       │   ├── _argcomplete.py
│   │       │   ├── _version.py
│   │       │   ├── cacheprovider.py
│   │       │   ├── capture.py
│   │       │   ├── compat.py
│   │       │   ├── debugging.py
│   │       │   ├── deprecated.py
│   │       │   ├── doctest.py
│   │       │   ├── faulthandler.py
│   │       │   ├── fixtures.py
│   │       │   ├── freeze_support.py
│   │       │   ├── helpconfig.py
│   │       │   ├── hookspec.py
│   │       │   ├── junitxml.py
│   │       │   ├── legacypath.py
│   │       │   ├── logging.py
│   │       │   ├── main.py
│   │       │   ├── monkeypatch.py
│   │       │   ├── nodes.py
│   │       │   ├── outcomes.py
│   │       │   ├── pastebin.py
│   │       │   ├── pathlib.py
│   │       │   ├── py.typed
│   │       │   ├── pytester.py
│   │       │   ├── pytester_assertions.py
│   │       │   ├── python.py
│   │       │   ├── python_api.py
│   │       │   ├── raises.py
│   │       │   ├── recwarn.py
│   │       │   ├── reports.py
│   │       │   ├── runner.py
│   │       │   ├── scope.py
│   │       │   ├── setuponly.py
│   │       │   ├── setupplan.py
│   │       │   ├── skipping.py
│   │       │   ├── stash.py
│   │       │   ├── stepwise.py
│   │       │   ├── terminal.py
│   │       │   ├── threadexception.py
│   │       │   ├── timing.py
│   │       │   ├── tmpdir.py
│   │       │   ├── tracemalloc.py
│   │       │   ├── unittest.py
│   │       │   ├── unraisableexception.py
│   │       │   ├── warning_types.py
│   │       │   └── warnings.py
│   │       ├── colorama
│   │       │   ├── tests
│   │       │   │   ├── __init__.py
│   │       │   │   ├── ansi_test.py
│   │       │   │   ├── ansitowin32_test.py
│   │       │   │   ├── initialise_test.py
│   │       │   │   ├── isatty_test.py
│   │       │   │   ├── utils.py
│   │       │   │   └── winterm_test.py
│   │       │   ├── __init__.py
│   │       │   ├── ansi.py
│   │       │   ├── ansitowin32.py
│   │       │   ├── initialise.py
│   │       │   ├── win32.py
│   │       │   └── winterm.py
│   │       ├── colorama-0.4.6.dist-info
│   │       │   ├── licenses
│   │       │   │   └── LICENSE.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── dir2md-0.0.1.dist-info
│   │       │   ├── licenses
│   │       │   │   └── LICENSE
│   │       │   ├── direct_url.json
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── iniconfig
│   │       │   ├── __init__.py
│   │       │   ├── _parse.py
│   │       │   ├── _version.py
│   │       │   ├── exceptions.py
│   │       │   └── py.typed
│   │       ├── iniconfig-2.1.0.dist-info
│   │       │   ├── licenses
│   │       │   │   └── LICENSE
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── packaging
│   │       │   ├── licenses
│   │       │   │   ├── __init__.py
│   │       │   │   └── _spdx.py
│   │       │   ├── __init__.py
│   │       │   ├── _elffile.py
│   │       │   ├── _manylinux.py
│   │       │   ├── _musllinux.py
│   │       │   ├── _parser.py
│   │       │   ├── _structures.py
│   │       │   ├── _tokenizer.py
│   │       │   ├── markers.py
│   │       │   ├── metadata.py
│   │       │   ├── py.typed
│   │       │   ├── requirements.py
│   │       │   ├── specifiers.py
│   │       │   ├── tags.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── packaging-25.0.dist-info
│   │       │   ├── licenses
│   │       │   │   ├── LICENSE
│   │       │   │   ├── LICENSE.APACHE
│   │       │   │   └── LICENSE.BSD
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── pathspec
│   │       │   ├── patterns
│   │       │   │   ├── __init__.py
│   │       │   │   └── gitwildmatch.py
│   │       │   ├── __init__.py
│   │       │   ├── _meta.py
│   │       │   ├── gitignore.py
│   │       │   ├── pathspec.py
│   │       │   ├── pattern.py
│   │       │   ├── py.typed
│   │       │   └── util.py
│   │       ├── pathspec-0.12.1.dist-info
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   └── WHEEL
│   │       ├── pip
│   │       │   ├── _internal
│   │       │   │   ├── cli
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── autocompletion.py
│   │       │   │   │   ├── base_command.py
│   │       │   │   │   ├── cmdoptions.py
│   │       │   │   │   ├── command_context.py
│   │       │   │   │   ├── index_command.py
│   │       │   │   │   ├── main.py
│   │       │   │   │   ├── main_parser.py
│   │       │   │   │   ├── parser.py
│   │       │   │   │   ├── progress_bars.py
│   │       │   │   │   ├── req_command.py
│   │       │   │   │   ├── spinners.py
│   │       │   │   │   └── status_codes.py
│   │       │   │   ├── commands
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── completion.py
│   │       │   │   │   ├── configuration.py
│   │       │   │   │   ├── debug.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   ├── hash.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── inspect.py
│   │       │   │   │   ├── install.py
│   │       │   │   │   ├── list.py
│   │       │   │   │   ├── search.py
│   │       │   │   │   ├── show.py
│   │       │   │   │   ├── uninstall.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── distributions
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   ├── installed.py
│   │       │   │   │   ├── sdist.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── index
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── collector.py
│   │       │   │   │   ├── package_finder.py
│   │       │   │   │   └── sources.py
│   │       │   │   ├── locations
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _distutils.py
│   │       │   │   │   ├── _sysconfig.py
│   │       │   │   │   └── base.py
│   │       │   │   ├── metadata
│   │       │   │   │   ├── importlib
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _compat.py
│   │       │   │   │   │   ├── _dists.py
│   │       │   │   │   │   └── _envs.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _json.py
│   │       │   │   │   ├── base.py
│   │       │   │   │   └── pkg_resources.py
│   │       │   │   ├── models
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── candidate.py
│   │       │   │   │   ├── direct_url.py
│   │       │   │   │   ├── format_control.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── installation_report.py
│   │       │   │   │   ├── link.py
│   │       │   │   │   ├── scheme.py
│   │       │   │   │   ├── search_scope.py
│   │       │   │   │   ├── selection_prefs.py
│   │       │   │   │   ├── target_python.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── network
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── download.py
│   │       │   │   │   ├── lazy_wheel.py
│   │       │   │   │   ├── session.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── xmlrpc.py
│   │       │   │   ├── operations
│   │       │   │   │   ├── install
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── editable_legacy.py
│   │       │   │   │   │   └── wheel.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── check.py
│   │       │   │   │   ├── freeze.py
│   │       │   │   │   └── prepare.py
│   │       │   │   ├── req
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── constructors.py
│   │       │   │   │   ├── req_file.py
│   │       │   │   │   ├── req_install.py
│   │       │   │   │   ├── req_set.py
│   │       │   │   │   └── req_uninstall.py
│   │       │   │   ├── resolution
│   │       │   │   │   ├── legacy
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   ├── resolvelib
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── base.py
│   │       │   │   │   │   ├── candidates.py
│   │       │   │   │   │   ├── factory.py
│   │       │   │   │   │   ├── found_candidates.py
│   │       │   │   │   │   ├── provider.py
│   │       │   │   │   │   ├── reporter.py
│   │       │   │   │   │   ├── requirements.py
│   │       │   │   │   │   └── resolver.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── base.py
│   │       │   │   ├── utils
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _jaraco_text.py
│   │       │   │   │   ├── _log.py
│   │       │   │   │   ├── appdirs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── compatibility_tags.py
│   │       │   │   │   ├── datetime.py
│   │       │   │   │   ├── deprecation.py
│   │       │   │   │   ├── direct_url_helpers.py
│   │       │   │   │   ├── egg_link.py
│   │       │   │   │   ├── encoding.py
│   │       │   │   │   ├── entrypoints.py
│   │       │   │   │   ├── filesystem.py
│   │       │   │   │   ├── filetypes.py
│   │       │   │   │   ├── glibc.py
│   │       │   │   │   ├── hashes.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── misc.py
│   │       │   │   │   ├── packaging.py
│   │       │   │   │   ├── retry.py
│   │       │   │   │   ├── setuptools_build.py
│   │       │   │   │   ├── subprocess.py
│   │       │   │   │   ├── temp_dir.py
│   │       │   │   │   ├── unpacking.py
│   │       │   │   │   ├── urls.py
│   │       │   │   │   ├── virtualenv.py
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── vcs
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── bazaar.py
│   │       │   │   │   ├── git.py
│   │       │   │   │   ├── mercurial.py
│   │       │   │   │   ├── subversion.py
│   │       │   │   │   └── versioncontrol.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── build_env.py
│   │       │   │   ├── cache.py
│   │       │   │   ├── configuration.py
│   │       │   │   ├── exceptions.py
│   │       │   │   ├── main.py
│   │       │   │   ├── pyproject.py
│   │       │   │   ├── self_outdated_check.py
│   │       │   │   └── wheel_builder.py
│   │       │   ├── _vendor
│   │       │   │   ├── cachecontrol
│   │       │   │   │   ├── caches
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── file_cache.py
│   │       │   │   │   │   └── redis_cache.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _cmd.py
│   │       │   │   │   ├── adapter.py
│   │       │   │   │   ├── cache.py
│   │       │   │   │   ├── controller.py
│   │       │   │   │   ├── filewrapper.py
│   │       │   │   │   ├── heuristics.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   ├── serialize.py
│   │       │   │   │   └── wrapper.py
│   │       │   │   ├── certifi
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── cacert.pem
│   │       │   │   │   ├── core.py
│   │       │   │   │   └── py.typed
│   │       │   │   ├── distlib
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── database.py
│   │       │   │   │   ├── index.py
│   │       │   │   │   ├── locators.py
│   │       │   │   │   ├── manifest.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── metadata.py
│   │       │   │   │   ├── resources.py
│   │       │   │   │   ├── scripts.py
│   │       │   │   │   ├── t32.exe
│   │       │   │   │   ├── t64-arm.exe
│   │       │   │   │   ├── t64.exe
│   │       │   │   │   ├── util.py
│   │       │   │   │   ├── version.py
│   │       │   │   │   ├── w32.exe
│   │       │   │   │   ├── w64-arm.exe
│   │       │   │   │   ├── w64.exe
│   │       │   │   │   └── wheel.py
│   │       │   │   ├── distro
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── distro.py
│   │       │   │   │   └── py.typed
│   │       │   │   ├── idna
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── codec.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── core.py
│   │       │   │   │   ├── idnadata.py
│   │       │   │   │   ├── intranges.py
│   │       │   │   │   ├── package_data.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   └── uts46data.py
│   │       │   │   ├── msgpack
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── ext.py
│   │       │   │   │   └── fallback.py
│   │       │   │   ├── packaging
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _elffile.py
│   │       │   │   │   ├── _manylinux.py
│   │       │   │   │   ├── _musllinux.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _structures.py
│   │       │   │   │   ├── _tokenizer.py
│   │       │   │   │   ├── markers.py
│   │       │   │   │   ├── metadata.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   ├── requirements.py
│   │       │   │   │   ├── specifiers.py
│   │       │   │   │   ├── tags.py
│   │       │   │   │   ├── utils.py
│   │       │   │   │   └── version.py
│   │       │   │   ├── pkg_resources
│   │       │   │   │   └── __init__.py
│   │       │   │   ├── platformdirs
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── android.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── macos.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   ├── unix.py
│   │       │   │   │   ├── version.py
│   │       │   │   │   └── windows.py
│   │       │   │   ├── pygments
│   │       │   │   │   ├── filters
│   │       │   │   │   │   └── __init__.py
│   │       │   │   │   ├── formatters
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _mapping.py
│   │       │   │   │   │   ├── bbcode.py
│   │       │   │   │   │   ├── groff.py
│   │       │   │   │   │   ├── html.py
│   │       │   │   │   │   ├── img.py
│   │       │   │   │   │   ├── irc.py
│   │       │   │   │   │   ├── latex.py
│   │       │   │   │   │   ├── other.py
│   │       │   │   │   │   ├── pangomarkup.py
│   │       │   │   │   │   ├── rtf.py
│   │       │   │   │   │   ├── svg.py
│   │       │   │   │   │   ├── terminal.py
│   │       │   │   │   │   └── terminal256.py
│   │       │   │   │   ├── lexers
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _mapping.py
│   │       │   │   │   │   └── python.py
│   │       │   │   │   ├── styles
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _mapping.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── cmdline.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── filter.py
│   │       │   │   │   ├── formatter.py
│   │       │   │   │   ├── lexer.py
│   │       │   │   │   ├── modeline.py
│   │       │   │   │   ├── plugin.py
│   │       │   │   │   ├── regexopt.py
│   │       │   │   │   ├── scanner.py
│   │       │   │   │   ├── sphinxext.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── token.py
│   │       │   │   │   ├── unistring.py
│   │       │   │   │   └── util.py
│   │       │   │   ├── pyproject_hooks
│   │       │   │   │   ├── _in_process
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── _in_process.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _compat.py
│   │       │   │   │   └── _impl.py
│   │       │   │   ├── requests
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __version__.py
│   │       │   │   │   ├── _internal_utils.py
│   │       │   │   │   ├── adapters.py
│   │       │   │   │   ├── api.py
│   │       │   │   │   ├── auth.py
│   │       │   │   │   ├── certs.py
│   │       │   │   │   ├── compat.py
│   │       │   │   │   ├── cookies.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── help.py
│   │       │   │   │   ├── hooks.py
│   │       │   │   │   ├── models.py
│   │       │   │   │   ├── packages.py
│   │       │   │   │   ├── sessions.py
│   │       │   │   │   ├── status_codes.py
│   │       │   │   │   ├── structures.py
│   │       │   │   │   └── utils.py
│   │       │   │   ├── resolvelib
│   │       │   │   │   ├── compat
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── collections_abc.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── providers.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   ├── reporters.py
│   │       │   │   │   ├── resolvers.py
│   │       │   │   │   └── structs.py
│   │       │   │   ├── rich
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __main__.py
│   │       │   │   │   ├── _cell_widths.py
│   │       │   │   │   ├── _emoji_codes.py
│   │       │   │   │   ├── _emoji_replace.py
│   │       │   │   │   ├── _export_format.py
│   │       │   │   │   ├── _extension.py
│   │       │   │   │   ├── _fileno.py
│   │       │   │   │   ├── _inspect.py
│   │       │   │   │   ├── _log_render.py
│   │       │   │   │   ├── _loop.py
│   │       │   │   │   ├── _null_file.py
│   │       │   │   │   ├── _palettes.py
│   │       │   │   │   ├── _pick.py
│   │       │   │   │   ├── _ratio.py
│   │       │   │   │   ├── _spinners.py
│   │       │   │   │   ├── _stack.py
│   │       │   │   │   ├── _timer.py
│   │       │   │   │   ├── _win32_console.py
│   │       │   │   │   ├── _windows.py
│   │       │   │   │   ├── _windows_renderer.py
│   │       │   │   │   ├── _wrap.py
│   │       │   │   │   ├── abc.py
│   │       │   │   │   ├── align.py
│   │       │   │   │   ├── ansi.py
│   │       │   │   │   ├── bar.py
│   │       │   │   │   ├── box.py
│   │       │   │   │   ├── cells.py
│   │       │   │   │   ├── color.py
│   │       │   │   │   ├── color_triplet.py
│   │       │   │   │   ├── columns.py
│   │       │   │   │   ├── console.py
│   │       │   │   │   ├── constrain.py
│   │       │   │   │   ├── containers.py
│   │       │   │   │   ├── control.py
│   │       │   │   │   ├── default_styles.py
│   │       │   │   │   ├── diagnose.py
│   │       │   │   │   ├── emoji.py
│   │       │   │   │   ├── errors.py
│   │       │   │   │   ├── file_proxy.py
│   │       │   │   │   ├── filesize.py
│   │       │   │   │   ├── highlighter.py
│   │       │   │   │   ├── json.py
│   │       │   │   │   ├── jupyter.py
│   │       │   │   │   ├── layout.py
│   │       │   │   │   ├── live.py
│   │       │   │   │   ├── live_render.py
│   │       │   │   │   ├── logging.py
│   │       │   │   │   ├── markup.py
│   │       │   │   │   ├── measure.py
│   │       │   │   │   ├── padding.py
│   │       │   │   │   ├── pager.py
│   │       │   │   │   ├── palette.py
│   │       │   │   │   ├── panel.py
│   │       │   │   │   ├── pretty.py
│   │       │   │   │   ├── progress.py
│   │       │   │   │   ├── progress_bar.py
│   │       │   │   │   ├── prompt.py
│   │       │   │   │   ├── protocol.py
│   │       │   │   │   ├── py.typed
│   │       │   │   │   ├── region.py
│   │       │   │   │   ├── repr.py
│   │       │   │   │   ├── rule.py
│   │       │   │   │   ├── scope.py
│   │       │   │   │   ├── screen.py
│   │       │   │   │   ├── segment.py
│   │       │   │   │   ├── spinner.py
│   │       │   │   │   ├── status.py
│   │       │   │   │   ├── style.py
│   │       │   │   │   ├── styled.py
│   │       │   │   │   ├── syntax.py
│   │       │   │   │   ├── table.py
│   │       │   │   │   ├── terminal_theme.py
│   │       │   │   │   ├── text.py
│   │       │   │   │   ├── theme.py
│   │       │   │   │   ├── themes.py
│   │       │   │   │   ├── traceback.py
│   │       │   │   │   └── tree.py
│   │       │   │   ├── tomli
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _parser.py
│   │       │   │   │   ├── _re.py
│   │       │   │   │   ├── _types.py
│   │       │   │   │   └── py.typed
│   │       │   │   ├── truststore
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _api.py
│   │       │   │   │   ├── _macos.py
│   │       │   │   │   ├── _openssl.py
│   │       │   │   │   ├── _ssl_constants.py
│   │       │   │   │   ├── _windows.py
│   │       │   │   │   └── py.typed
│   │       │   │   ├── urllib3
│   │       │   │   │   ├── contrib
│   │       │   │   │   │   ├── _securetransport
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── bindings.py
│   │       │   │   │   │   │   └── low_level.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── _appengine_environ.py
│   │       │   │   │   │   ├── appengine.py
│   │       │   │   │   │   ├── ntlmpool.py
│   │       │   │   │   │   ├── pyopenssl.py
│   │       │   │   │   │   ├── securetransport.py
│   │       │   │   │   │   └── socks.py
│   │       │   │   │   ├── packages
│   │       │   │   │   │   ├── backports
│   │       │   │   │   │   │   ├── __init__.py
│   │       │   │   │   │   │   ├── makefile.py
│   │       │   │   │   │   │   └── weakref_finalize.py
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   └── six.py
│   │       │   │   │   ├── util
│   │       │   │   │   │   ├── __init__.py
│   │       │   │   │   │   ├── connection.py
│   │       │   │   │   │   ├── proxy.py
│   │       │   │   │   │   ├── queue.py
│   │       │   │   │   │   ├── request.py
│   │       │   │   │   │   ├── response.py
│   │       │   │   │   │   ├── retry.py
│   │       │   │   │   │   ├── ssl_.py
│   │       │   │   │   │   ├── ssl_match_hostname.py
│   │       │   │   │   │   ├── ssltransport.py
│   │       │   │   │   │   ├── timeout.py
│   │       │   │   │   │   ├── url.py
│   │       │   │   │   │   └── wait.py
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── _collections.py
│   │       │   │   │   ├── _version.py
│   │       │   │   │   ├── connection.py
│   │       │   │   │   ├── connectionpool.py
│   │       │   │   │   ├── exceptions.py
│   │       │   │   │   ├── fields.py
│   │       │   │   │   ├── filepost.py
│   │       │   │   │   ├── poolmanager.py
│   │       │   │   │   ├── request.py
│   │       │   │   │   └── response.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── typing_extensions.py
│   │       │   │   └── vendor.txt
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── __pip-runner__.py
│   │       │   └── py.typed
│   │       ├── pip-24.2.dist-info
│   │       │   ├── AUTHORS.txt
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE.txt
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── pluggy
│   │       │   ├── __init__.py
│   │       │   ├── _callers.py
│   │       │   ├── _hooks.py
│   │       │   ├── _manager.py
│   │       │   ├── _result.py
│   │       │   ├── _tracing.py
│   │       │   ├── _version.py
│   │       │   ├── _warnings.py
│   │       │   └── py.typed
│   │       ├── pluggy-1.6.0.dist-info
│   │       │   ├── licenses
│   │       │   │   └── LICENSE
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── pygments
│   │       │   ├── filters
│   │       │   │   └── __init__.py
│   │       │   ├── formatters
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── bbcode.py
│   │       │   │   ├── groff.py
│   │       │   │   ├── html.py
│   │       │   │   ├── img.py
│   │       │   │   ├── irc.py
│   │       │   │   ├── latex.py
│   │       │   │   ├── other.py
│   │       │   │   ├── pangomarkup.py
│   │       │   │   ├── rtf.py
│   │       │   │   ├── svg.py
│   │       │   │   ├── terminal.py
│   │       │   │   └── terminal256.py
│   │       │   ├── lexers
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _ada_builtins.py
│   │       │   │   ├── _asy_builtins.py
│   │       │   │   ├── _cl_builtins.py
│   │       │   │   ├── _cocoa_builtins.py
│   │       │   │   ├── _csound_builtins.py
│   │       │   │   ├── _css_builtins.py
│   │       │   │   ├── _googlesql_builtins.py
│   │       │   │   ├── _julia_builtins.py
│   │       │   │   ├── _lasso_builtins.py
│   │       │   │   ├── _lilypond_builtins.py
│   │       │   │   ├── _lua_builtins.py
│   │       │   │   ├── _luau_builtins.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── _mql_builtins.py
│   │       │   │   ├── _mysql_builtins.py
│   │       │   │   ├── _openedge_builtins.py
│   │       │   │   ├── _php_builtins.py
│   │       │   │   ├── _postgres_builtins.py
│   │       │   │   ├── _qlik_builtins.py
│   │       │   │   ├── _scheme_builtins.py
│   │       │   │   ├── _scilab_builtins.py
│   │       │   │   ├── _sourcemod_builtins.py
│   │       │   │   ├── _sql_builtins.py
│   │       │   │   ├── _stan_builtins.py
│   │       │   │   ├── _stata_builtins.py
│   │       │   │   ├── _tsql_builtins.py
│   │       │   │   ├── _usd_builtins.py
│   │       │   │   ├── _vbscript_builtins.py
│   │       │   │   ├── _vim_builtins.py
│   │       │   │   ├── actionscript.py
│   │       │   │   ├── ada.py
│   │       │   │   ├── agile.py
│   │       │   │   ├── algebra.py
│   │       │   │   ├── ambient.py
│   │       │   │   ├── amdgpu.py
│   │       │   │   ├── ampl.py
│   │       │   │   ├── apdlexer.py
│   │       │   │   ├── apl.py
│   │       │   │   ├── archetype.py
│   │       │   │   ├── arrow.py
│   │       │   │   ├── arturo.py
│   │       │   │   ├── asc.py
│   │       │   │   ├── asm.py
│   │       │   │   ├── asn1.py
│   │       │   │   ├── automation.py
│   │       │   │   ├── bare.py
│   │       │   │   ├── basic.py
│   │       │   │   ├── bdd.py
│   │       │   │   ├── berry.py
│   │       │   │   ├── bibtex.py
│   │       │   │   ├── blueprint.py
│   │       │   │   ├── boa.py
│   │       │   │   ├── bqn.py
│   │       │   │   ├── business.py
│   │       │   │   ├── c_cpp.py
│   │       │   │   ├── c_like.py
│   │       │   │   ├── capnproto.py
│   │       │   │   ├── carbon.py
│   │       │   │   ├── cddl.py
│   │       │   │   ├── chapel.py
│   │       │   │   ├── clean.py
│   │       │   │   ├── codeql.py
│   │       │   │   ├── comal.py
│   │       │   │   ├── compiled.py
│   │       │   │   ├── configs.py
│   │       │   │   ├── console.py
│   │       │   │   ├── cplint.py
│   │       │   │   ├── crystal.py
│   │       │   │   ├── csound.py
│   │       │   │   ├── css.py
│   │       │   │   ├── d.py
│   │       │   │   ├── dalvik.py
│   │       │   │   ├── data.py
│   │       │   │   ├── dax.py
│   │       │   │   ├── devicetree.py
│   │       │   │   ├── diff.py
│   │       │   │   ├── dns.py
│   │       │   │   ├── dotnet.py
│   │       │   │   ├── dsls.py
│   │       │   │   ├── dylan.py
│   │       │   │   ├── ecl.py
│   │       │   │   ├── eiffel.py
│   │       │   │   ├── elm.py
│   │       │   │   ├── elpi.py
│   │       │   │   ├── email.py
│   │       │   │   ├── erlang.py
│   │       │   │   ├── esoteric.py
│   │       │   │   ├── ezhil.py
│   │       │   │   ├── factor.py
│   │       │   │   ├── fantom.py
│   │       │   │   ├── felix.py
│   │       │   │   ├── fift.py
│   │       │   │   ├── floscript.py
│   │       │   │   ├── forth.py
│   │       │   │   ├── fortran.py
│   │       │   │   ├── foxpro.py
│   │       │   │   ├── freefem.py
│   │       │   │   ├── func.py
│   │       │   │   ├── functional.py
│   │       │   │   ├── futhark.py
│   │       │   │   ├── gcodelexer.py
│   │       │   │   ├── gdscript.py
│   │       │   │   ├── gleam.py
│   │       │   │   ├── go.py
│   │       │   │   ├── grammar_notation.py
│   │       │   │   ├── graph.py
│   │       │   │   ├── graphics.py
│   │       │   │   ├── graphql.py
│   │       │   │   ├── graphviz.py
│   │       │   │   ├── gsql.py
│   │       │   │   ├── hare.py
│   │       │   │   ├── haskell.py
│   │       │   │   ├── haxe.py
│   │       │   │   ├── hdl.py
│   │       │   │   ├── hexdump.py
│   │       │   │   ├── html.py
│   │       │   │   ├── idl.py
│   │       │   │   ├── igor.py
│   │       │   │   ├── inferno.py
│   │       │   │   ├── installers.py
│   │       │   │   ├── int_fiction.py
│   │       │   │   ├── iolang.py
│   │       │   │   ├── j.py
│   │       │   │   ├── javascript.py
│   │       │   │   ├── jmespath.py
│   │       │   │   ├── jslt.py
│   │       │   │   ├── json5.py
│   │       │   │   ├── jsonnet.py
│   │       │   │   ├── jsx.py
│   │       │   │   ├── julia.py
│   │       │   │   ├── jvm.py
│   │       │   │   ├── kuin.py
│   │       │   │   ├── kusto.py
│   │       │   │   ├── ldap.py
│   │       │   │   ├── lean.py
│   │       │   │   ├── lilypond.py
│   │       │   │   ├── lisp.py
│   │       │   │   ├── macaulay2.py
│   │       │   │   ├── make.py
│   │       │   │   ├── maple.py
│   │       │   │   ├── markup.py
│   │       │   │   ├── math.py
│   │       │   │   ├── matlab.py
│   │       │   │   ├── maxima.py
│   │       │   │   ├── meson.py
│   │       │   │   ├── mime.py
│   │       │   │   ├── minecraft.py
│   │       │   │   ├── mips.py
│   │       │   │   ├── ml.py
│   │       │   │   ├── modeling.py
│   │       │   │   ├── modula2.py
│   │       │   │   ├── mojo.py
│   │       │   │   ├── monte.py
│   │       │   │   ├── mosel.py
│   │       │   │   ├── ncl.py
│   │       │   │   ├── nimrod.py
│   │       │   │   ├── nit.py
│   │       │   │   ├── nix.py
│   │       │   │   ├── numbair.py
│   │       │   │   ├── oberon.py
│   │       │   │   ├── objective.py
│   │       │   │   ├── ooc.py
│   │       │   │   ├── openscad.py
│   │       │   │   ├── other.py
│   │       │   │   ├── parasail.py
│   │       │   │   ├── parsers.py
│   │       │   │   ├── pascal.py
│   │       │   │   ├── pawn.py
│   │       │   │   ├── pddl.py
│   │       │   │   ├── perl.py
│   │       │   │   ├── phix.py
│   │       │   │   ├── php.py
│   │       │   │   ├── pointless.py
│   │       │   │   ├── pony.py
│   │       │   │   ├── praat.py
│   │       │   │   ├── procfile.py
│   │       │   │   ├── prolog.py
│   │       │   │   ├── promql.py
│   │       │   │   ├── prql.py
│   │       │   │   ├── ptx.py
│   │       │   │   ├── python.py
│   │       │   │   ├── q.py
│   │       │   │   ├── qlik.py
│   │       │   │   ├── qvt.py
│   │       │   │   ├── r.py
│   │       │   │   ├── rdf.py
│   │       │   │   ├── rebol.py
│   │       │   │   ├── rego.py
│   │       │   │   ├── resource.py
│   │       │   │   ├── ride.py
│   │       │   │   ├── rita.py
│   │       │   │   ├── rnc.py
│   │       │   │   ├── roboconf.py
│   │       │   │   ├── robotframework.py
│   │       │   │   ├── ruby.py
│   │       │   │   ├── rust.py
│   │       │   │   ├── sas.py
│   │       │   │   ├── savi.py
│   │       │   │   ├── scdoc.py
│   │       │   │   ├── scripting.py
│   │       │   │   ├── sgf.py
│   │       │   │   ├── shell.py
│   │       │   │   ├── sieve.py
│   │       │   │   ├── slash.py
│   │       │   │   ├── smalltalk.py
│   │       │   │   ├── smithy.py
│   │       │   │   ├── smv.py
│   │       │   │   ├── snobol.py
│   │       │   │   ├── solidity.py
│   │       │   │   ├── soong.py
│   │       │   │   ├── sophia.py
│   │       │   │   ├── special.py
│   │       │   │   ├── spice.py
│   │       │   │   ├── sql.py
│   │       │   │   ├── srcinfo.py
│   │       │   │   ├── stata.py
│   │       │   │   ├── supercollider.py
│   │       │   │   ├── tablegen.py
│   │       │   │   ├── tact.py
│   │       │   │   ├── tal.py
│   │       │   │   ├── tcl.py
│   │       │   │   ├── teal.py
│   │       │   │   ├── templates.py
│   │       │   │   ├── teraterm.py
│   │       │   │   ├── testing.py
│   │       │   │   ├── text.py
│   │       │   │   ├── textedit.py
│   │       │   │   ├── textfmts.py
│   │       │   │   ├── theorem.py
│   │       │   │   ├── thingsdb.py
│   │       │   │   ├── tlb.py
│   │       │   │   ├── tls.py
│   │       │   │   ├── tnt.py
│   │       │   │   ├── trafficscript.py
│   │       │   │   ├── typoscript.py
│   │       │   │   ├── typst.py
│   │       │   │   ├── ul4.py
│   │       │   │   ├── unicon.py
│   │       │   │   ├── urbi.py
│   │       │   │   ├── usd.py
│   │       │   │   ├── varnish.py
│   │       │   │   ├── verification.py
│   │       │   │   ├── verifpal.py
│   │       │   │   ├── vip.py
│   │       │   │   ├── vyper.py
│   │       │   │   ├── web.py
│   │       │   │   ├── webassembly.py
│   │       │   │   ├── webidl.py
│   │       │   │   ├── webmisc.py
│   │       │   │   ├── wgsl.py
│   │       │   │   ├── whiley.py
│   │       │   │   ├── wowtoc.py
│   │       │   │   ├── wren.py
│   │       │   │   ├── x10.py
│   │       │   │   ├── xorg.py
│   │       │   │   ├── yang.py
│   │       │   │   ├── yara.py
│   │       │   │   └── zig.py
│   │       │   ├── styles
│   │       │   │   ├── __init__.py
│   │       │   │   ├── _mapping.py
│   │       │   │   ├── abap.py
│   │       │   │   ├── algol.py
│   │       │   │   ├── algol_nu.py
│   │       │   │   ├── arduino.py
│   │       │   │   ├── autumn.py
│   │       │   │   ├── borland.py
│   │       │   │   ├── bw.py
│   │       │   │   ├── coffee.py
│   │       │   │   ├── colorful.py
│   │       │   │   ├── default.py
│   │       │   │   ├── dracula.py
│   │       │   │   ├── emacs.py
│   │       │   │   ├── friendly.py
│   │       │   │   ├── friendly_grayscale.py
│   │       │   │   ├── fruity.py
│   │       │   │   ├── gh_dark.py
│   │       │   │   ├── gruvbox.py
│   │       │   │   ├── igor.py
│   │       │   │   ├── inkpot.py
│   │       │   │   ├── lightbulb.py
│   │       │   │   ├── lilypond.py
│   │       │   │   ├── lovelace.py
│   │       │   │   ├── manni.py
│   │       │   │   ├── material.py
│   │       │   │   ├── monokai.py
│   │       │   │   ├── murphy.py
│   │       │   │   ├── native.py
│   │       │   │   ├── nord.py
│   │       │   │   ├── onedark.py
│   │       │   │   ├── paraiso_dark.py
│   │       │   │   ├── paraiso_light.py
│   │       │   │   ├── pastie.py
│   │       │   │   ├── perldoc.py
│   │       │   │   ├── rainbow_dash.py
│   │       │   │   ├── rrt.py
│   │       │   │   ├── sas.py
│   │       │   │   ├── solarized.py
│   │       │   │   ├── staroffice.py
│   │       │   │   ├── stata_dark.py
│   │       │   │   ├── stata_light.py
│   │       │   │   ├── tango.py
│   │       │   │   ├── trac.py
│   │       │   │   ├── vim.py
│   │       │   │   ├── vs.py
│   │       │   │   ├── xcode.py
│   │       │   │   └── zenburn.py
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cmdline.py
│   │       │   ├── console.py
│   │       │   ├── filter.py
│   │       │   ├── formatter.py
│   │       │   ├── lexer.py
│   │       │   ├── modeline.py
│   │       │   ├── plugin.py
│   │       │   ├── regexopt.py
│   │       │   ├── scanner.py
│   │       │   ├── sphinxext.py
│   │       │   ├── style.py
│   │       │   ├── token.py
│   │       │   ├── unistring.py
│   │       │   └── util.py
│   │       ├── pygments-2.19.2.dist-info
│   │       │   ├── licenses
│   │       │   │   ├── AUTHORS
│   │       │   │   └── LICENSE
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── pytest
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   └── py.typed
│   │       ├── pytest-8.4.2.dist-info
│   │       │   ├── licenses
│   │       │   │   ├── AUTHORS
│   │       │   │   └── LICENSE
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── __editable__.dir2md-0.0.1.pth
│   │       └── py.py
│   ├── Scripts
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── Activate.ps1
│   │   ├── deactivate.bat
│   │   ├── dir2md.exe
│   │   ├── pip.exe
│   │   ├── pip3.12.exe
│   │   ├── pip3.exe
│   │   ├── py.test.exe
│   │   ├── pygmentize.exe
│   │   ├── pytest.exe
│   │   ├── python.exe
│   │   └── pythonw.exe
│   └── pyvenv.cfg
├── .env
├── .env.example
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── config_test.manifest.json
├── config_test.md
├── Dockerfile
├── FEATURES.md
├── LICENSE
├── PROJECT_BLUEPRINT.md
├── pyproject.toml
├── README.md
├── requirements.txt
├── SECURITY.md
└── update.txt
```


## File Contents

### File: `.devcontainer\devcontainer.json`

```json
{
  "name": "dir2md",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "postCreateCommand": "pip install -e . && pre-commit install",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "ms-python.vscode-pylance"]
    }
  }
}
```


### File: `.github\workflows\dir2md-blueprint.yml`

```yml
name: dir2md Blueprint
on:
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize, reopened]
  workflow_dispatch:

jobs:
  build-blueprint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dir2md
        run: |
          python -m pip install --upgrade pip
          pip install .
      - name: Generate blueprint
        id: gen
        run: |
          dir2md . --capsule --emit-manifest --stats -o DIR2MD_BLUEPRINT.md || true
          TOKENS=$(jq .stats.est_tokens_prompt DIR2MD_BLUEPRINT.manifest.json 2>/dev/null || echo "0")
          echo "tokens=$TOKENS" >> $GITHUB_OUTPUT
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: dir2md-blueprint
          path: |
            DIR2MD_BLUEPRINT.md
            DIR2MD_BLUEPRINT.manifest.json
            DIR2MD_BLUEPRINT.capsule.zip
      - name: Comment PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const tokens = '${{ steps.gen.outputs.tokens }}';
            const body = [
              '## 📦 dir2md Blueprint',
              `- Estimated prompt tokens: **${tokens}**`,
              '- Artifacts: _see workflow run → Artifacts_',
              '',
              'Run locally:',
              '```bash',
              'pip install .',
              'dir2md .',
              '```'
            ].join('\n');
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body
            });
```


### File: `.pytest_cache\v\cache\lastfailed`

```text
{}
```


### File: `.pytest_cache\v\cache\nodeids`

```text
[
  "tests/test_dir2md.py::test_budget_and_modes",
  "tests/test_dir2md.py::test_follow_symlinks_behavior",
  "tests/test_dir2md.py::test_include_glob_filtering",
  "tests/test_dir2md.py::test_inline_sampling",
  "tests/test_dir2md.py::test_masking",
  "tests/test_dir2md.py::test_masking_pro_license_mode_respect",
  "tests/test_dir2md.py::test_nested_glob_patterns",
  "tests/test_dir2md.py::test_ref_mode_manifest",
  "tests/test_dir2md.py::test_sha256_preservation_with_max_bytes"
]
```


### File: `.pytest_cache\.gitignore`

```text
# Created by pytest automatically.
*
```


### File: `.pytest_cache\CACHEDIR.TAG`

```TAG
Signature: 8a477f597d28d172789f06886806bc55
# This file is a cache directory tag created by pytest.
# For information about cache directory tags, see:
#	https://bford.info/cachedir/spec.html
```


### File: `.pytest_cache\README.md`

```md
# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
```


### File: `demo\app.py`

```py
import gradio as gr
import git
import tempfile
import shutil
from pathlib import Path
import os

# dir2md will be imported from the source code uploaded to the Space.
from dir2md.core import generate_markdown_report, Config

def process_github_repo(repo_url: str, preset: str):
    """
    Clones a GitHub repository and generates a dir2md blueprint.
    """
    temp_dir_path = None
    try:
        # 1. Create a temporary directory
        temp_dir_path = tempfile.mkdtemp()
        temp_dir = Path(temp_dir_path)

        # 2. Clone the Git repository
        gr.Info(f"Cloning repository: {repo_url}...")
        git.Repo.clone_from(repo_url, temp_dir)
        gr.Info("Repository cloned. Generating blueprint...")

        # 3. Create a dir2md Config object
        # The output path is temporary as we return the content as a string.
        output_path = temp_dir / "blueprint.md"

        cfg = Config(
            root=temp_dir,
            output=output_path,
            preset=preset,
            # Default values
            include_globs=[],
            exclude_globs=[],
            omit_globs=[],
            respect_gitignore=True,
            follow_symlinks=False,
            max_bytes=None,
            max_lines=None,
            include_contents=True,
            llm_mode="ref",
            budget_tokens=8000,
            max_file_tokens=2000,
            dedup_bits=16,
            sample_head=120,
            sample_tail=40,
            strip_comments=False,
            emit_manifest=False, # No manifest file needed for the demo
            explain_capsule=False,
            no_timestamp=True,
            masking_mode="basic"
        )

        # 4. Call the blueprint generation function
        md_output = generate_markdown_report(cfg)
        gr.Info("Blueprint generated successfully!")

        return md_output

    except Exception as e:
        # Clean up the temp directory on error
        if temp_dir_path and os.path.exists(temp_dir_path):
            shutil.rmtree(temp_dir_path)
        return f"An error occurred: {e}"
    finally:
        # 5. Delete the temporary directory
        if temp_dir_path and os.path.exists(temp_dir_path):
            shutil.rmtree(temp_dir_path)

# 6. Define the Gradio interface
demo = gr.Interface(
    fn=process_github_repo,
    inputs=[
        gr.Textbox(label="GitHub Repository URL", placeholder="https://github.com/Flamehaven/dir2md"),
        gr.Radio(choices=["iceberg", "raw", "pro"], value="iceberg", label="Select Preset")
    ],
    outputs=gr.Textbox(label="Markdown Blueprint", lines=30, show_copy_button=True),
    title="dir2md: AI-Ready Repository Blueprint Generator",
    description="Enter the URL of a public GitHub repository to convert its structure and content into an LLM-friendly Markdown blueprint.",
    allow_flagging="never",
    examples=[["https://github.com/psf/requests", "iceberg"], ["https://github.com/gradio-app/gradio", "raw"]]
)

demo.launch()
```


### File: `demo\requirements.txt`

```txt
gradio
pathspec>=0.12.0
GitPython
```


### File: `extra advertage\Dir2md.pdf`

```pdf
%PDF-1.4
%����
1 0 obj
<<
/Type /Catalog
/Version /1.4
/Pages 2 0 R
/StructTreeRoot 3 0 R
/MarkInfo 4 0 R
/Lang (ko-KR)
/ViewerPreferences 5 0 R
>>
endobj
6 0 obj
<<
/Title <FEFFC81CBAA90020C5C6B2940020B514C790C778>
/Creator (Canva)
/Producer (Canva)
/CreationDate (D:20250908113636+00'00')
/ModDate (D:20250908113634+00'00')
/Keywords (DAGyYbIS73A,BAEy504CNMk,0)
/Author (Life GuruKing)
/containsAiGeneratedContent (Yes)
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [7 0 R 8 0 R 9 0 R 10 0 R 11 0 R 12 0 R 13 0 R 14 0 R 15 0 R 16 0 R
17 0 R 18 0 R 19 0 R 20 0 R 21 0 R 22 0 R 23 0 R 24 0 R]
/Count 18
>>
endobj
3 0 obj
<<
/Type /StructTreeRoot
/K [25 0 R]
/ParentTree 26 0 R
/ParentTreeNextKey 1
>>
endobj
4 0 obj
<<
/Marked true
/Suspects false
>>
endobj
5 0 obj
<<
/Type /ViewerPreferences
/DisplayDocTitle true
>>
endobj
7 0 obj
<<
/Type /Page
/Resources <<
/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState 27 0 R
/XObject <<
/X4 28 0 R
>>
>>
/MediaBox [0.0 7.920007 1440.0 817.92]
/Contents 29 0 R
/StructParents 0
/Tabs /S
/Parent 2 0 R
/BleedBox [0.0 7.920007 1440.0 817.92]
/TrimBox [0.0 7.920007 1440.0 817.92]
/CropBox [0.0 7.920007 1440.0 817.92]
/Rotate 0
/Annots []
>>
endobj
8 0 obj
<<
/Type /Page
/Resources <<
/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState 30 0 R
/XObject <<
/X4 31 0 R
>>
>>
/MediaBox [0.0 7.920007 1440.0 817.92]
/Contents 32 0 R
/StructParents 1
/Tabs /S
/Parent 2 0 R
/BleedBox [0.0 7.920007 1440.0 817.92]
/TrimBox [0.0 7.920007 1440.0 817.92]
/CropBox [0.0 7.920007 1440.0 817.92]
/Rotate 0
/Annots []
>>
endobj
9 0 obj
<<
/Type /Page
/Resources <<
/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState 33 0 R
/XObject <<
/X4 34 0 R
>>
>>
/MediaBox [0.0 7.920007 1440.0 817.92]
/Contents 35 0 R
/StructParents 2
/Tabs /S
/Parent 2 0 R
/BleedBox [0.0 7.920007 1440.0 817.92]
/TrimBox [0.0 7.920007 1440.0 817.92]
/CropBox [0.0 7.920007 1440.0 817.92]
/Rotate 0
/Annots []
>>
endobj
10 0 obj

<!-- [truncated middle: 1840 lines omitted] -->

�ݪU�0a1���x���L/@%�%���ja�ر�Ts���лw���R�p��HJJW4h� HL#|c$����#G"S��
�W�
�b�ƍg̘�r�o@�P9���۷o�ޯ) �/Nj����P]QQ$c�ȑ
��=OCCC���1x
~�-//��
�����ի�f�jݺ5��3=����
���Ν;���p�	�/�RVVv��a>�9����t���Nqk���2��7o��ǰ��6�����}�
���� �	ضm�H�����
��Φ�#
�|��6111ӦM#(����������RH�1W'S���6�_�5�� 7]��ǜ�b�O�`	��t�R��������@�~�>���������/��"==}ݺuG�
���)**����*��1t�P]]]ZZ��_��ӧ��w�m�6t�#	��x��={��ׯo߾�k@߾}�u���w߁۔?���~������{��ݷo�~��o߾}��IHH���%<�p��

�/�������S�c�>���'N��۷���4%$$���7>>>%%��`0�����=z�В���������\C��/��ٳgs���ڵ+CCtѶmۙ3g���BTVV.]��gϞZm�֭����y�
�
��K�.�1"**��عs�K�B莪�s��ߴ��^�z���3;�C��ݗ/_nIu0P�-�޽{BBB�޽{O�2����͛7�O�>P8�����cΜ9&�/d��9s�̐!CZ�j�*f���g�}�x�b��`֚�=���[�`fa#�������b�T�
���l={��ݻ7��x�799�����AFc�%�� ��ݻwJJ�ݻwk�����`G+npV=u���_ݹsg�L�*DXXX�nݦM�v�
��%�<�����X�޽{
�\KJ6�u��Æ
;}�4*-����K�_ >��ǂ
�t���QҦM��ӧ3gGUUղe�gG׮]O�>��Y
�
�5���
�:�|bb�L�vUt��i����O1����_s����ڵ�,]�r��W.��
����H������������ ??���������())C5^,�fB�'p�z�H�_�(�������w�:���8??���������ZCS���d[� =�z�������]p:Ch�y
������B��
��ꎡ�At�^oQQ#l^���L�_|3*((В�Z~�2���|^^ޕ+W6o�<hР��h�������'�L�<�����8�

��{<
Օ2�!�A �����333��۷z��m۶�������o�_��9��a���
�.,
 R�͠� �k,**���Ǿ�
x<
�ߌ�_&2���{��ѱc�fΜٱc���pȄ���7m�4%%e�ҥ�O��@+Dy��eee0
���<����%%%�
C6�ag�:C�!���*//����݃9��p��sɬ���=
pÁ��N�N�?B�*Z�=�_�|����ܹsʔ)�{�nԨ�0����={Μ9sǎ
W�^�/$S �;x�x��_QQq�Ν������A�t���.ٽ{�9s�
?~

Q������0���hv�����￯_�>%%�iӦ!!!�����
```


### File: `extra advertage\Dir2md__The_AI_Code_Blueprint.mp4`

```mp4
   ftypmp42    isommp42 ��moov   lmvhd              � Y)                                            @                                �}trak   \tkhd                   WZ                                              @      �    �mdia    mdhd              0  A� U�     Ghdlr        vide            ISO Media file produced by Google Inc.   ��minf   $dinf   
dref          
url      �jstbl   �stsd          �avc1                        � H   H                                        ��   4avcCd �� 
gd ���-�
P      �<`ʀ h�<�   stts          �      4stsc             
         
     �        
 stco      � �� � �� � ? )� 2 N� k- �i �� �K z� �A �� �� �E = r ;� W� r� �� 
l� 
�d 
�� 
�M 
ݮ 
�. 
i 
*/ 
E( 
_� 
y� 
o7 V� ou ns �Z ֡ �� �. �R 
� $~ ?7 'Q � 
� =W W� q� g! � �� �� � � �� �P �7 �M �8 � 	c $6 ?
 Y� u� U� )� �{ !� D2 \� 
w� 
�� 
�r 
� 
�5 
�f 
� � !� E� a {�  �
  ��  ��  �> !� "M #)[ #B) #c� #~� #�� #�� $�� $�� %& %,� %G
 &Tv '[F 'to '�j '�> '� (�o )
 )$� )>� )Z )tk +j  +�� +� +�Z +�" +�� -� --� -�� -� -�� .N2 .�� .�" .�� .�� /� /.� /�1 /�� /�( /� 0
@ 0w0 0�� 0�� 1& 1,Z 1D� 1�� 1ֺ 1�� 2* 3^  3� 4T
 4nV 4�� 4�� 4�[ 4�< 5�R 5�8 6] 66� 6P� 7
 7� 8b 8!q 8;� 8U� 9BL 9]� 9v� 9�H 9�N 9�� :�� ;b� ;{` ;�< ;� ;ϐ <�� <׺ <� =	� = T =7� >�
 >�� >�@ ?� AZ� A� A�n A�` A�� CQ� Cl� C� D� D�� E0 E)� EE\ F�
 F� G3� GNZ Gg� G�� Hʾ J
_ J&� JL� Jg J�M K�` L� L/= LJ Ld� M�� O_v O�g P� P8: PSp Pn Q�� Q�* Rq R33 RM� S]� T|  T�� T� Tւ T�
 V7� VS� Vm� V�{ V�
 V�g X�
 X�  Y
 Y:� YU� Yq Z�) Z�� [� [,
 [F \d� ]�T ]�� ]�C ]�M ]�
 ^	 _W� _q� _�� _�
 _�Q a2( a�
 a�K a�� b b'� b�C b�> b�2 c6 c&� c=� d6� dL� dc( d d�n d� eK� eb� ez� e�� e�A f8 f�� f�� f�� g
� g"� g�K g�I g�F h
� h"y i�� i�� j�� j�r j�� j�y j� k�� l l.; lG� laA l{ n@G nX2 nt� n�� n�� n�> o�> o�� p� p p0� q � rO r
� r;E rS� rmF swT s�� s�� s�� s�% s� t� u�� u�p u�� v� w\! w�X w�� wѳ w�( x� x�G yЮ y�d z� z!� z:; zRx {X� {pQ {� {�� {�# |�X }{� }�� }� }�� }�_ ~�a  )� Ai X� p� �� �1� �I; �h� ��� ��7 ��X ��w ��O ��b ��} ��� ��� ��t ��� �� �)& �B" �Eh �]< �t� ��� �n� �c� �G> �]� �~ ��* ��I ��
 ��_ ��o �h � � �9 �� �� �({ �X8 �o� ��g ��� ��� ��� �� �� ��� ��\ ��� ��M �
{ �$� �3� �K� �c3 �z� ��� ��� ��� ��� ��� ��C ��� ��= ��g ��� �� �� �� �3 ��� ��E �� �$@ �<. �T� �SL �k� ��� ��� ��4 ��� �i
 �� ��� ��� ��� ��A �� � � �
 �/� �G@ �'� ��� �� �4 �KP �c� �^� �u
 ��� ��+ ��: ��� �s� ��� ��M ��� ��
 ��n ��. �� �
� �6Q �M� ��� �0� �G� �n� ��� ��� �GB �_k �w� ��� ��Y ��u ��� ��3 �� �$� �<V �S� ��
 �
 �L9 �� ��� ��� ��~ ��
 � � �>n �Z� �w� ��^ ��� ��� � �46 � ��X ��� ��� ��y �} �Z% �td ��� ��� ��: ��� �� �!O �:$ �^� �x� �� ��< ��v �� �.k �Hp �q? ��� ��F �α ��� � �F� �i ��r �� ��� �j ��$ ¨� ��� ��� �� � � �aA �|n Ęh Ĳ^ ��& ��P �~ �
 �:� �Xp �s� ǏZ ��
 �� ��� � �1� �OJ �g[ ˀ+ ˢ� ˾� ��4 � �/� �H� �b# �|� ͗G δ_ ��� ��� �b �#� �?� �|� і ѯ� ��� ��U ��� �� �� �{� ՟a ո� �� �� �
H �5 �Y� �s[ ؍� ٪
 ��� ��  ��h �6 �T� �l� ۃ ۙ� ۰F ��� ��2 ��� �� �5� �M� �eS �� �8 �.$ �H �_z ��6 �8� �Pe �k� ��� ��� �� �,c �B� �Z6 �q� �
 ��
 � �I� �s� ㎭ 㩴 �p� �l �q ��F ��o �� �j+ � �� �" �ω ��p ��p ��� ��� �
� �&� �� �� ��R �� ��� �� ��c �	� �"c �9� 짽 ��� �� �� �-� �S �p~ �� �x ��� ��+ �� �/� �J� �P( �k? �� �� �� �� �� �^� ��- ��P ��� ��l ��7 ��o �� �+S �G �s� ��� ��� ��� ��� �
J �� ��� ��B �� �1� �N �{� ��F ��' ��b ��I ��k �� � ��� :;h7�O�h����J�}c�|����p�|�6�
� q9�S���	1%��	x!	�S
Al
]�  �Xstsz           �  �I  �   U   �      �  �  �  Q  F  �   �   �   �   �  �  I   �   �   U   P   L   L  �  
  �   �   x   q   v   e     q   �   o   w   d   y   h   t   d   w   g   p   d   |   e   �   h   t   \   _   U   c   V   `   R   c   [  �L  �  \  
   �   �   �   �   �   y   �   ~   �   {   �   ~   �   {   �   ~   �   z   �   �   �   {   �   ~   �   {   �   ~   �   {   �   ~   �   z   �   ~   �   {   �   ~   �   z   �   ~   �   z   �   }   �   v   �   }   �   y   �   |  �o  �  
   �   �   �   �   �  �%  �   �   }   c   _   l   X   T   O   X   S   T   O   X   S   [   M   V   S   R   O   V   S  �  ]  $   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �  �Y  �  .   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �      �   |   �      �   |   �   ~   �   ~   �   �   �   {   �   ~   �   �   �   �  Վ  �  i  �     }   [   `  �c  �   �   K   �   n   @   >   <   <   :   <   :   <   :   <   E   <   :   <   :   <   :   <  �  `   �   �   l   q   l   q   �   �   |   q   l   q   l   q   l   q   l   q   l   q   l   q   ~   �   l   q   l   q   l   q   l   q   l   q  ��  n     �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �  ��  �  �   �   �   �   ~   �  �0  �   �   w   M   L   K   L   L   L   K   L   _   P   `   d   c   q   �   [   �   X   �  ��  %�    �  �  
�  �    C  E  �  �  j   �   �   �   �   �   v   �   t   x   r   x   r   �   �   n   o   t   o   t   o   w   r   v   o  ��  �  w   �   �   �   W   ]   _   ^   W   Z   W   Z   Z   Z   W   [   W   n   `   `   V   _   b   \   W   Z   W   Z   Z   Z   W   Z   Q   T   `   d   V   Z   R   Z   P   Z   R   ]   P   \   W   `   M   S   �   �   �   }  ,  J  z    �  �  T   �   i   �   D   :  ��  Q  :     c   _   V   V   V   U   U   U   U   U   U   U   r   e   S   V   V   V   V   V  
  �   �   �               �   �   ~   z   z   z   z   z   z   z   z   z   �   ~   z   z   �   �   z   z   z   z   z   z   z   z   z   z  ��  R     �   �   u   `   `   `   `   `   `   `   `   `   `   `   `   `   `   �   r   `   `   `   `   `   `   `   `   `   `   `   `   `   `   |   s   `   `   h   h   k   g   g   g   g   g   g   g   g   g   |   r   Z   Z   Z   Z   Z   Z  ��  �  	   �   c   X   R   F  ��  �  p   �   e   V   T   T   T   T   T   T   T   T   T   T   p   c   T   T   T   T   T   T  �  �   �   |   u   u   t   s   �   �   �   s   t   s   t   s   t   s   t   s   t   s   t   s   �   �   p   s   t   s   t   s   t   s   t   s  �:  �   �   �   �      p   p   p   p   p   p   p   p   p   p   p   p   p   p   �   �   p   p   p   p   p   p   p   p   p   p   p   p   p   p   �   �   p   x   w   z   w   w   w   w   w   w   w   v  ~   |   �   �   m   l   l   �   i   �  �4  S  �   �   p   p   i   J  �4  �  m   �   x   V   O   M   N   Q   l   m   c   Z   n   s  �  ��  �     t  �  M  �  T  �  0  h  +   �   m   k  �  c  ?   �   i   E   J   F   @   @   @   @   @   @   @   @   F   L   G   @   @   @   @   @   @   @   @   @  ��    p   �   �   {   t   p   q   t   q   r   t   o   q   r   t   o   q   r      r   t   p   q   j   i   n   k   g   i   j   k   g   i   f   j   h   j   d   f   d   f   l   i   d   f   g   i   a   c   i   o   i   h   a   g   e   f   h  �g  �  ?   �   |   {      \  �  .  (   �   Z   K   F   D   F   G   F   D   F   G   F   D   V   D   F   G   F   G   F   D  �  �   �   �   �   t   v   x   �   {   z   t   v   t   v   x   z   t   v   x   z   t   v   x   }   {   z   t   v   t   v   x   z   t   v   x :  j     �   �   ~   o   m   l   k   l   n   o   k   l   s   r   k   l   n   ~   n   o   m   l   k   l   n   o   k   l   r   o   k   o   n   w   n   o   m   l   n   o   r  	\     �   a      [   g   �  �   �   �   x   _   _   _   _  �  �  (   �   \   S   X   K  �  �   �   y   P   H   H   H   H   H   H   H   H   H   H   K   �   G   B   F   E   F   E   F  �  
   �   �   p   n   n   n   �   r   n   n   n   n   n   n   n   n   n   n   n   n   n   n   �   r   l   l   l   l   l   l   l   l   l   l f  �  a   �   �   r   n   n   o   n   o   n   o   n   o   n   o   n   o   n   �   o   n   n   o   n   o   n   o   n   o   n   o   n   o   n   �   o   n   n   o   n   o   n   z   p   m   k   m   k   m   l   x   m   l   l   m   k   k   i  �y  X     �   �   e   h   v  �  �   �   y   P   H   H   H   H   H   H   H   H   H   H   H   �   G   B   F   E   F   E   F  �  
   �   �   p   n   n   n   �   r   n   n   n   n   n   n   n   n   n   n   n   n   n   n   �   r   l   l   l   l   l   l   l   l   l   l �  �  =   �   �   i   g   g   g   g   g   g   g   g   g   g   g   g   g   g   x   i   g   g   g   g   g   g   g   g   g   g   g   g   g   g   �   i  `   t   e   e   e   o   o   }   b   b   �   h   d   d   t   f   i   d   p   j   c   c  �  Z     �   �   j   i   x  �  a   �   l   Q   H   H   H   H   H   H   H   H   H   H   H   ^   L   J   J   J   J   J   J  �  Q   �      t   t   t   t   �   v   l   l   l   l   l   l   l   l   l   l   l   l   l   l   �   r   l   g   �   f   f   f   f   i   a   e  �v  �  "   �   �   v   m   m   m   m   m   m   m   m   m   p   q   s   U   T  Z  [S  O  �  0  �  �  t  E   O     �   N   W   X   +  �  ]   �   B   1   0   7   ,   /   /   1   /   1   /   1   /   1   -   -   -   -   -   -   ,  P�   R   7   3   /   -   .   -  Q�   `   9   -   ,   -   ,   -   ,   -   ,   -   ,   -   ,   -   -   -   ,   -   ,   -   ,   -  .   �   >   0   3   0   3   0   �   @   =   0   3   0   3   0   3   0   3   0   3   0   3   0   9   0   3   G   /   ,   /   ,   /   ,   /   ,  c�   /   =   6   8   5   -   +   -   +   -   +   -   +   -   +   -   +   -   +   4   2   -   +   -   +   -   +   -   ,   .   ,   K   '   +   ,   �   Z   �   '   R   &   &   &   &   &   &   &   (   &   &   &   5   3   &   &   &   &   &   &  U=   H   p   &   &   &   &   ,  R~   ?   &   &   &   &   &   &   &   &   &   &   &   &   &   &   /   /   &   &   &   &   &   &  �   �     C   >   8   8   8   P   J   8   8   8   8   8   8   8   8   8   8   8   6   6   6   A   9   6   6   6   6   6   6   3   +   +   +  c�   7   2   0   J   >   0   +   +   +   +   +   +   +   .   .   .   .   .   .   ?   :   /   /   /   /   ,   &   &   &   &   &   0   )   )   %   �  ��    8  i  
u  	u  
8  �  Y  g    �      �   �  �  J  \   �   �   �   �   �   �   �   �   �   ~   w   e   ]  �
  ~   �   x   S   b   P   [   P   Y   P   ]   U   ]   U   ]   ]   ^   U   Y   P   Y   P   Y  �  ]   �   �   �   �   z   �   �   �   �   ~   y   |   x   t   s   x   o   n   h   u   o   n   q   �   �   �   m   y   t   k   f   v   p   k  ��  �  !   �   �   �   �   �   �   x   ~   x      y   }   w   }   w   {   u   �   �   �   w   �   �  �    5   �   n   X   �   Z   R   �  e   �   �   t   t   ^   `   R   U   b   S   X   U   S   S   S   P   K   K   K   K   K   M   K  �&    k   o   V   >   =   5  ��  �   �   Y   R   9   7   5   5   5   5   5   5   5   5   5   F   8   5   5   5   5   5   5  �  �   �   �   �   |   |   �   �   �   |   |   �   }   |   |   |   |   |   |   |   |   |   |   �   �   |   |   |   |   |   |   |   z   y   v  �
  �   �   `   i   R   P   N   P   N   P   N   P   N   P   N   P   N   P   N   S   R   P   N   P   N   P   N   P   N   P   N   P   N   P   R   W   W   O   H   H   H   H   K   H   I   I   I   M   M   M   L   J   J   G   B   B   G   B   B  ��  �  C   �   O   7   <   ;  �  �   �   K   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   D   ?   ;   7   7   7   7   7  v  	   �   t   b   b   b   b   l   e   b   e   b   b   b   b   b   b   b   b   b   b   b      j   i   f   f   f   f   f   f   f   f   f   f  ��  �   �   R   J   ?   9   A   9   9   9   9   9   9   9   9   9   9   9   ?   �   C   @   7   <   7   =   7   7   V   9   9   9   9   9   9   A   A   =   >   :   6   9   6   6   6   ;   ;   ;   ;   :   9   B   C   =   7   4   2   2   7  �(  �  e   ]   H   =   A   G  �e  �   �   U   >   6   >   4   4   4   4   :   4   5   1   1   G   K   8   =   >   @   X   V  '   �   �   �   �   �   ]   �  o   �   �   V g�  �  $  &�  "  �  �  �  �  �  
U  f  �  s  �  K   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   n   ~   x   �   x   �   x   �   �   �   �   �   � F%  �  �  +   �   �   �   {   {   k   x   k   u   k   u   j   �   v   n   b   n  W   �   q   s   i   k   Z   _   R   H   H (b     �   �   b   V   T   O   T   O   T   O   T   O   T   O   q   c   T   O   T   O   T   O  	m     �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � V?  B  �   �   �   �   �   �   �   �   �   �   �   �  $*  t  Z  �   �   �  
3  �  �   �   �  9   }   q   l   l   l   l   l   l   l   v   �   ~   k   k   f   f   f   f   f   l   f   f   m   ]   Z   Z   V   f   c   a   a   U   U   U )  �  �  E   _   Q   N   B %P  �  �   �   \   G   G   G   G   G   G   G   G   G   G   G   I   G   G   G   G   G   G   G    �  W   �   j   j   e   e   n   m   o   j   j   j   j   j   j   j   j   j   j   j   e   d   e   d   i   i   i   i   i   i   i   i   i   i U�  �  l   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   {   {   {   z   z   u   u   u   }   u   u   u   u   u   u   u   u   u   u   u   u   u   m   m   m   c   M   J   J   J   W   W -  q  �   �   u   �   i   j  �5     �  �8  �  �  
  1  `  e  C  �  �  
  F  *  	q  �  P  �  '   �   �   �  �  4  9  %  )   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � e  �  �  9  �  H   �   y  %  �  ?   �   �   �   �  �   z   �  8   �  2  �   �   �   �   x   ~   k   l   k   l   k   l   k   o   n   w   k   s   x   w   t   t   w   t   r   q   o   }   h   n   e   s   h   i   x   `   ^   [   X  �_  8  H   �   l   Q   M   H  �  �  $   �   m   l   k   j   k   o   k   j   k   j   k   g   �   j   k   j   k   j   p   j  p  �   �   �      }   p   n   r   j   l   j   l   j   l   j   l   j   l   j   l   j   l   j   k   j   l   j   l   j   l   j   l   j   l   j &O  P  3   �   �   �   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   s   u   o   o   l   l   l   n   q   k   k   k   n   j   j   l !  >  �   �   x   z   p   `  �    .   �   i   a   a   a   a   a   a   a   a   a   a   ]   �   e   a   a   a   a   a   a  @  �     �   �   |   ~   |   �   |   ~      ~   |   ~   |   ~   |   ~   |   ~   |   ~   |   �   |   x   y   x   u   x   u   x   u      | $:  �  
  |  
l  j  #   p   f   �   k   i  -   j   r   j   j   j   j   j   �   �   o   k   k   k   k   k   ~   h   m   h   h   h   q   i   m   q   i   f   e   f   f   f   \   \   f   k   e   a   f   c   g   j   e   e   e   e   e   [  �  �  9   �   �   p   u   L �  6  :   d   D   D   D   D   D   D   D   D   D   D   D   D   N   D   D   D   D   D   D   D  �  �   �   �   w   m   k   k   �   l   u   p   c   c   c   c   c   c   c   c   c   c   c   c   k   f   ~   e   c   c   c   c   c   c   c   c &[  �  �   �   �   v   v   w   v   v   v   v   v   v   v   v   v   v   v   v   v   v   v   v   v   v   v   �   v   v   v   v   v   v   v   v   v   v   v   v   u   u   u   u   u   u   u   �   r   v   v   v   u   u   u   {   {   u   t   t  ��  �   �   N  \r  �     �  n�   �   M   +   +   N   2   2   2   2   2   2   2   1   1   1   O   6   ;   .   (   (   (   (  
:  �   h   A   /   /   )   )   R   3   D   )   )   )   )   )   )   )   )   )   )   )   )   )   @   3   B   )   )   )   )   )   m   U   1   +  �c   +   8   *  ~   �   ,   �   7   5   5   5   5   5   5   5   5   5   5   5   6   3   3   3   3   3   3   3   1   1   .   +   +   O   (   &   &   &   +   &   .   .   )   &   &   &   &   &   &   )   &   &   &   &   &   &   &   &   &   &  rj   [   B   ,   &   &   *   &  n�   S   )   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  i  �   b   ?   k   /   )   )   )   /   ,   )   )   )   )   )   )   )   )   )   )   )   )   )   )   )   )   )   )   a   &   &   &   &   &   &  ��   2   8   5   )   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   ,   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  v�   ]   �   .   &   &   &   &  oQ   l   )   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  o  5   �   D   >   '   ,   )   3   ,   )   )   )   )   )   )   )   )   )   )   )   )   )   )   �   3   �   @   -   3   )   )   )   )   )   )  ��   5   6   '  %     l   =   2   a   E   )   '   '   '   '   '   '   '   '   @   ;   &   )   &   &   &   &   &   &   *   &   &   &   &   &   6   4   &   &   )   .   ,   0   )   5  �|  
�  ;  V  �  h  ?  �   n  �   �   �   m   e   [   T   M   C   =   6   8   &  �N   �   5   /   *   .   *   .   *   .   *   .   *   .   *   .   ,   1   *   .   *   .   *   .  �  `   �   i   �   �   V   @   a  1   i   N   �   R   S   O   `   R   V   T   _   k   k   `   �   {   Z   R   ^   U   �   R   P   �     o  �J  �   �     �   �   �      d   f   a   f   a   f   a   f   ]   f   ]   f   l   v   l   g   [   f   [   f   [   [   [   Y   V   T   V   T   [   Y   V   T   V   W   V   T   V   T   S   T   S   U   V   U   Z   Y   S   S   U   S   W   T  �Q    �   �   k   p   X   U  ̾   �   5   /   *   .   *   .   *   .   *   .   *   .   *   .   ,   1   *   .   *   .   *   .  b  �   �   �   }   I   T  '   [   b   �   I   F   B   U   e   M   T   b   {  �  �   �   H  
T  -   t   W   L   :   3   7   7   7   3   .  ��  �   [   y   :   +   &   &   &   &   &   &   +   &   &   &   &   &   &   &   &   +   &   &   &   &   &   &   +   &   &   &   &   &   &   &   &   +   &   &   &   &   -   -   -   -   -   -   -   -   -   G   -   -   /   0   0   ,   ,   ,  ր    0   Y   5   P   &   .  �w   �   ,   &   &   *   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  �  [  x   S   /   ,   :   .   4   3   z   :   .   .   L   .   :   k   3   3   C   <   7   a   7   7  b   �   K   4   :   <   s   �  ;   �  �L  �   �   X   ?   .   5   .   .   4   .   .   5   5   5   5   .   .   .   .   .   4   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   6   &   &   &   &   &   &   &   &   ,   ,   ,   ,   ,   ,   6   ,   ,   ,   /   /   /   -  ��    A   �   ;   <   =   /  ��   �   &   &   &   *   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   %  �  �   b   N   J   I   /   .   4   6   �   6   h   <   a   L   B   P   \   O   3   P   9   1  
   D  �M  ]  
�  C  �  u  P  �     �  �  y  9   �  {  $  
   �   �   �   `   Q   d   O   P   O   P   O   P   O   W   K   B   =   5   8   8   8   8   8   4   4   1   1   1   5   B   =   8   ;   =   :   8   8   8   8   4   4   4   1  �&   n   �   t   H   A   :   ;   8   @   <   6   2   0   +   '   '   '  ��   {   0   (   .   '   '   '   '   '   '   '   '   '   '   '   +   '   '   '   '   '   '   '  �  �  �   �   �   Y   A   @   `   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   A   ;   ;   ;  �
   �   m   d   ]   N   C   B   C   B   C   B   C   B   C   B   C   B   C   B   G   B   C   B   C   B   C   B   C   H   F   F   B   C   B   C   B   @   9   4   4   7   5   4   5   5   4   4   4   4   2   2   6   .   .   .   .   .   /   *  �Q   �   �   �   P   J   J   *  �   ~   /   '   '   '   '   '   '   '   '   '   '   '   '   '   +   '   '   '   '   '   '   '  �  #  t   �   y   b   �   �  g  3   �   m   K   H   D   E   E   E   I   E   E   E   E   E   S   C   E   E   E   E   E   E   E   E   E   E  �   �   S   *   '   '   *   *   *   *   *   *   *   *   *   *   *   *   *   *   '   '   *   *   *   *   *   *   *   *   *   *   +   *   +   *   '   '   +   *   +   *   +   +   +   +   +   +   +   +   *   *   '   '   *   +   +   +   +   +  �l   �   �   K   :   2   '   '  �>   �   0   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +  �  |   ]   �   K   K   K   K   K   K   K   K   K   K   K   K   K   Y   K   K   K   K   K   K   K   K   �   �   H   H   H   H   H   H   H   H  ��   �   T   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   *   '   *   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  ��   �   �   R   0   3   '   '  Ĕ   �   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  �  �   x   H   p   =   =   =   W   =   =   =   =   =   =   =   =   =   =   =   >   =   =   =   =   =   =   =   =   =   =   =   =   =   =   =  ��   �   W   7   0   0   0   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   ,   3   0   ,   ,   +   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   +   '   '   '  �    �  ;  �  �  
  �   �   �   h   F   L   J  ܖ   �   �   [   :   9   .   .  �i   �   <   0   +   +   +   +   +   +   +   +   +   +   +   +   +   .   +   +   +   +   +   +  D  %   \   �   D   8   8   8   8   A   C   8   8   8   8   8   8   8   8   8   8   8   8   8   8   >   >   8   8   8   =   ;   ;   E   ;   ;  ��   �   X   l   o   [   U   T   S   P   O   N   N   I   I   I   I   I   I   I   V   I   N   I   I   I   I   I   F   F   F   E   F   B   <   <   L   E   C   <   >   >   >   >   =   =   >   <   >   ;   9   9   D   =   <   :   <   <   <   6  �P   �  
   I   8   8   3   3  �]   �   <   +   +   +   +   +   +   +   +   +   +   +   +   +   +   .   '   '   <   2   *   *  	�  �   j     J   =   =   =  �  )     a   =   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9  ��   �   n   /   8   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *  ��   �   �   8   *   '   '   '  ��   �   7   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  �  j  "   T   >   7   7   7   =   4   7   7   7   7   7   :   :   :   :   :   :   :   :   :   7   7   :   :   :   :   :   :   :   :   :   :  ��   �   X   3   4   +   ,   +   +   +   +   +   +   +   +   +   +   +   +   +   ;   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   +   *   '   '   '   '   '   '   '   '   '   '  ۺ   k  [   5   *   '   '   '  �~   �   >   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  =  0   R   I   3   6   3   =   =   5   7   5   5   8   4   ,   K   +   0   N   >   +   +   '     �  ��  �  G  
N  V  
  �  u   �  2  ��   �   U   t  .  `   �   �   k   O   y   B   f   B   ?   B   ?   B   ?   B   g   B   ?   B   ?   B   ?   B   ?   B   ?   ?   ;   5   6   3   .   3   3   .   .   1   1   7   1   6   /   /   :   6   1   6   8   .   *   *   1   *   *   *  ��   �   �   E   3   .   +   '  ��   }   )   )   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  %  ^   �   K   {   ~   6   :   8   M   3   A   3   5   3   D   3   E   8   D   3   <   `   >   3   J   [   f   3   5   8   E   3   9   3   f  �   �   U   n   M   =   8   8   8   8   8   8   8   8   8   8   8   8   8   8   ;   8   8   8   8   8   8   8   8   E   I   C   C   <   2   2   6   +   +   +   +   +   2   '   '   '   '   '   '   '   '   *   *   *   *   *   *   *   *   *  ̋   �   s   B   )   *   +   '  ��   d   )   '   '   '   '   .   8   /   +   .   '   '   '   '   ^   3   '   '   '   '   '   '  �  O   �   �   =   <   5   5   ;   8   5   5   5   5   5   5   5   5   5   5   5   5   5   5   8   8   5   5   5   5   5   5   5   5   5   5  ��   �   W   '   L   7   -   '   '   '   '   '   '   '   '   '   '   '   '   '   7   7   '   '   '   '   '   '   '   '   '   '   '   '   '   '   7   7   '   '   '   '   '   '   '   '   '   '   '   '   '   '   0   0   '   '   '   '   '   '  ��   �   �   C   ;   3   )   )  �Y   �   3   '   '   '   '   '   '   '   '   '   '   '   '   '   *   +   '   '   '   '   '   '  )  �    D   A   2   ,   '   4   ,   '   '   +   -   '   '   '   +   -   '   -   '   '   '   �   O   �   '   '   '   '   '   '   '   '   '  �4   �   L   1   7   4   .   .   .   .   .   .   .   .   .   .   .   .   .   .   4   4   .   .   .   .   .   .   .   .   .   .   .   .   .   .   4   4   .   .   .   .   .   *   *   *   *   *   *   *   *   *   3   -   *   *   '   '   '   '  �&   �   �   F   9   1   '   '  �,   �   *   '   '   '   '   '   '   -   *   '   '   '   '   '   .   +   '   '   '   '   '   '  &  �  r   M   *   +   '   '   /   0   -   '   '   -   '   '   '   ,   '   '   '   '   '   '   :   1   '   '   '   '   '   '   '   '   '   '  �   �   T   5   :   8   -   -   -   -   -   -   -   -   -   -   -   -   -   -   7   8   -   -   *   *   *   *   *   *   *   *   *   *   *   *   /   1   *   *   *   *   *   *   *   *   *   *   *   *   *   *   -   -   '   '   '   '   '   '  �   �   z   '  rn  u  �  .  |�   n   \   (   &   3   )   &   &   6   &   &   &   &   &   &   _   V   -   ,   ,   ,   ,   ,  r  m   C   =   ,   ,   ,   ,   I   3   6   4   5   5   6   ,   ,   0   ,   5   6   ,   ,   ,   5   3   4   8   9   5   6   ,   ,   ,   ,   ,  ��   >   l   H   W   ?   @   8   7   8   7   8   7   8   7   8   7   8   7   8   ?   >   4   6   4   6   4   6   4   6   4   6   4   6   0   1   >   :   0   /   0   /   0   0   /   0   /   0   /   0   /   0   /   0   /   0   .   /   .   ,  �8   b   �   A   8   )   &   &  *   B   .   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  �  ~   t   �   A   :   :   5   A   1   1   1   1   1   .   .   -   0   .   :   .   /   (   (   (   (   (   (   &   0   ,   -   -   0   /   .  ��   0   3   +   )   +   &   (   &   (   &   '   &   &   -   &   %   ' *  �  D�  9�  *  
�  ?  �  )  �      @  �  1   �   �   �  
  �  )  G  
   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � >  �    �   �   �   �   z �      �   z   c   _   \   `   ^   ^   \   ^   ^   ^   \   ^   h   a   \   ^   ^   ^   \   ^  �  
  C     �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � $h  ?  �  �  '  ,   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �  #?  �  ��  .  =   �   z   �   _   C i     �   �   H   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   N   ?   ?   ?   ?   ?   ?   F  �  �   �   �   r   f   i   i   �   o   i   i   i   i   i   i   i   i   i   i   i   i   i   i   p   m   i   i   i   i   i   i   i   i   i   i *�  B  X   �   �   z   t   r   r   r   r   r   r   r   r   r   r   r   r   r   y   y   r   r   r   r   r   r   f   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   e   Z   X   X   X   X   X   Z   V   Z   Z   Z   Y   \   \   \ r  *  �   �   |   m   i   k i     �   �   H   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   ?   N   ?   ?   ?   ?   ?   ?   ?  �  �   �   �   r   f   i   i   �   o   i   i   i   i   i   i   i   i   i   i   i   i   i   i   p   m   i   i   i   i   i   i   i   i   i   i *�  B  X   �   �   z   t   r   r   r   r   r   r   r   r   r   r   r   r   r   y   y   r   r   r   r   r   r   f   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   e   Z   X   _   [   ]   [   Z  �   a   g   V   U   U   U   w �  �  �   �   p   p   g   Y g  �     z   j   Q   Q   Q   Q   Q   Q   Q   Q   Q   Q   Q   Z   Q   Q   Q   Q   Q   Q   Q  �  i   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � )�  }  /   �   �   �   t   t   t   t   t   p   i   i   i   i   i   i   i   i   p   i   i   v   i   i   i   i   i   i   n   i   i   i   i   i   q   i   n   i   s   r   v   k   c   x   l   h   q   |  �  p  }  (  �  �  �  2   �  -  �  �  
   �   �   z   x   o  �  \   �   r   V   W   T   T   T   T   U   S   S   S   S   S   a   Z   J   W   S   S   S   S  �  �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � 
9  .  �   �   �   �   s   �   �   �   �   �   �   �   �   �   �   �   �   �   z   �   q   �   �   �   �   �   �   �   �   �   �   �   �   �   u   �   u   �   �   �   �   �   u   t  �  O   �   m   r   s  �   �   �   o   �   g   c   a  ��  �  7   �   �   {   w   G  ��  '   �   �   I   M   I   M   I   M   I   M   I   M   I   M   T   M   I   M   I   M   I   M  R  �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � �  M  k   �   �   _   W   U   U   U   U   U   U   U   U   U   U   U   U   U   Y   U   U   U   U   U   U   U   U   U   U   U   U   U   U   U   Y   U   U   U   U   U   Y   U   U   U   \   Y   Y   ]   X   X   Z   U   U   P   P   P   P   O  ��  ]  �   �   o   l   k   T  ��  N   �   `   I   I   I   I   I   I   I   I   I   I   I   I   U   I   I   I   I   I   I   I    �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � 
  7     �   �   �   n   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   h   m   h   h   d   _   b   _   d  R   o   _   _   _   _   _   �   c   ]   �   k   `   c   `   f   _   _   _   ^  �2  _      �   {   x      S  ��  '   �   �   I   M   I   M   I   M   I   M   I   M   I   M   T   M   I   M   I   M   I   M  R  �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � �  M  k   �   �   _   W   U   U   U   U   U   U   U   U   U   U   U   U   U   Y   U   U   U   U   U   U   U   U   U   U   U   U   U   U   U   Y   U   U   U   U   U   Y   U   U   U   \   Y   Y   ]   X   X   Z   U   U   P   P   P   P   O  ��  ]  �   �   o   l   k   T  �I  �   �   e   O   Q   ]   I   Z   i   M   T   )  �f  �  �  �  	  ?  �    �  )  �  #r  M    �   �   f   T   d  t  �  �   �   y   o   k   j   j   j   j   j   j   i   i   f   w   x   r   m   j   j   j   j   j   j   j   j �   �   �   p   O   b   7   )   *   )   *   )   *   )   *   )   *   )   *   )   <   <   7   )   *   )   *   /   /   1   .   R   *   3  �  �  n     ^   @   B   K   ;   ;   D   ;   8   8  �   3   -   -   <   .   2   +   +   '   '   ' o   �   �   D   '   '   '   ' �  *   4   '   '   '   '   '   '   '   '   '   '   '   '   '   /   '   /   '   '   '   '   '  =  C   �   =   7   4   4   4   V   i   �   L   =   =   �   =   =   =   =   ?   w   =   C   =   D   =   H   =   U   I   B   A   �   Y   �   C (  �   �   :   B   -   C   *   *   *   *   *   *   *   *   *   *   *   *   *   8   -   7   *   *   *   *   *   *   *   *   *   *   *   *   *   6   -   6   *   '   '   '   '   '   '   '   '   '   '   '   '   1   '   6   *   '   '   '   ' �     �   =   >   +   '   '  �W   �   T   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  3  �   Z   4   4   4   4   4   E   '   3   .   '   '   '   '   '   '   K   7   4   *   '   '   E   M   B   -   /   f   M   X   6   )  k  F  �  �  �  �  �  �   �   �   I   O   @   [   D   A   D   �   B   5   @   &  �   �   �   a   (   *   )   *  *   �   F   .   +   Q   P   G  M   X   =   .   )   &   -   +   .   ,   ,   (   &   &   &   &   &   (   &   &   &   &  U�   u   �   *   *   &   &   *   &   )  T   G   *   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &    �   b   *   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '  f�   1   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   '   )   '   '   '   '   '   '   '   '   '   '   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &   &  Y�   O   b   )   8   ,   &   &  =L   l  ��  �  
8  ~  E  
�  
  0  p  �    =   �   �  \  =  �   �   �   b   N   O  	�    �  %   �   �   �   �   �   p   �   w   n   m   k   m   k   m   k   m   k   m   f   b   �   n   �   h   `   i   b   a   `   a   `   a  �~  �  �   �   �   �   �   l   h   b   h   b   h   c   i   e   l   l   k   `  :    �  1     �   {   �   t   �   �   x   �   �      y  '  �   �   t   m   f   v   j   j   j   j   j   j   l   f   f   u   j   o   v   x   q   o   k  ��  �  �   �   X   =   8   4  ��  �   �   C   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   E   ;   ;   ;   ;   ;   ;   ;  q  6   �   �   Z   P   T   P   _   P   ]   T   ^   T   W   X   [   X   [   X   `   Z   ]   Z   ]   Z   ]   Z   ]   Z   ]   Z   ]   Z   ]   Z  ��     �   P   Q   E   E   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   H   K   H   H   H   H   H   H   H   H   H   H   H   H   K   K   K   K   K   K   P   J   E   ;   ;   ;   ;   ;   ;   ;   :  ��  �   �   X   O   C   ?   W  �w    i   v   H   B   B   B   B   B   B   B   B   B   B   B   F   B   B   B   B   B   B   B  �  z   �   Q   L   L   L   L   L   L   N   L   c   L   N   L   N   L   N   L   N   L   N   L   L   L   S   L   N   L   N   L   N   �   N   e  ��  �   �   n   h   E   E   E   B   B   B   L   I   B   B   B   �   C   F   G   S   D   h   K   J   C   U   K   @   A   L   R   @   a   ]   x  �   �  �L  �    $�  !�  �  &  1  �  �  
>  �  �    �    
  c   �   �   �   �  �  v    �   �   f   U   p  �$  
  n   }   h   c   g   c   g   c   g   c   g   c   g   c   �   {   j   c   g   c   g   c  @  �  ]  N   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � 
�  0      3   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   }   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   w   s   �   �   u   �   t   r   m   o  �  �  �  2   �   �   �   u  ��  C  q   �   �   r   u   p   u   p   u   p   u   p   u   p   �   �   u   p   u   p   u   p  l  �     �   �   �   �   �     �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � 
�  �  �    �   �   �   �   �   �  %<  �  `  E   �   �   �  �   �   �  	�  �  T   �   �   �   �   �   �   �   �                  �   �         �   �   �   �   �   �   �   �   �   y   x   x   �   �   x   ~   �   w      ~  �  �  .     �   x   k   c  �    �   �   b   f   `   b   `   b   `   b   `   b   `   b   u   d   `   b   `   b   `   b  �     �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   � 
J  ,  f   �   �   �   k   j   e   e   k   e   l   d   k   y   �   ]   q   c      z   n   p   h   _   S   P   S   Y  ��  �  1  �  �  
%  �  �  _  
�  :  �   �  0   �   �   �   �   �   �   �   �  �  O   �   �   �   �   �   �  Ų  �    l   �   �   r   ]  ��  K     �   �   }   p   ]   \   `   `   \   a   \   a   ^   d   O   W   R   W   X   Y   X  G  �  P   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �  �p  P  1  
  )(    �   �   �   �   �   �   �   �  )   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �      �  ��  �  �   �   G   A   M   8  ��  ~  =   �   X   R   T   R   T   R   T   R   T   R   T   R   W   R   T   R   T   R   T   T  �  6   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �   �           ��  [  �   �   �   _   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   Y   S   S   S   S   S   S   S   S   S   S   S   S   S   S   W   S   S   S   R   R   R   R  Ɨ  n  `   �   v   d   o   d  Ū    �   �   V   S   J   J   J   J   J   J   O   J   J   J   T   J   J   J   J   J   J   J    u   �   x   s   s   s   s   �   u   s   s   u   s   s   s   s   s   s   s   s   s   s   x   x   y   w   w   w   w   w   {   s   p  �   o  ݈  �  &   ~   �     p   k   �   g   b   b   b   b   b   b   b   b   b   b   e   c   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   Z   ^   Z   Z   Z   Z   Z   Z   Y   f   ]   ]   ]   ]   ]   b   h   b   ^   ^   `   \   \   \  ��  <  �   �   b   W   a   _  ��  }   �   u   P   N   P   R   T   N   P   N   V   N   v   M   Z   K   M   K   X   M   K   E  �     �   k   \   S   W   R  �  o  �  
�  `    
�  

<!-- [truncated middle: 1840 lines omitted] -->

        (          N  Y  �   �   �     �   �  	    
       +    H  5   �   �            ?  #  /  D   �   �   �    
    1  :  &  
  %  &   �   �    "  $                                          #     %  "  $  !    B  !   �  
  	      	    (      
    =     
      4      "  G  H  D  3   �   �   �      	      
    k  
   �    
        
            !  !  #  *  
            +               	              *  $       3  l          	      
          )    	  0  
    
  !  R   �    '  
     '  S   �   �       
        <  i   �   �   �    	  '            1  
  	  	  
  
  !    9  m   �   �              
  ?                          g     �     n   �   �   �    
  T    
  
    %  	  x   �     	          p  8   �   �      T  )      G   �    "         V  
   �   �                   8  "  
  :      \   �   �  	        .  f   �          �      d  \   �   �   �    %  U   �   �   �  $   �     
  
    e  8   �   �   �    
      $    1    
              .  k   �    
  /            #    
  
        3      
        "  
  '                 ~     �    -  /         \   �   �   �    
  
    
      /      !     $  C  9    
  e   �       �  
    '    D  K   �   �     �    
```


### File: `patches\1.patch`

```patch
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -11,7 +11,7 @@
 license = {text = "MIT"}
 requires-python = ">=3.9"
-dependencies = ["pathspec>=0.12.0"]
+dependencies = ["pathspec>=0.12.0", "tomli>=2.0.0"]
 
 [project.scripts]
 dir2md = "dir2md.cli:main"
--- a/src/dir2md/cli.py
+++ b/src/dir2md/cli.py
@@ -1,9 +1,15 @@
 from __future__ import annotations
 import argparse, zipfile, hashlib, os
 from pathlib import Path
+try:
+    import tomli
+except ImportError:
+    tomli = None
+
 from .core import Config, generate_markdown_report
 from . import __version__
 
+
 # Load .env file if it exists (for Pro license and configuration)
 def load_env_file():
     # Try current directory first, then parent directories
@@ -19,6 +25,25 @@
             except Exception:
                 pass  # Silently ignore .env file errors
 
+def _load_pyproject_config() -> dict:
+    """Find and parse the [tool.dir2md] section of a pyproject.toml file."""
+    if not tomli:
+        return {}
+    
+    current_dir = Path.cwd()
+    for path in [current_dir] + list(current_dir.parents):
+        pyproject_path = path / "pyproject.toml"
+        if pyproject_path.exists():
+            try:
+                with open(pyproject_path, "rb") as f:
+                    config = tomli.load(f)
+                return config.get("tool", {}).get("dir2md", {})
+            except (tomli.TOMLDecodeError, OSError):
+                # Ignore errors in parsing the config file
+                return {}
+    return {}
+
 # Load environment configuration on import
 load_env_file()
 
@@ -37,60 +62,64 @@
     return iv
 
 def main(argv: list[str] | None = None) -> int:
+    # Load config from pyproject.toml
+    config_from_file = _load_pyproject_config()
+
     ap = argparse.ArgumentParser(prog="dir2md", description="Directory → Markdown exporter with LLM optimization")
+    
+    # Set defaults from the config file before parsing arguments
+    ap.set_defaults(**config_from_file)
+
     ap.add_argument("path", nargs="?", default=".")
-    ap.add_argument("-o", "--output", default="PROJECT_BLUEPRINT.md")
+    ap.add_argument("-o", "--output")
 
     # Preset options
-    ap.add_argument("--preset", default="raw", choices=["iceberg","pro","raw"], help="Preset mode: iceberg/pro/raw")
+    ap.add_argument("--preset", choices=["iceberg","pro","raw"], help="Preset mode: iceberg/pro/raw")
 
     # Token and selection control
-    ap.add_argument("--llm-mode", choices=["off","ref","summary","inline"], default=None)
-    ap.add_argument("--budget-tokens", type=int, default=6000)
-    ap.add_argument("--max-file-tokens", type=int, default=1200)
-    ap.add_argument("--dedup", type=int, default=16)
-    ap.add_argument("--sample-head", type=int, default=120)
-    ap.add_argument("--sample-tail", type=int, default=40)
+    ap.add_argument("--llm-mode", choices=["off","ref","summary","inline"])
+    ap.add_argument("--budget-tokens", type=int)
+    ap.add_argument("--max-file-tokens", type=int)
+    ap.add_argument("--dedup", type=int)
+    ap.add_argument("--sample-head", type=int)
+    ap.add_argument("--sample-tail", type=int)
     ap.add_argument("--explain", action="store_true", help="Include selection rationale and drift_score in capsule comments")
 
     # Filtering and safety controls
-    ap.add_argument("--include-glob", action="append", default=[])
-    ap.add_argument("--exclude-glob", action="append", default=[])
-    ap.add_argument("--omit-glob", action="append", default=[])
-    ap.add_argument("--only-ext", default="")
+    ap.add_argument("--include-glob", action="append")
+    ap.add_argument("--exclude-glob", action="append")
+    ap.add_argument("--omit-glob", action="append")
+    ap.add_argument("--only-ext")
     ap.add_argument("--respect-gitignore", action="store_true")
     ap.add_argument("--follow-symlinks", action="store_true")
-    ap.add_argument("--max-bytes", type=positive_int, default=200_000)
-    ap.add_argument("--max-lines", type=positive_int, default=2000)
+    ap.add_argument("--max-bytes", type=positive_int)
+    ap.add_argument("--max-lines", type=positive_int)
 
     # Output options
     ap.add_argument("--emit-manifest", action="store_true")
     ap.add_argument("--stats", action="store_true")
     ap.add_argument("--capsule", action="store_true", help="Package md+manifest into zip")
     ap.add_argument("--dry-run", action="store_true")
     ap.add_argument("--no-timestamp", action="store_true", help="Omit timestamp for reproducible output")
-    ap.add_argument("--masking", choices=["off", "basic", "advanced"], default="off", help="Secret masking mode (advanced requires Pro license)")
+    ap.add_argument("--masking", choices=["off", "basic", "advanced"], help="Secret masking mode (advanced requires Pro license)")
 
     ap.add_argument("-V", "--version", action="version", version=f"dir2md {__version__}")
 
     ns = ap.parse_args(argv)
 
     root = Path(ns.path).resolve()
-    output = Path(ns.output)
-    only_ext = {e.strip().lstrip('.') for e in ns.only_ext.split(',') if e.strip()} or None

<!-- [truncated middle: 11 lines omitted] -->

-        max_bytes=int(ns.max_bytes) if ns.max_bytes else None,
-        max_lines=int(ns.max_lines) if ns.max_lines else None,
+        include_globs=list(ns.include_glob or []),
+        exclude_globs=list(ns.exclude_glob or []) + DEFAULT_EXCLUDES,
+        omit_globs=list(ns.omit_glob or []),
+        respect_gitignore=bool(ns.respect_gitignore or False),
+        follow_symlinks=bool(ns.follow_symlinks or False),
+        max_bytes=int(ns.max_bytes) if ns.max_bytes is not None else 200_000,
+        max_lines=int(ns.max_lines) if ns.max_lines is not None else 2000,
         include_contents=True,
         only_ext=only_ext,
-        add_stats=bool(ns.stats),
+        add_stats=bool(ns.stats or False),
         add_toc=False,
         llm_mode=(ns.llm_mode or "ref"),
-        budget_tokens=int(ns.budget_tokens),
-        max_file_tokens=int(ns.max_file_tokens),
-        dedup_bits=int(ns.dedup),
-        sample_head=int(ns.sample_head),
-        sample_tail=int(ns.sample_tail),
+        budget_tokens=int(ns.budget_tokens) if ns.budget_tokens is not None else 6000,
+        max_file_tokens=int(ns.max_file_tokens) if ns.max_file_tokens is not None else 1200,
+        dedup_bits=int(ns.dedup) if ns.dedup is not None else 16,
+        sample_head=int(ns.sample_head) if ns.sample_head is not None else 120,
+        sample_tail=int(ns.sample_tail) if ns.sample_tail is not None else 40,
         strip_comments=False,
-        emit_manifest=bool(ns.emit_manifest),
-        preset=str(ns.preset),
-        explain_capsule=bool(ns.explain),
-        no_timestamp=bool(ns.no_timestamp),
-        masking_mode=str(ns.masking),
+        emit_manifest=bool(ns.emit_manifest or False),
+        preset=str(ns.preset or "raw"),
+        explain_capsule=bool(ns.explain or False),
+        no_timestamp=bool(ns.no_timestamp or False),
+        masking_mode=str(ns.masking or "off"),
     )
 
     md = generate_markdown_report(cfg)

```


### File: `scripts\bench_dir2md.py`

```py
from __future__ import annotations
import time, json, argparse
from pathlib import Path
from dir2md.core import Config, generate_markdown_report

def run_case(root: Path, preset: str, mode: str | None, budget: int, file_budget: int) -> dict:
    cfg = Config(
        root=root, output=root/"_BENCH.md", include_globs=[], exclude_globs=[], omit_globs=[],
        respect_gitignore=True, follow_symlinks=False, max_bytes=200_000, max_lines=2000,
        include_contents=True, only_ext=None, add_stats=True, add_toc=False,
        llm_mode=(mode or "ref"), budget_tokens=budget, max_file_tokens=file_budget,
        dedup_bits=16, sample_head=120, sample_tail=40, strip_comments=False,
        emit_manifest=False, preset=preset, explain_capsule=True,
    )
    t0 = time.perf_counter()
    md = generate_markdown_report(cfg)
    dt = time.perf_counter() - t0
    est = md.split("Estimated tokens (prompt): `")[-1].split("`")[0]
    return {"preset": preset, "mode": cfg.llm_mode, "elapsed_sec": round(dt,3), "est_tokens": int(est)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    ns = ap.parse_args()
    root = Path(ns.path).resolve()
    cases = [
        ("iceberg", None, 6000, 1000),
        ("pro", "summary", 6000, 1000),
        ("pro", "ref", 4000, 1000),
        ("pro", "inline", 8000, 1200),
    ]
    rows = [run_case(root, *c) for c in cases]
    print(json.dumps(rows, indent=2))

if __name__ == "__main__":
    main()
```


### File: `src\dir2md\__init__.py`

```py
from .masking import apply_masking
from .core import Config, generate_markdown_report

__all__ = ["__version__", "apply_masking", "Config", "generate_markdown_report"]
__version__ = "1.0.2"
```


### File: `src\dir2md\gitignore.py`

```py
from __future__ import annotations
from pathlib import Path
from typing import List, Optional, Callable

try:
    from pathspec import PathSpec
except Exception:
    PathSpec = None  # type: ignore


def _collect_gitignore_lines(root: Path) -> List[str]:
    lines: List[str] = []
    for gi in root.rglob('.gitignore'):
        rel_dir = gi.parent.relative_to(root)
        base = str(rel_dir).replace('\\', '/')
        raw = gi.read_text(encoding='utf-8', errors='ignore').splitlines()
        for ln in raw:
            s = ln.strip()
            if not s or s.startswith('#'):
                continue
            if s.startswith('/'):
                s = s[1:]
            if base and s:
                s = f"{base}/{s}"
            lines.append(s)
    return lines


def build_gitignore_matcher(root: Path) -> Optional[Callable[[str], bool]]:
    if PathSpec is None:
        return None
    lines = _collect_gitignore_lines(root)
    top = root / ".gitignore"
    if top.exists():
        lines = top.read_text(encoding='utf-8', errors='ignore').splitlines() + lines
    if not lines:
        return None
    spec = PathSpec.from_lines("gitwildmatch", lines)
    def match(relpath: str) -> bool:
        return spec.match_file(relpath)
    return match
```


### File: `src\dir2md\manifest.py`

```py
from __future__ import annotations
from pathlib import Path
import json, hashlib

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def write_manifest(data: dict, out: Path) -> None:
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
```


### File: `src\dir2md\markdown.py`

```py
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core import Config, Stats

def to_markdown(cfg: 'Config', tree_lines: list[str], file_blocks: list[tuple[Path, str, str]], stats: 'Stats') -> str:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts: list[str] = []
    parts.append("# Project Blueprint\n")
    parts.append(f"- Root: `{cfg.root}`  ")
    if not cfg.no_timestamp:
        parts.append(f"- Generated: `{ts}`  ")
    parts.append(f"- Preset: `{cfg.preset}`  ")
    parts.append(f"- LLM mode: `{cfg.llm_mode}`  ")
    parts.append(f"- Estimated tokens (prompt): `{stats.est_tokens_prompt}`  ")
    parts.append("")
    parts.append("## Directory Tree\n")
    parts.append("```\n" + "\n".join(tree_lines) + "\n```\n\n")
    if cfg.llm_mode != "off" and file_blocks:
        parts.append("## File Contents\n")
        for path, lang, text in file_blocks:
            rel = path.relative_to(cfg.root)
            parts.append(f"### File: `{rel}`\n")
            parts.append(f"```{lang}\n{text}\n```\n\n")
    if cfg.add_stats:
        parts.append("## Summary\n")
        parts.append("| metric | value |\n|---|---:|")
        parts.append(f"| dirs | {stats.total_dirs} |")
        parts.append(f"| files in tree | {stats.total_files_in_tree} |")
        parts.append(f"| selected files | {stats.total_with_contents} |")
        parts.append(f"| omitted | {stats.total_omitted} |")
        parts.append(f"| est tokens (prompt) | {stats.est_tokens_prompt} |\n")
    return "\n".join(parts)
```


### File: `src\dir2md.egg-info\dependency_links.txt`

```txt

```

