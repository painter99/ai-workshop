# PHASE 4 — LOCAL-FIRST INFERENCE / EDGE BASICS (Month 7)

## Goal

Make local model serving real and stable, usable from your app.

## CORE

- microsoft/edgeai-for-beginners (selected modules: inference + optimization)

## REFERENCE (optional)

- microsoft/PhiCookBook (only if you choose Phi-family SLM)

## LAB

- mlabonne/llm-course (serving + quantization pointers; pick only one path)

## HARD CHOICE (pick ONE serving path; do not compare endlessly)

- Path A (starter): Ollama
- Path B (perf): vLLM (often GPU)
- Path C (CPU-hardcore): llama.cpp server

## Deliverables

- a documented local endpoint:
  - base URL
  - model name
  - how to start/stop
  - how Dify calls it (endpoint settings)
- a tiny benchmark note:
  - latency (rough)
  - tokens/s (rough)
  - RAM usage (rough)

## Gate 4 (PASS/FAIL)

PASS if:

- endpoint is stable for repeated runs
- your Dify app can use it (or a Python script can)
- you understand basic tradeoffs (latency vs context vs quantization)

---

[← Back to roadmap index](../README.md)
