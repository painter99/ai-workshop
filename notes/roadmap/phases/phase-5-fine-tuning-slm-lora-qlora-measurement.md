# PHASE 5 — FINE-TUNING SLM (LoRA/QLoRA) + MEASUREMENT (Months 8–9)

## Goal
One engineering experiment: clear task, clear metric, measured improvement.
Strategy: Train in Cloud (RunPod/Colab) → Run Locally (GGUF).

## CORE
- LLM Engineer's Handbook (fine-tuning, evaluation mindset)

## REFERENCE
- Packt "Python Machine Learning By Example" (metrics, experimentation discipline)
- Packt "Mathematics of ML" (Theory on-demand: overfitting/loss/embeddings when needed)

## LAB (core here)
- mlabonne/llm-course (LLM Scientist sections: datasets + LoRA workflows)

## STRATEGY (Cloud-to-Local)
- Use Cloud GPUs for training (RunPod, Lambda Labs, Colab).
- Export fine-tuned model to GGUF format for local inference.
- Keep hardware costs low: pay-per-hour training, local-only serving.

## CONTEXT ENGINEERING IN FINE-TUNING
- Consistent prompt formatting (ChatML/Alpaca) for the dataset.
- Model learns the format, not just the style.

## What you DO (choose ONE task only)
- Option 1: Structured output to JSON schema
- Option 2: Classification (label + short rationale)
- Option 3 (harder): tool-call planning (only if you already have stable tool format)

## Dataset rules
- small is OK (hundreds to few thousands)
- clean formatting, consistent style
- documented source + license + version

## Metric rules (pick one)
- JSON: schema-valid rate, exact match for key fields
- Classification: accuracy/F1
- LLM-judge: plus mandatory manual spot-check sample

## Deliverables
- dataset_card.md (source/license/version/size)
- training_config notes (what model, what params)
- results_before_after.md (table)
- short experiment report (what improved, what regressed, why)
- the quantized model (GGUF) runnable on your Linux machine

## Gate 5 (PASS/FAIL)
PASS if:
- you can show before/after with your chosen metric
- you can reproduce the run (at least roughly)
- you can explain what fine-tuning changed (style/format vs knowledge)
- model runs locally on your Phase 4 endpoint

---

[← Back to roadmap index](../README.md)
