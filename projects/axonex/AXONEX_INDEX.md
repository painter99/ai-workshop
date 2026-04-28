# AXONEX — Projekt Index (živý dokument)

> **Instrukce pro AI agenta:** Tento soubor načti jako PRVNÍ při každé AXONEX session.
> Obsahuje aktuální mapu dokumentů, jejich stav a klíčový obsah.
> Po každé session kde dojde k změnám, **aktualizuj tento soubor** — datum, stav, poznámku.

---

## 🗂️ Mapa dokumentů projektu

### Primární dokumenty (vždy relevantní)

| Soubor | Typ | Poslední změna | Stav | Klíčový obsah |
|--------|-----|----------------|------|---------------|
| `README.md` | Veřejný úvod | 2026-04-27 | ✅ Aktuální | Elevator pitch, tech stack, status, use cases, HW požadavky, repo struktura |
| `docs/prd.md` | Produkt | 2026-04-27 | ✅ Aktuální | Executive summary, personas, use cases, FR-1–FR-20, NFR, milestones |
| `docs/tech_spec.md` | Architektura | 2026-04-27 | ✅ Aktuální | Stack, moduly A1.x–A4.x, datové toky, zamítnuté knihovny (11 položek) |
| `docs/active_hypotheses.md` | Experimenty | 2026-04-25 | ⏳ 5 hypotéz čeká | H-TECH-001÷003, H-PERF-001, H-ARCH-001 — vše PROPOSED |
| `PLAN_LEHKY_START.md` | Vývojový plán | 2026-04-25 | ✅ Aktuální | 4 kroky (A–D) pro pokračujícího vývojáře, časové odhady |

### Analytické a referenční dokumenty

| Soubor | Typ | Poslední změna | Stav | Klíčový obsah |
|--------|-----|----------------|------|---------------|
| `docs/brainstorm_pivot_2026-04-28.md` | Brainstorm | 2026-04-28 | ✅ Hotovo | Produktový pivot — nová vize, personas, HitL, Flatpak/AppImage |
| `docs/brainstorm_analysis_2026-04-27.md` | Brainstorm | 2026-04-27 | ✅ Historický | 6 bloků: Docling ✅, oLLM ⚠️, LangGraph ❌, TheAlgorithms ✅ |
| `docs/hypothesis_registry.md` | Šablona | 2026-04-24 | 📋 Šablona | Prázdný registr se šablonou pro nové hypotézy |

### Interní záznamy (v .gitignore — nepublikovat)

| Soubor | Typ | Obsah |
|--------|-----|-------|
| `docs/review_konzultace_v1.md` | Konzultace | Review dokumentů 25.4., hodnocení 7.5/10 |
| `SESSION_SUMMARY_2026-04-25.md` | Session | Shrnutí session 25.4. — kontext, výstupy, pravidla |

---

**Fáze:** Pre-implementace — pivot brief schválen, dokumentace čeká na přepis

**Poslední aktivita:** 2026-04-28 — produktový pivot, brainstorm brief dokončen

**Příští logický krok:** Schválit pivot brief → přepsat PRD + Tech spec → začít Krok A (jednoduchý PoC)


---

## 🔑 Klíčová architektonická rozhodnutí

| Rozhodnutí | Volba | Kde zdokumentováno |
|------------|-------|--------------------|
| UI framework | **Flet** (ne CustomTkinter, ne PySide6) | `tech_spec.md` §2, `brainstorm_analysis` Blok 2 |
| Chain orchestrace | **asyncio + PydanticAI** (ne LangGraph, ne LangChain) | `tech_spec.md` §2.3 |
| MVP backend | **Ollama** → produkce llama.cpp | `tech_spec.md` §1.3 |
| Validace | **Pydantic v2 + PydanticAI** retry repair (max 3×) | `tech_spec.md` §2, FR-4 |
| PDF vstup | **Docling** (IBM) → Markdown → chain | `tech_spec.md` A2.6, FR-13 |
| RAG (v1.x) | **ChromaDB + FastEmbed** — lokální, offline | `tech_spec.md` A2.7, FR-20 |
| Distribuce | **Nuitka** standalone ELF + fallback PyInstaller | `tech_spec.md` §2, A4.1 |
| HW limit | ~1.4 GB VRAM (ThinkPad E14 Gen2, MX450) | `tech_spec.md` §2.3 |

---

## 📚 Studijní zdroje propojené s projektem

| Zdroj | Relevance pro AXONEX | Oblast |
|-------|---------------------|--------|
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | Sorting položek faktury, string processing OCR | Algoritmy, datové struktury |
| [Ollama Prompt Chaining Manual](../practical_tools/ollama_prompt_chaining_manual.md) | Základ existujícího `brainstorm.py` | Multi-model chain |

---

## 📋 Instrukce pro agenta (jak udržovat tento soubor)

1. **Po každé session kde proběhly změny:** Aktualizuj datum a stav v tabulce dokumentů
2. **Při přidání nového souboru:** Přidej řádek do odpovídající tabulky
3. **Při změně architektonického rozhodnutí:** Aktualizuj sekci Klíčová rozhodnutí
4. **Při otestování hypotézy:** Aktualizuj stav v `active_hypotheses.md` A zde přidej poznámku do Aktuální stav
5. **Tento soubor COMMITOVAT** — patří do repozitáře (není v .gitignore)

---

*Poslední aktualizace indexu: 2026-04-27*
*Aktualizoval: Pavel Mareš + Agent Zero*
