# SteeringBench Agent Instructions

This repository is an eval harness for coding-agent workflow discipline.

## Boundaries

- Keep the first implementation simple and inspectable.
- Prefer deterministic scoring before LLM-as-judge scoring.
- Keep generated run artifacts under `runs/` and `reports/`.
- Do not add dashboards, Docker, or multi-agent orchestration until the first
  manual loop works end to end.

## Editing Rules

- `cases/*/seed_repo/` defines controlled starting repos. Keep these tiny.
- `agent_scaffolds/` contains the agent instructions being evaluated and
  improved.
- `steeringbench/` contains harness and scorer code.
- `program.md` explains the experiment loop for humans and agents.

## Verification

Run:

```bash
python3 prepare.py dirty_worktree_preservation baseline
python3 score.py dirty_worktree_preservation baseline
```

The first score before any agent edits should be low because the task has not
been completed yet. That is expected.

