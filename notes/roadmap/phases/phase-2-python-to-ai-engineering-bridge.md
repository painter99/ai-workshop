# PHASE 2 — PYTHON → AI ENGINEERING BRIDGE (Month 4, ~15–25h)

## CORE

- Towards AI "Beginner Python for AI Engineering" (selective use)

## REFERENCE

- LLM Engineer's Handbook (only app/API mindset sections as needed)

## LAB

- One small Python "API pipeline" project

## What you DO (concrete project spec)

Build a script that:

- takes an input (file or user input)
- calls an HTTP API endpoint
- parses JSON response
- saves output to a file (json/txt)
- handles basic HTTP failure modes:
  - timeout
  - non-200 status
  - empty/invalid JSON

## Deliverables

- repo: `api_pipeline/`
- README: how to run, what it does
- logs: show one success run + one failure case
- optional: 1 pytest for a pure function that processes JSON

## Gate 2 (PASS/FAIL)

PASS if the script is reproducible and robust enough that:

- running it twice works
- bad input does not crash
- failure mode prints/logs a clear message

---

[← Back to roadmap index](../README.md)
