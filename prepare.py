from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from steeringbench.case import load_case


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 prepare.py <case_id> <run_id>", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parent
    case = load_case(sys.argv[1], repo_root)
    run_id = sys.argv[2]
    run_root = repo_root / "runs" / case.id / run_id
    worktree = run_root / "worktree"

    if run_root.exists():
        shutil.rmtree(run_root)
    worktree.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(case.seed_repo, worktree)

    run(["git", "init"], worktree)
    run(["git", "config", "user.email", "steeringbench@example.local"], worktree)
    run(["git", "config", "user.name", "SteeringBench"], worktree)
    run(["git", "add", "."], worktree)
    run(["git", "commit", "-m", "seed repo"], worktree)

    dirty_file = worktree / case.data["dirty_seed_file"]
    dirty_file.write_text(case.data["dirty_seed_text"])

    (run_root / "prompt.md").write_text(case.prompt.read_text())
    (run_root / "system.md").write_text((repo_root / "agent_scaffolds" / "baseline" / "system.md").read_text())

    print(f"Prepared {case.id}/{run_id}")
    print(f"Worktree: {worktree}")
    print(f"Prompt:   {run_root / 'prompt.md'}")
    print(f"System:   {run_root / 'system.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

