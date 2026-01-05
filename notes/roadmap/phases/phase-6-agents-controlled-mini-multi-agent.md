# PHASE 6 — AGENTS → CONTROLLED MINI MULTI-AGENT (Months 10–12)

## Goal
Build safe, controlled agent workflows with logs and replay.
Advanced Context Engineering for agentic memory management.

## CORE
- **Packt: "Context Engineering for Multi-Agent Systems"**
  - This is your PRIMARY guide for building Context Engines.
  - Study: Semantic Blueprints, MCP, Memory Models, Safeguards.
  - Build: One Glass-Box agent example from the book (Chapter 10).

## REFERENCE
- LLM Engineer's Handbook (only for cross-checking specific agent patterns)
- Dify Documentation (for implementation of the architecture)

## ADVANCED CONTEXT ENGINEERING
- Agent Memory Management:
  - Conversation Summary Buffer (prevent context overflow).
  - When to prune: token limits vs. information loss.
- Tool-calling context:
  - How to present tool outputs to the agent clearly.
- Lost in the Middle mitigation:
  - Critical info placement (beginning/end) in agent context.

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
- memory management strategy document (how you handle context limits)

## Gate 6 (PASS/FAIL)
PASS if:
- no infinite loops
- tool use stays inside allowlist/sandbox
- you can rerun and compare outcomes after changes
- agent memory management prevents context overflow in multi-turn conversations

---

[← Back to roadmap index](../README.md)
