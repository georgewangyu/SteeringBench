from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Case:
    root: Path
    data: dict[str, Any]

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def seed_repo(self) -> Path:
        return self.root / self.data["seed_repo"]

    @property
    def prompt(self) -> Path:
        return self.root / self.data["prompt_file"]


def load_case(case_id: str, repo_root: Path) -> Case:
    case_root = repo_root / "cases" / case_id
    case_file = case_root / "case.json"
    if not case_file.exists():
        raise FileNotFoundError(f"Unknown case: {case_id}")
    return Case(root=case_root, data=json.loads(case_file.read_text()))

