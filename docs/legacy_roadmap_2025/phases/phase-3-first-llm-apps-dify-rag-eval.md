# PHASE 3 — FIRST LLM APPS + RAG + EVAL (Months 5–6)

## Goal
Build your first portfolio-grade local RAG pipeline and prove quality improvement through eval.
Introduction to Context Engineering.

## PATH CHOICE (pick ONE primary path)

### Path A — Python-first (RECOMMENDED)
Build your own lightweight Python orchestrator: load docs → chunk → embed → retrieve → generate.
You understand every line of code. Harder, slower to start, deeper understanding.

**CORE (Path A):**
- Packt ebook: "RAG-Driven Generative AI" (primary build guide)

**REFERENCE (Path A):**
- LLM Engineer's Handbook (API mindset, retrieval patterns)
- microsoft/generative-ai-for-beginners (selected RAG lessons)
- microsoft/rag-time (journey 1–2 for iteration ideas)

---

### Path B — No-code orchestrator (OPTIONAL)
Use Dify, Flowise, or Langflow as a fast prototyping shell.
Faster to first result, less code understanding, useful for validating ideas or working in teams that use these tools.

**CORE (Path B):**
- Packt video: "Dify – Create No-Code Chatbots and AI Workflows" (owned)

**REFERENCE (Path B):**
- Packt ebook: "RAG-Driven Generative AI" (for understanding what Dify does under the hood)

> **Note on no-code tools:** Dify/Flowise/Langflow are essentially backend glue + FE-BE bridging layers.
> They connect LLM APIs, vector stores, and UI without you writing that plumbing.
> Useful for prototyping. Limited for non-standard requirements.

---

## IMPORTANT TECH TARGET
- Local model must serve your pipeline by end of Phase 3A (Ollama or equivalent).
- Model can be weak, but local run must be stable.
- Path A: your Python script calls Ollama directly.
- Path B: Dify/Flowise self-hosted locally, connected to Ollama.

## CONTEXT ENGINEERING FOCUS
- Chunking strategies: Fixed-size vs Semantic chunking.
- Reranking: Learn why top-k results need a second pass.

---

## PHASE 3A — RAG MVP (Weeks 1–3)

## What you DO (MVP spec)
- Pick a knowledge domain you can legally use (your own notes, public docs).
- Build an app/pipeline that:
  - loads a knowledge base (documents)
  - answers questions using retrieval (RAG)
  - has basic safety behavior: "abstain" when KB lacks info
- Create eval set:
  - file: `eval/eval_set.jsonl` (or csv)
  - at least 30 questions
  - categories:
    - 10 factual questions answerable from docs
    - 10 citation-required questions ("quote source")
    - 10 "should abstain / not in docs"

## Deliverables
- README:
  - what the app does
  - how to run it locally (Path A: `python rag_pipeline.py`, Path B: how to start Dify)
  - how to load KB
  - how to run the eval (even if manual)
- `eval/eval_set.jsonl` in repo
- "Known limitations" section

## Gate 3A (PASS/FAIL)
PASS if:
- Pipeline works end-to-end (ask → retrieval → answer)
- At least some form of provenance/citation is present
- Abstain policy exists and you tested it with "not in docs" queries

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
- `docs/data_pipeline.md` (source + cleaning + KB versioning)
- `eval/results_v1.md` + `eval/results_v2.md` (or one table with both)
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
