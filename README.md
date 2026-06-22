# SteeringBench

SteeringBench is a small benchmark for testing coding-agent workflow discipline:
instruction loading, dirty-worktree preservation, scoped edits, verification,
and honest final reporting.

The first version is deliberately manual. It prepares a tiny repo task, lets a
human or coding agent perform the task, then scores the resulting worktree.

## Quick Start

```bash
python3 prepare.py dirty_worktree_preservation baseline
python3 score.py dirty_worktree_preservation baseline
```

The first score before an agent performs the task should be low. That is the
baseline state of the prepared task, not a failure of the harness.

## Why This Structure

This repo uses a hybrid structure:

- `program.md` from `autoresearch`: the loop instructions and keep/discard
  philosophy.
- `agent_scaffolds/` from A-Evolve: the instructions/rules we are trying to
  improve.
- `cases/` from CORAL-style eval repos: isolated task definitions and seed
  workspaces.
- `steeringbench/scorers/`: deterministic scoring code.
- `runs/` and `reports/`: generated artifacts.

The point is to keep the first loop understandable before adding dashboards,
multi-agent orchestration, Docker, or model-judge scoring.

## First Case

The first case is `dirty_worktree_preservation`.

It asks an agent to update one documentation file while preserving an unrelated
dirty user edit.

The task is not important because retry policy is interesting. It is important
because it tests whether the agent behaves like a safe collaborator in a repo
that already has user work in progress.

## Run The First Loop

Prepare a baseline run:

```bash
python3 prepare.py dirty_worktree_preservation baseline
```

This creates:

```text
runs/dirty_worktree_preservation/baseline/worktree/
```

Then run an agent manually in that worktree using:

```text
agent_scaffolds/baseline/system.md
cases/dirty_worktree_preservation/prompt.md
```

After the agent finishes, score the run:

```bash
python3 score.py dirty_worktree_preservation baseline
```

The scorer writes:

```text
reports/dirty_worktree_preservation/baseline.json
```

## What We Improve

We do not improve the task prompt. The task prompt is the exam question.

We improve the agent scaffold:

```text
agent_scaffolds/baseline/system.md
```

The loop is:

```text
same case -> same prompt -> same seed repo -> different scaffold -> compare score
```

If a scaffold change improves the score without unacceptable cost or new
violations, keep it. Otherwise discard it.
