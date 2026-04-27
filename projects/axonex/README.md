# AXONEX — Local Multi-Model Pipeline Orchestrator

> *"n8n for local LLMs — but native on Linux, without cloud, with guaranteed JSON output."*

[![Status](https://img.shields.io/badge/status-pre--implementation-yellow)]()
[![Platform](https://img.shields.io/badge/platform-Linux-blue)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-TBD-lightgrey)]()

---

## What is AXONEX?

AXONEX is a native Linux desktop application for **visually chaining locally running language models (LLMs) into unified workflows**.

It combines:
- **Multimodal input** — text + images (drag & drop)
- **Guaranteed structured JSON output** — via Pydantic v2 validation with retry repair
- **Full local data sovereignty** — zero cloud, zero data leaving your machine
- **COSMIC Desktop design** — native look & feel for Pop!_OS / COSMIC Desktop Epoch 1

---

## Motivation

Current tools for local LLMs fall into two unsatisfying categories:

| Category | Examples | Limitation |
|----------|----------|------------|
| CLI / Python libraries | Ollama CLI, llama.cpp, LangChain | No visual UI, high entry barrier |
| Web orchestrators | n8n, Flowise, LangFlow | Cloud-first, browser-bound, no native desktop integration |

AXONEX fills the gap: a **lightweight native desktop tool** combining visual chaining (like n8n) with fully local inference (like Ollama) and structured output (like PydanticAI).

---

## Key Features (planned v1.0)

- 🔗 **Sequential prompt chaining** — output of model N becomes input of model N+1
- 🖼️ **Multimodal input** — drag & drop images (PNG/JPG/WebP) → Base64
- ✅ **JSON validation** — Pydantic v2 schemas with auto-retry repair (max 3×)
- 🔌 **Backend-agnostic** — switch Ollama ↔ llama.cpp via `config.toml`
- 📋 **Recipes** — 3 built-in use-cases: invoice analyzer, code generator, document analyzer
- 🔒 **Privacy-first** — all inference runs locally on `localhost`
- 📦 **Single binary distribution** — Nuitka standalone ELF + `.desktop` integration

---

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Language | Python 3.10+ | asyncio, Pydantic v2, tomllib |
| UI | Flet (Flutter) | GPU acceleration, streaming text, drag-drop |
| LLM backend (MVP) | Ollama | Fast setup, iterative tuning |
| LLM backend (prod) | llama.cpp | Lower latency, smaller footprint |
| Validation | Pydantic v2 + PydanticAI | Guaranteed JSON + retry repair |
| Config | TOML | Native Python parser from 3.11 |
| Distribution | Nuitka | Python → C → standalone binary |

---

## Project Status

**Phase:** Pre-implementation — architecture and documentation complete, experiments not yet started.

```
[✅] Product Requirements Document (PRD)
[✅] Technical Specification
[✅] Hypothesis Registry (5 hypotheses pending validation)
[✅] Brainstorm analysis (6 blocks filtered, decisions recorded)
[ ] M0 Proof of Concept (next step)
[ ] M1 Core chain + JSON validation
[ ] M2 Vision input
[ ] M3 Integration test (invoice analyzer)
[ ] M4–M7 UI, build, distribution
```

---

## Planned Use Cases

### 🧾 Invoice Analyzer (flagship demo)
```
Drag & Drop receipt image
        ↓
Vision model → JSON (InvoiceSchema)
        ↓
Analytical model → Markdown summary in Czech
        ↓
OutputRenderer → table in UI
```

### 💻 Code Generator
Describe a function in natural language → get validated Python code

### 📄 Document Analyzer
Upload a document → get structured key-point summary

---

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Linux (systemd) | Pop!_OS 22.04+ / COSMIC |
| GPU | CPU-only fallback | NVIDIA CUDA ≥ 12.0 / AMD ROCm ≥ 5.7 |
| RAM | 8 GB | 16 GB+ |
| Disk | 200 MB (app) | + space for GGUF models |

---

## Repository Structure

```
projects/axonex/
├── docs/
│   ├── prd.md                          # Product Requirements Document
│   ├── tech_spec.md                    # Technical Specification
│   ├── active_hypotheses.md            # 5 hypotheses pending validation
│   ├── hypothesis_registry.md          # Hypothesis template and registry
│   └── brainstorm_analysis_2026-04-27.md  # Brainstorm decisions log
├── AXONEX_INDEX.md                     # Living project index (start here)
├── PLAN_LEHKY_START.md                 # Developer onboarding guide
├── DEVELOPMENT_TOOLSTACK.md            # Recommended development tools
└── README.md                           # This file
```

> 📌 **For AI agents and new contributors:** Start with [`AXONEX_INDEX.md`](AXONEX_INDEX.md) — it contains the authoritative map of all documents, current project state, and key architectural decisions.

---

## Why This Project?

AXONEX is a **personal hobby project** exploring:
- Desktop AI tooling for Linux
- Prompt chaining and local LLM orchestration
- Structured output guarantees with Pydantic
- COSMIC Desktop native app development

It is **not** a commercial product. It serves as deep technical learning and a portfolio demonstration of local AI engineering.

---

## Contributing

This is currently a solo hobby project. If you find it interesting, feel free to open an issue or discussion.

---

## License

TBD — hobby / open-source. See [LICENSE](../../LICENSE) for details once finalized.

---

*Author: Pavel Mareš — 2026*
