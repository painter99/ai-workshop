# PHASE 1.5 — ENGINEERING HYGIENE MINIMUM (Spread across Months 2–4, ~10–15h)

## Purpose

Not "learn DevOps". Just enough hygiene so later projects don't collapse.

## CORE (tiny set, no rabbit holes)

- Git minimum (CLI preferred eventually, but can start simple)
- Project structure
- Minimal tests
- Minimal logging

## What you DO (minimum checklist)

1) Repo template you will reuse:

- README.md
- requirements.txt OR pyproject.toml (choose one)
- .gitignore
- src/ (optional), data/ (optional), tests/ (optional)
- eval/ (optional later), logs/ (optional later)

2) Git minimum actions:

- create repo
- make commits with messages
- view history (log)

3) Testing minimum:

- install pytest
- create 1 test that asserts a function output ("golden test")

4) Logging minimum:

- use Python logging instead of print for at least 1 script

## Deliverables

- A "template repo" you can copy for future projects
- At least 3 commits (not one giant dump)
- 1 passing pytest test

## Gate 1.5 (PASS/FAIL)

PASS if you have:

- README with run steps
- reproducible dependency list (requirements/pyproject)
- `pytest` passes locally (>=1 test)
- you can commit changes without stress

---

[← Back to roadmap index](../README.md)
