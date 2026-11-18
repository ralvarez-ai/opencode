# Changelog

All notable changes to this repository. Format based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `task install` for OpenCode: the `TOKEN_DISCIPLINE` block in `~/.config/opencode/AGENTS.md`
  (subagent briefs ask for caveman-style reports), RTK v1.1.0 with its OpenCode plugin
  (`--hook-only`), CodeGraph 1.6.3 registered under `mcp.servers`, and the context-mode
  plugin. `task check` / `task verify` report each piece.
- `task check:repos` counts the git repos under `PROJECTS_ROOT` (default
  `~/Dev/active/projects`) that have a CodeGraph index and lists the ones that do not;
  `task check` reports it and counts a gap. `task index:repos` indexes the missing repos and
  adds `.codegraph/` to their `.gitignore`. CodeGraph does nothing in an unindexed repo, so
  without this a repo silently falls back to grep.

### Changed

- CodeGraph 1.6.2 → 1.6.3 (`CODEGRAPH_VERSION`; bumped together with the `claude` repo).
