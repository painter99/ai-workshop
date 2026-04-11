# PHASE 3 — FIRST LLM APPS (DIFY-FIRST) + RAG + EVAL (Months 5–6)

## Goal
Build your first portfolio-grade RAG application in Dify and prove improvement.
Introduction to Context Engineering.

## CORE
- Packt video: "Dify – Create No-Code Chatbots and AI Workflows"

## REFERENCE
- Packt ebook: "RAG-Driven Generative AI"

## LAB/Repo (choose ONE at a time)
- microsoft/generative-ai-for-beginners (selected RAG + security lessons)
- microsoft/rag-time (journey 1–2) in the iteration phase

## IMPORTANT TECH TARGET
- Dify should run self-hosted locally by the end of Phase 3A or 3B.
- Model can be temporary (even weaker), but local run must exist.

## CONTEXT ENGINEERING FOCUS (New)
- Chunking strategies: Fix-size vs Semantic chunking.
- Reranking: Learn why the top-k results need a second look.

---

## PHASE 3A — DIFY RAG MVP (Weeks 1–3)

## What you DO (MVP spec)
- Pick a knowledge domain you can legally use (your own notes, public docs).
- Create a Dify app with:
  - system instructions
  - knowledge base connected (RAG)
  - basic safety behavior ("abstain" when KB lacks info)
- Create eval set:
  - file: eval/eval_set.jsonl (or csv)
  - at least 30 questions
  - categories:
    - 10 factual questions answerable from docs
    - 10 citation-required questions ("quote source")
    - 10 "should abstain / not in docs"

## Deliverables
- README:
  - what the app does
  - how to run Dify locally
  - how to load KB
  - how to run the eval (even if manual)
- eval_set file in repo
- "Known limitations" section
## Gate 3A (PASS/FAIL)
PASS if:
- Dify app works end-to-end (ask → retrieval → answer)
- at least some form of provenance/citation is present (if Dify supports it)
- abstain policy exists and you tested it with "not in docs" queries

---

## PHASE 3B — RAG QUALITY ITERATION (Weeks 4–6)

## What you DO (quality spec)
- Data pipeline:
  - define document source list (what is included/excluded)
  - cleaning rules (remove boilerplate, normalize headings)
  - version your KB (v1, v2)
- Retrieval improvements (one change at a time):
  - chunk size / overlap changes
  - metadata tagging (doc type, date, section)
  - prompt adjustments for "cite sources"
  - implement basic reranking if possible
- Re-run eval:
  - record results before/after
  - make a simple table:
    - correct / incorrect / abstain-correct / hallucination

## Deliverables
- docs/data_pipeline.md (source + cleaning + KB versioning)
- eval/results_v1.md + eval/results_v2.md (or one table with both)
- short release notes: "what changed and why"

## Gate 3B (PASS/FAIL) — Portfolio-ready RAG
PASS if:
- KB pipeline is documented
- eval shows measurable improvement
- you can explain tradeoffs and remaining failure modes

## SECURITY/LICENSING CHECKPOINT (must do here)
- Are docs public/your own? Can you publish them?
- If not: publish only scripts + synthetic/sample docs.

---

[← Back to roadmap index](../README.md)
