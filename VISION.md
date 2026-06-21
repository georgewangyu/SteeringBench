# SteeringBench Vision

SteeringBench should be a small, inspectable benchmark for coding-agent
workflow discipline.

## Product Thesis

The benchmark is useful because it tests the boring behaviors that decide
whether coding agents are safe collaborators: instruction loading, dirty
worktree preservation, scoped edits, verification, and honest final reporting.
The first version should stay manual and deterministic before adding heavier
orchestration.

## Goals

- Keep cases tiny enough to inspect by hand.
- Prefer deterministic scorers before model-judge scoring.
- Compare agent scaffolds against the same seed repo and prompt.
- Make failure modes concrete enough to improve instructions.

## Non-Goals

- Do not add dashboards, Docker, or multi-agent orchestration before the first
  loop works end to end.
- Do not improve the exam prompt when the goal is to improve the scaffold.
- Do not let generated run artifacts become source-of-truth docs.
