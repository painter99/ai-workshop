# PHASE 6 — AGENTS → CONTROLLED MINI MULTI-AGENT (Months 10–12)

## Goal

Build safe, controlled agent workflows with logs and replay.

## CORE

- Dify workflows/agent apps (tool use, routing, memory)

## REFERENCE

- LLM Engineer's Handbook (agents, safety, evaluation)

## LAB (optional patterns only)

- microsoft/autogen (do not make it the core)

## Required guardrails (must implement)

- tool allowlist (explicit tools only)
- sandbox folder for file access (only allowed directory)
- budgets:
  - max steps
  - max time per run
  - max tokens if available (or equivalent)
- logging + replay:
  - store agent decisions and tool calls
  - rerun a scenario set after changes (regression mindset)

## Deliverables

- single-agent workflow (stable) + logs
- controlled 2-role (planner/executor) with hard stop conditions
- small agent_eval_set.jsonl (10–20 scenarios) + rerun notes

## Gate 6 (PASS/FAIL)

PASS if:

- no infinite loops
- tool use stays inside allowlist/sandbox
- you can rerun and compare outcomes after changes

---

[← Back to roadmap index](../README.md)
