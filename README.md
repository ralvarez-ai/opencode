# opencode

Setup for OpenCode on this machine: the token tools and the global instructions,
applied idempotently by `task install`. The Claude Code counterpart is the sibling
`claude` repository; both install the same tool versions.

## What it applies

| Piece | Source | Destination |
|---|---|---|
| Instructions block | `instructions/token-discipline.md` | `~/.config/opencode/AGENTS.md` (marked block `TOKEN_DISCIPLINE`) |
| RTK | `task install:rtk` | `~/.local/bin/rtk` + `~/.config/opencode/plugins/rtk.ts` |
| CodeGraph | `task install:codegraph` | npm global + `mcp.servers.codegraph` in `opencode.jsonc` |
| context-mode | `task install:context-mode` | `plugins` in `opencode.jsonc` |

```bash
task              # list the tasks
task check        # what is applied and what is missing (read-only)
task install      # apply everything
task uninstall    # remove the instructions block
```

## Notes

- **RTK** runs with `--hook-only`, so no `RTK.md` joins the always-loaded instructions.
  `rtk init --opencode` also (re)applies the Claude Code hook; RTK has no OpenCode-only mode.
  Savings: `rtk gain`.
- **CodeGraph** only acts in repos that have an index: run `codegraph init` in a repo and
  add `.codegraph/` to its `.gitignore`. It writes its own marked block to `AGENTS.md`.
  Telemetry is on by default: `codegraph telemetry off` disables it.
- **context-mode** loads its `ctx_*` tools and routing hooks. Measure what it injects
  before trusting it on long sessions (the `claude` repo has the audit).
- **`opencode mcp list`** in 2.1.x does not show servers under `mcp.servers`; check with
  `opencode debug config`, or ask the agent to list its tools.
- The built-in `explore` subagent is left as it is: an override replaces its prompt.
  The instructions block asks the main agent to request terse reports instead.

## Removing the tools

`rtk init -g --opencode --uninstall`, `opencode plugin remove context-mode`, and delete
`mcp.servers.codegraph` from `opencode.jsonc`.
