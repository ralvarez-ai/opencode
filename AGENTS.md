# AGENTS.md — opencode

Applies the OpenCode setup for this machine. The product is `task install`: it
must stay idempotent, back up what it edits, and leave other tools' config alone.

## Rules

- **Idempotent.** Running `task install` twice changes nothing the second time. Tool
  steps carry a `status:` check; instruction files are edited only inside the
  `TOKEN_DISCIPLINE` markers (`scripts/apply-block.py`).
- **Pinned.** `RTK_VERSION` and `CODEGRAPH_VERSION` in `Taskfile.yml` match the sibling
  `claude` repo. Bump both together.
- **Foreign blocks stay.** CodeGraph and other tools keep their own marked blocks in
  `AGENTS.md`; never rewrite outside our markers.
- **No secrets** (provider keys live in OpenCode's auth store, not here).
- **Nothing is committed or pushed** unless the owner asks.

## Checks

```bash
task lint     # py_compile on the scripts
task check    # read-only state report
```

Every change to what `task install` writes needs a `CHANGELOG.md` entry.
