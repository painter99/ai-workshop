# PAVEL — DETAIL ROADMAP (12–24 months, 5h/week, Linux, local-first)

**Goal:** Local-first Python LLM pipeline apps + 1 fine-tuned SLM (trained Cloud -> served Local) + Agents
**Style:** low-friction, portfolio-ready outputs, deep context understanding
**Philosophy:** Python-first, understand the code you run. No-code tools (Dify, Flowise, Langflow) are optional Path B — useful for prototyping and backend/FE-BE bridging, but not the primary learning vehicle.

---

## MATERIALS (COMPLETE)

### CORE Python

- Ardit "Python Mega Course"
- PY4E (Owned book)

### CORE Bridge & AI Engineering

- Towards AI "Beginner Python for AI Engineering"

### CORE RAG & Context (Books)

- Packt "RAG-Driven Generative AI"
- Packt "LLM Engineer's Handbook"

### CORE RAG & Context (Videos)

- Packt Video: "Dify – No-Code Chatbots & Workflows"
- Packt Video: "AI & LLM Engineering Mastery – GenAI/RAG" (optional accel)

### Advanced Agents (Context Engineering Mastery)

- Packt "Context Engineering for Multi-Agent Systems"

### Math & ML Reference

- Packt "Python Machine Learning By Example"
- Packt "Mathematics of ML"

### Practice Hub & Free Resources

- GitHub: <https://github.com/mlabonne/llm-course>
- Microsoft: generative-ai-for-beginners
- Microsoft: rag-time
- Microsoft: edgeai-for-beginners
- Microsoft: PhiCookBook

### Reference / Encyclopedia

- Harvard "ML Systems" (2.6k pages)

---

## OPERATING RULES (to prevent overload)

1. **1 CORE + 1 REFERENCE + 1 LAB/Repo** per phase.
2. **OFFLINE MODE:** When you are not at your PC, study theory (Embeddings, RAG architecture, Context Engineering, Quantization).
3. **FLEX-TIME:** The goal is mastery, not speed. 5 hours/week → depth over speed.

---

## PORTFOLIO RULE

Every phase ends with a concrete artifact in a repo:

- README (How to run / What I learned / Known limitations)
- (if applicable) eval/results or benchmarks

---

## WHERE I AM NOW

**Last assessed:** 2026-04-25

Formal status vs. real-world practice often diverge — this section captures both.

| Phase | Formal Status | Real-World Practice |
|-------|--------------|---------------------|
| 0 | ✅ Complete | Linux, Python, venv, Git all working |
| 1 | 🔄 In Progress | Core syntax solid; Python Mega Course ongoing; projects already in play |
| 1.5 | 🔄 In Progress | Git/GitHub ✅, structured repos ✅; pytest and systematic logging still pending |
| 2 | 🟡 Partial | Not formally completed, but AXONEX project already does exactly what Gate 2 requires: Ollama API → JSON parse → file output → error handling |
| 3 | ⬜ Not started | Dify untouched; RAG pipeline not yet built formally |
| 4 | 🟡 Partial | Ollama running locally ✅; basic prompt chaining working; formal benchmark not documented |
| 5–6 | ⬜ Not started | Fine-tuning and agents not yet started |

> **Note on 🟡 Partial:** Phase requirements are met in practice through project work, but formal deliverables (README, eval, logged benchmark) are not yet written up.

**Active project:** [AXONEX](../projects/axonex/) — local multi-model Python pipeline, covers Phase 2 and early Phase 4 territory.

---

## Phase Navigation & Status

| Phase                                                                 | Title                                      | Status |
| --------------------------------------------------------------------- | ------------------------------------------ | ------ |
| [PHASE 0](./phases/phase-0-setup-workflow-base.md)                    | SETUP & WORKFLOW BASE                      | ☑️     |
| [PHASE 1](./phases/phase-1-python-foundations.md)                     | PYTHON FOUNDATIONS + THEORY BASE           | 🔄     |
| [PHASE 1.5](./phases/phase-1-5-engineering-hygiene-minimum.md)        | ENGINEERING HYGIENE MINIMUM                | 🔄     |
| [PHASE 2](./phases/phase-2-python-to-ai-engineering-bridge.md)        | PYTHON → AI ENGINEERING BRIDGE             | ⬜     |
| [PHASE 3](./phases/phase-3-first-llm-apps-dify-rag-eval.md)           | FIRST LLM APPS + RAG + EVAL                | ⬜     |
| [PHASE 3.5](./phases/phase-3-5-optional-accelerator.md)               | OPTIONAL ACCELERATOR                       | ⬜     |
| [PHASE 4](./phases/phase-4-local-first-inference-edge-basics.md)      | LOCAL-FIRST INFERENCE / EDGE BASICS        | ⬜     |
| [PHASE 5](./phases/phase-5-fine-tuning-slm-lora-qlora-measurement.md) | FINE-TUNING SLM (CLOUD-TO-LOCAL)           | ⬜     |
| [PHASE 6](./phases/phase-6-agents-controlled-mini-multi-agent.md)     | AGENTS + ADVANCED CONTEXT & MEMORY         | ⬜     |
| [OPTIONAL](./phases/optional-towards-ai-full-stack-ai-engineering.md) | Towards AI Full Stack AI Engineering       | ⬜     |
| [END STATE](./phases/end-state-month-12.md)                           | MONTH 12/24 DELIVERABLES                   | ⬜     |

---

**Last Updated:** 2026-04-25
