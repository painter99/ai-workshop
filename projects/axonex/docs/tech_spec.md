# AXONEX — Unifikovaná technická specifikace

| Položka | Hodnota |
|---|---|
| **Název projektu** | AXONEX — Local Multi-Model Pipeline Orchestrator |
| **Verze dokumentu** | 1.0 (Unified Final) |
| **Datum** | 24. 04. 2026 |
| **Status** | K doladění a tvoření hypotéz |
| **Cílová platforma** | Linux (primárně Pop!_OS 22.04+ s COSMIC Desktop — Epoch 1) |
| **Filozofie** | KISS · Low-latency · Local-first privacy · Backend-agnostic |
| **Licence** | TBD (hobby / open-source) |

---

## 1. 🎯 Přehled projektu

### 1.1 Účel aplikace

AXONEX je **nativní desktopová aplikace pro Linux**, která slouží jako vizuální orchestrátor lokálních velkých jazykových modelů (LLM). Umožňuje řetězit více modelů do pracovních postupů (**Prompt Chaining**), zpracovávat multimodální vstupy (text + obraz) a produkovat garantovaně strukturovaný JSON výstup — to vše **zcela lokálně**, bez cloudových závislostí.

### 1.2 Klíčové charakteristiky

| Charakteristika | Popis |
|---|---|
| **Lokální provoz** | Veškeré inference běží výhradně na hardwaru uživatele. |
| **Řetězení modelů** | Sekvenční zpracování dat přes více modelů s automatickým předáváním kontextu. |
| **Multimodalita** | Nativní podpora obrazových i textových vstupů (Drag & Drop). |
| **Strukturovaný výstup** | Garantovaný JSON formát s Pydantic v2 validací + retry logika. |
| **Backend-agnostic** | Abstrakce LLM vrstvy umožňuje přepnout Ollama ↔ llama.cpp bez zásahu do jádra. |

### 1.3 Strategie nasazení LLM engine

| Fáze | Engine | Účel |
|---|---|---|
| **Prototyp / MVP** | **Ollama** (REST API `localhost:11434`) | Rychlý setup, iterativní ladění chainů, snadná správa modelů, validace konceptu. |
| **Deep Analysis** *(opt.)* | **oLLM / AirLLM** | Volitelný batch backend pro offline zpracování s 70B+ modely na omezeném HW (layer-by-layer CPU/disk inference). Latence minuty–desítky minut; akceptovatelné pro scénáře několika spuštění za směnu. Přidá se jako `A1.2c` v v1.x. |
| **Produkce** | **llama.cpp** (přes `llama-cpp-python`) | Finální distribuce — přímé načítání GGUF modelů, eliminace režie wrapperu, nižší latence, menší binárka, plná kontrola. |

> **Přechod Ollama → llama.cpp** je plánován jako jeden z posledních kroků vývoje, po ověření všech use-caseů v prototypu. Vyžaduje výměnu jediného adapter modulu (`A1.2b`).

---

## 2. 🛠️ Technologický stack

| Vrstva | Technologie | Verze | Odůvodnění |
|---|---|---|---|
| **Jazyk** | Python | 3.10+ | Stabilní `asyncio`, async generátory, Pydantic v2, `tomllib` (3.11+). |
| **UI framework** | Flet (na Flutteru) | ≥ 0.24 | Declarativní UI, GPU akcelerace, built-in Markdown renderer, streaming text, drag-drop. |
| **LLM backend (prototyp)** | Ollama | ≥ 0.5 | REST API, JSON mode, jednoduchá správa modelů. |
| **LLM backend (produkce)** | llama.cpp | ≥ b3500 | Přímá GGUF inference, nativní GPU akcelerace. |
| **LLM bindings (produkce)** | `llama-cpp-python` | latest | Jednotné Python API pro llama.cpp. |
| **HTTP klient** | `httpx` | ≥ 0.27 | Async streaming, kontrolovatelné timeouty, retry policy. |
| **Datová validace** | Pydantic | v2.x | Striktní schémata, runtime validace JSON. |
| **Agentic workflow** | PydanticAI | latest | Vynucení JSON struktury, retry repair, agentic patterns. |
| **Concurrency** | `asyncio` | nativní | Non-blocking UI + token streaming. |
| **Konfigurace** | TOML | `tomllib` | Nativní Python parser od 3.11, čitelnější než YAML. |
| **Kompilace (primární)** | Nuitka | latest | Python → C → standalone binárka (`--onefile`). |
| **Kompilace (záložní)** | PyInstaller | latest | Rychlé testovací buildy. |

### 🚫 Zamítnuté knihovny — zdůvodněné rozhodnutí

> Tento seznam dokumentuje nástroje, které byly zvažovány v rámci brainstormingu a byly vědomě odmítnuty. Slouží jako precedent pro budoucí diskuse.

| Knihovna | Kategorie | Důvod zamítnutí |
|---|---|---|
| **LangGraph** | Orchestrace | Těžká závislost, overkill pro lineární chain; `asyncio` + PydanticAI pokrývají use-case elegantněji. |
| **LangChain** | Orchestrace | Nadměrná komplexita, magické abstrakce skrývají chyby; přímý `httpx` je čitelnější a kontrolovatelnější. |
| **oLLM / AirLLM** | LLM engine (Deep Analysis) | Layer-by-layer disk loading → latence minuty až desítky minut. **Nepoužitelné pro interaktivní režim** (TTFT < 500 ms), ale **hodnotné jako volitelný Deep Analysis backend** pro offline batch (70B+ modely, několik spuštění za směnu). Viz sekce 1.3 — Deep Analysis Mode. |
| **ExLlamaV2** | LLM engine | Vyžaduje NVIDIA VRAM > 4 GB; HW Pavel má 1.4 GB VRAM (viz hardware constraint). |
| **SGLang / vLLM / TensorRT-LLM** | Produkční server | Server-side enginy pro multi-user inference; AXONEX je single-user desktop aplikace. |
| **LocalAI** | API wrapper | Přidává síťovou vrstvu navíc; Ollama/llama.cpp řeší to samé s méně přepalem. |
| **MLC LLM / WebLLM** | Multi-platform | AXONEX v1.0 je Linux only; mobilní/browser target je v plánu mimo scope. |
| **Unsloth** | Fine-tuning | PRD explicitně vylučuje trénování modelů (Non-goal). |
| **CustomTkinter** | UI | Tkinter stack; AXONEX přijal Flet (Flutter) pro GPU akceleraci a streaming text. |
| **ChromaDB / RAG stack** | Znalostní archiv | Hodnotné, ale out-of-scope pro v1.0; přidáno jako modul A2.7 pro v1.x plánování. |
| **Docker kontejnerizace** | DevOps | Redundantní pro desktop hobby projekt; spravuje se přes venv + Nuitka binárka. |

**Klíčový princip:** Pokud brainstorming nabídne nový nástroj ve stejné kategorii, odkaž na tento seznam a zdůvodni, proč je nová volba lepší než zamítnuté alternativy.

---


### ⚠️ Otevřené otázky k ověření (před M1)

| # | Otázka | Výchozí rozhodnutí |
|---|---|---|
| 1 | Flet vs. PySide6 (libadwaita) pro COSMIC stylistiku? | **Flet** — ověřit podporu zaoblených rohů, accent barev, tiling-aware layoutu. |
| 2 | Nuitka vs. PyApp pro distribuci? | **Nuitka** — ověřit velikost binárky a startup time < 3 s. |
| 3 | `ollama-python` vs. čistý `httpx`? | **httpx** — lepší kontrola nad timeouty, retry a streaming granularity. |
| 4 | Formát konfigurace: YAML / JSON / TOML? | **TOML** (nativní od 3.11). |
| 5 | llama.cpp napojení: `llama-cpp-python` vs. subprocess? | **`llama-cpp-python`** — jednotné API. |

---

## 3. 📐 Architektura a atomický rozklad modulů

### 3.1 Modulární struktura projektu

```
axonex/
├── core/                        # Srdce systému
│   ├── orchestrator.py          # A1.1 — Async řízení chainu
│   ├── llm_adapter_base.py      # A1.2 — Abstraktní rozhraní (ABC)
│   ├── ollama_adapter.py        # A1.2a — Prototype adapter
│   ├── llamacpp_adapter.py      # A1.2b — Production adapter
│   ├── stream_handler.py        # A1.3 — Token-by-token streaming
│   ├── model_registry.py        # A1.4 — Katalog modelů a rolí
│   └── health_check.py          # A1.5 — Startup probe backendu
│
├── data/                        # Datová vrstva
│   ├── schemas.py               # A2.1 — Pydantic BaseModel třídy
│   ├── json_enforcer.py         # A2.2 — PydanticAI wrapper + retry
│   ├── multimodal.py            # A2.3 — Obraz → Base64
│   ├── chain_manager.py         # A2.4 — Propagace kontextu mezi kroky
│   └── branch_router.py         # A2.5 — Podmíněné větvení chainu
│
├── ui/                          # Prezentační vrstva (COSMIC style)
│   ├── cosmic_window.py         # A3.1 — Root layout, tmavé téma
│   ├── use_case_selector.py     # A3.2 — Sidebar s recepty
│   ├── input_zone.py            # A3.3 — Text + drag-drop hybrid
│   ├── output_renderer.py       # A3.4 — Streaming Markdown
│   ├── chain_visualizer.py      # A3.5 — (v2) Vizuální stav chainu
│   └── error_overlay.py         # A3.6 — Graceful chybové hlášky
│
├── recipes/                     # Use-case recepty (plug-in)
│   ├── __init__.py
│   ├── invoice_analyzer.py      # R1 — Analýza faktury
│   ├── code_generator.py        # R2 — Generátor kódu
│   └── document_analyzer.py     # R3 — Analýza dokumentu
│
├── build/                       # Build & distribuce
│   ├── nuitka_build.py          # A4.1 — Kompilační skript
│   ├── desktop_generator.py     # A4.2 — `.desktop` + ikona
│   └── config_template.py       # A4.3 — Default `config.toml`
│
├── config.toml                  # Runtime konfigurace
└── main.py                      # Entry point
```

### 3.2 Atomická specifikace modulů

#### A1. Core Engine — Srdce systému

| ID | Modul | Popis | Definition of Done |
|---|---|---|---|
| **A1.1** | `AsyncOrchestrator` | Centrální `asyncio` smyčka řídící tok dat, pořadí kroků chainu, synchronizaci a paralelizaci. | Provede $N$ kroků sekvenčně; výstup kroku $N$ je dostupný jako vstup kroku $N{+}1$; podporuje cancel. |
| **A1.2** | `LLMAdapterBase` (ABC) | Abstraktní rozhraní s metodami `generate()`, `chat()`, `stream()`, `health_check()`. | Všechny konkrétní adaptery dědí a implementují identický kontrakt. |
| **A1.2a** | `OllamaAdapter` | Async wrapper pro Ollama REST API (`/api/generate`, `/api/chat`), JSON mode, streaming přes SSE/NDJSON. | TTFT < 500 ms; stream tokenů bez bufferingu. |
| **A1.2b** | `LlamaCppAdapter` | Přímá integrace přes `llama-cpp-python`. Stejný kontrakt jako Ollama adapter. | Swap backendu změnou jedné hodnoty v `config.toml`; regression testy pass. |
| **A1.2c** *(v1.x opt.)* | `OLLMAdapter` | Volitelný batch backend přes `oLLM` nebo `AirLLM`. Layer-by-layer CPU/disk inference pro 70B+ modely na omezeném HW. **Nepoužitelné pro interaktivní UX** — výhradně pro Deep Analysis recepty s akceptovatelnými minutovými latencemi. | Backend se aktivuje přepnutím v `config.toml`; integrace test s 10-minutovým timeoutem projde. |
| **A1.3** | `StreamHandler` | Zachytávání token-by-token streamu, buffer a push do UI queue (async). | UI zobrazuje tokeny průběžně; žádné „trhání"; latence < 100 ms od přijetí tokenu. |
| **A1.4** | `ModelRegistry` | TOML/dict konfigurace mapující role → modely (např. `vision: granite-vision-4b`, `analyst: qwen3.5-9b`). | Změna modelu pouze editací `config.toml`; žádný zásah do kódu. |
| **A1.5** | `HealthCheck` | Startup probe: ověří dostupnost aktivního backendu. Při selhání → `ErrorOverlay` s instrukcemi. | Spuštění bez backendu nespadne; uživatel vidí jasnou hlášku. |

#### A2. Data Logic — Struktura a validace

| ID | Modul | Popis | Definition of Done |
|---|---|---|---|
| **A2.1** | `PydanticSchemas` | Sada `BaseModel` tříd pro každý use-case (`InvoiceSchema`, `CodeReviewSchema`, `DocumentSchema`). | Každý recept má vlastní schéma; validace probíhá automaticky. |
| **A2.2** | `JSONEnforcer` | PydanticAI wrapper: balí prompt do JSON-mode instrukce, parsuje odpověď, při chybě provede repair retry (max 3×). | Nevalidní JSON → auto-retry s opravným promptem; po 3 neúspěších → `ErrorOverlay`. |
| **A2.3** | `MultimodalProcessor` | Konverze obrázků (PNG/JPG/WebP) → Base64 + metadata (rozměry, mime type). | Drag-dropped obrázek se objeví jako Base64 v API requestu Vision modelu. |
| **A2.4** | `ChainManager` | Předává výstup kroku $N$ jako vstup kroku $N{+}1$, injektuje system prompty, vede data-flow trace. | Plný trace vstup → transformace → výstup pro každý krok; logovatelné. |
| **A2.5** | `BranchRouter` | Podmíněné větvení chainu na základě klíčů v JSON výstupu. Příklad podmínky: $\text{total} > 1000 \Rightarrow \text{větev A}$, jinak větev B. | DSL nebo lambda-based podmínky; unit testy pro všechny větve. |
| **A2.6** *(v1.x)* | `DoclingPDFParser` | Konverze PDF dokumentů na čistý Markdown pomocí knihovny Docling (IBM). Zachovává strukturu tabulek — klíčové pro faktury. Doplňuje `MultimodalProcessor` (A2.3), který řeší obrázky. | PDF faktura → Markdown → `InvoiceSchema` pipeline projde end-to-end; tabulky jsou zachovány. |
| **A2.7** *(v1.x)* | `RAGKnowledgeBase` | Soukromý znalostní archiv: embedding lokálních dokumentů do ChromaDB + FastEmbed → retrieval pro recept `document_analyzer`. Vše lokálně (žádný cloud). | Uživatel se zeptá na obsah svých dokumentů; odpověď vychází z nalezených útržků, ne z parametrů modelu. |

#### A3. UI/UX — Tvář aplikace (COSMIC Style)

| ID | Komponenta | Popis | Definition of Done |
|---|---|---|---|
| **A3.1** | `CosmicWindow` | Flet okno, tmavé téma (`bg #1a1a1a`, accent `#f6b73c`), zaoblené rohy 8–12 px, tiling-aware layout. | Vizuální soulad s COSMIC DE; responzivní na tiling WM. |
| **A3.2** | `UseCaseSelector` | Sidebar se seznamem receptů (ikona + název). | Klik → okamžité načtení chainu bez reloadu. |
| **A3.3** | `InputZone` | Hybridní pole: `TextField` + drag-drop detektor. Indikátor přijatého obrázku. | Přijme text i obrázek; automatická detekce typu vstupu. |
| **A3.4** | `OutputRenderer` | Streaming Markdown widget: tabulky, code highlighting, auto-scroll. | Vše se vykresluje průběžně a korektně; žádné blikání. |
| **A3.5** | `ChainVisualizer` *(v2)* | Grafická reprezentace běžícího chainu (kroky, stav, latency). | Volitelné pro v1; postačí textový log. |
| **A3.6** | `ErrorOverlay` | Non-blocking toast notifikace pro chyby (backend down, invalid JSON, timeout). | Žádný crash; uživatel má možnost retry nebo report. |

#### A4. Build & Deploy — Distribuce

| ID | Úkol | Popis | Definition of Done |
|---|---|---|---|
| **A4.1** | `Nuitka Build` | Skript `./build.sh` pro kompilaci do jednoho statického binárního souboru (`--standalone --onefile`). | Výstupní ELF binárka < 150 MB, spustitelná na čistém Pop!_OS. |
| **A4.2** | `Desktop Integration` | Generátor `axonex.desktop` + ikony (SVG + PNG 16–512 px). Metadata: kategorie Utility / AI / Development. | Aplikace se objeví v COSMIC App Grid s ikonou. |
| **A4.3** | `Config Template` | Výchozí `config.toml` s model registry a cestou k backendu (default: `http://localhost:11434`). | První spuštění funguje bez ruční konfigurace. |

---

## 4. 🔀 Datové toky

### 4.1 Standardní chain

```
┌─────────────────────────────────────────────────────────────┐
│                     Uživatel (text / obrázek)                │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
                        Input Zone (A3.3)
                               │
                               ▼
                 Multimodal Processor (A2.3)
                  (Base64 pokud je vstup obrázek)
                               │
                               ▼
                   Chain Manager (A2.4) — Krok 1
                               │
                ┌──────────────┴──────────────┐
                ▼                              ▼
         JSON Enforcer (A2.2)          LLM Adapter (A1.2a/b)
         + Pydantic (A2.1)                     │
                ▲                              ▼
                │                      Stream Handler (A1.3)
                │                              │
                │                              ▼
                │                     Output Renderer (A3.4)
                │                              │
                └──────────────────────────────┘
                               │
                               ▼
               Branch Router (A2.5) — rozhodnutí
                               │
                               ▼
                   Chain Manager (A2.4) — Krok 2
                               │
                              ...
                               │
                               ▼
                     Finální výstup → UI
```

### 4.2 Abstrakční vrstva LLM Backend

```python
from abc import ABC, abstractmethod
from typing import AsyncGenerator

class LLMAdapterBase(ABC):
    @abstractmethod
    async def generate(
        self, model: str, prompt: str, **kwargs
    ) -> AsyncGenerator[str, None]: ...

    @abstractmethod
    async def chat(
        self, model: str, messages: list[dict], **kwargs
    ) -> AsyncGenerator[str, None]: ...

    @abstractmethod
    async def health_check(self) -> bool: ...
```

Tato abstrakce zajišťuje **transparentní přepínání** mezi Ollama (prototyp) a llama.cpp (produkce) jedinou konfigurační hodnotou v `config.toml`.

---

## 5. 📦 Use-case recepty

| ID | Recept | Chain |
|---|---|---|
| **R1** | Analýza faktury | Vision → extrakce položek (JSON) → analytický model → Markdown tabulka |
| **R2** | Generování kódu | Specifikace → kód → validace syntaxe → automatická oprava chyb |
| **R3** | Analýza dokumentu | OCR → sumarizace → extrakce klíčových bodů → strukturovaný výstup |

> Recepty jsou samostatné moduly v `recipes/` a lze je přidávat bez zásahu do jádra.

### 5.1 Demo Use-Case „Blesková analýza faktury" (M3 acceptance test)

**Účel:** End-to-end integrační test ověřující spolupráci všech modulů současně.

| Krok | Modul / Role | Vstup | Výstup |
|---|---|---|---|
| 0 | Uživatel | Drag & Drop fotografie účtenky + volný text | Obrázek + instrukce |
| 1 | Vision model (LFM2.5-VL-1.6B-Q8_0.gguf) | Base64 obraz + system prompt | `InvoiceSchema { items[], total, date, vendor }` |
| 2 | Analytický model (Qwopus3.5-9B-v3.Q4_K_M.gguf) | JSON z kroku 1 + prompt „Shrň česky" | Markdown text s tabulkou a komentářem |
| 3 | `OutputRenderer` (A3.4) | Markdown string | Renderovaná tabulka v UI |

**Validace bodů selhání:**
- Krok 1 vrátí nevalidní JSON → `JSONEnforcer` provede retry s repair promptem (max 3×).
- Po neúspěchu → `ErrorOverlay` zobrazí raw vision output pro manuální korekci.

---

## 6. ⚙️ Nefunkční požadavky

### 6.1 Výkon

| Metrika | Cíl |
|---|---|
| Startup aplikace | $< 3$ s na desktopovém GPU |
| Time To First Token (TTFT) | $< 500$ ms od odeslání requestu |
| Streaming latence | $< 100$ ms per token (llama.cpp direct) |
| Velikost binárky | $< 150$ MB |

### 6.2 Spolehlivost

| Scénář | Implementace |
|---|---|
| Backend nedostupný | `ErrorOverlay` + graceful fallback |
| Neplatný JSON | Retry loop (max 3× s repair promptem) |
| Chyba modelu | Systémové hlášení + tlačítko „Nahlásit do logu" |
| Timeout | Konfigurovatelný; default $30$ s per krok |

### 6.3 Integrace systému

- `.desktop` soubor pro Pop!_OS Launcher
- Tiling WM responzivní layout
- Tmavé téma v souladu s COSMIC design language
- Ikona v rozlišeních 16–512 px

### 6.4 Systémové požadavky

| Komponenta | Minimum | Doporučené |
|---|---|---|
| **OS** | Pop!_OS 22.04+ / jiný Linux se systemd | Pop!_OS COSMIC |
| **GPU** | CPU-only fallback | NVIDIA CUDA ≥ 12.0 / AMD ROCm ≥ 5.7 |
| **RAM** | 8 GB | 16 GB+ (pro modely > 7B parametrů) |
| **Disk** | 200 MB (aplikace) | + prostor pro lokální modely |

---

## 7. 🧭 Graf závislostí a implementační pořadí

### 7.1 Dependency graph

```
              ┌─────────────┐
              │   A1.2 ABC  │ (base interface)
              └──────┬──────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    A1.2a        A1.2b        A1.5
   (Ollama)   (llama.cpp)  (HealthCheck)
        │            │
        └─────┬──────┘
              ▼
          A1.3 (StreamHandler)
              │
              ▼
          A1.1 (AsyncOrchestrator) ◄── A1.4 (ModelRegistry)
              │
              ▼
          A2.1 (Schemas) ──► A2.2 (JSONEnforcer)
              │                    │
              ▼                    ▼
          A2.3 (Multimodal)   A2.4 (ChainManager) ──► A2.5 (BranchRouter)
                                   │
                                   ▼
          A3.1 (CosmicWindow) ──► A3.2/A3.3/A3.4/A3.6 ──► Recipes (R1-R3)
                                                                │
                                                                ▼
                                                        A4.1/A4.2/A4.3
```

### 7.2 Roadmap implementace (milestones)

| Fáze | Moduly | Přijímací kritérium |
|---|---|---|
| **M1** | A1.2, A1.2a, A1.3, A1.5, A1.4 | Async komunikace s Ollamou, streaming do konzole, health check. |
| **M2** | A2.1, A2.2, A2.4, A2.5, A1.1 | Pydantic validace, JSON enforcement, chain manager, orchestrator — validní JSON round-trip. |
| **M3** | A2.3, A3.1, A3.2, A3.3, A3.4, A3.6 | Kompletní COSMIC UI + multimodální vstup + streaming output. |
| **M4** | R1, R2, R3 | Tři funkční recepty; Demo „Analýza faktury" projde end-to-end. |
| **M5** | A4.1, A4.2, A4.3 | Standalone binárka + `.desktop` integrace + config template. |
| **M6** | A1.2b | Přepnutí backendu na llama.cpp; regression testy pass. |
| **M7** *(v2)* | A3.5 | Vizualizace chainu. |

---

## 8. 📊 Srovnání s existujícími projekty

| Projekt | Síla | Přidaná hodnota AXONEXu |
|---|---|---|
| [Yacana](https://github.com/rememberSoftwares/yacana) | Strukturovaný Pydantic output | Vizuální GUI + Prompt Chaining |
| [TalkPipe](https://github.com/sandialabs/talkpipe) | Unix-like pipeline | Nativní Linux desktop + COSMIC styl |
| [CheetahClaws](https://github.com/SafeRL-Lab/cheetahclaws) | Rychlý async streaming | Komplexní workflows + UI |
| [MultiBot](https://github.com/UndergroundAI-DM/MultiBot) | Multi-model spolupráce | Garantovaný JSON + vizuální chaining |
| [n8n](https://n8n.io/) | Vizuální chaining v uzlech | Nativní Python/Flet + lokální LLM |
| [PydanticAI](https://docs.pydantic.dev/) | Agentic workflows | Integrace do celistvé desktop aplikace |

**Závěr:** AXONEX zaplňuje mezeru mezi CLI nástroji a komplexními webovými frameworky — nativní Linux aplikace s COSMIC designem, garantovaným JSON výstupem a vizuálním Prompt Chainingem, která v této ucelené podobě neexistuje.

---

## 9. 🤖 Instrukce pro AI kódovacího agenta

> **Role:** Jsi hlavní architekt a seniorní Python/Flet vývojář projektu AXONEX.
>
> **Pravidla:**
>
> 1. **Atomizace** — každý modul implementuj jako samostatně testovatelnou jednotku odpovídající `A*` ID v sekci 3.2. Každý modul musí splnit svou **Definition of Done** předtím, než přejdeš na další.
> 2. **KISS princip** — žádné konfigurace LLM parametrů pro koncového uživatele; vše pevně v receptech a `config.toml`.
> 3. **Backend-agnostic** — vždy programuj proti abstrakci `LLMAdapterBase` (A1.2), nikdy přímo proti Ollamě nebo llama.cpp.
> 4. **Typování** — důsledné type hints (Python 3.10+ syntax: `list[str]`, `dict[str, Any]`, `X | None`).
> 5. **Testovatelnost** — každý modul má odpovídající `tests/test_<modul>.py` s pytest + pytest-asyncio.
> 6. **Error handling** — žádné holé `except:`; všechny chyby propagovat přes `ErrorOverlay` (A3.6).
> 7. **Logging** — `structlog` nebo stdlib `logging` s JSON formátem; každý krok chainu loguje vstup/výstup/latenci.
>
> **Postup:**
>
> | Krok | Akce |
> |---|---|
> | 1 | Vytvoř prázdnou strukturu dle sekce 3.1 (`axonex/...`). |
> | 2 | Inicializuj `pyproject.toml` se závislostmi ze sekce 2. |
> | 3 | Implementuj **M1** (A1.2 → A1.2a → A1.3 → A1.5 → A1.4) v tomto pořadí. |
> | 4 | Pro každý modul napiš: implementaci + unit testy + mini ukázku v `examples/`. |
> | 5 | Po dokončení M1 čekej na schválení před pokračováním na M2. |
>
> **Zákazy:**
> - ❌ Nepřidávej cloudové LLM providery (OpenAI, Anthropic, …).
> - ❌ Neměň strukturu adresářů bez schválení.
> - ❌ Nepřidávej závislosti mimo sekci 2 bez explicitního souhlasu.
> - ❌ Nezačínej s UI (A3.x) před dokončením Core Engine (A1.x) a Data Logic (A2.x).

---

<details>
<summary><strong>📎 Appendix A — Default <code>config.toml</code> šablona</strong></summary>

```toml
[backend]
# Aktivní LLM backend: "ollama" | "llamacpp"
active = "ollama"

[backend.ollama]
base_url = "http://localhost:11434"
timeout_seconds = 30

[backend.llamacpp]
models_dir = "~/.axonex/models"
n_gpu_layers = -1
n_ctx = 8192

[models]
# Mapování role → konkrétní model
vision = "LFM2.5-VL-1.6B-Q8_0.gguf"
analyst = "Qwopus3.5-9B-v3.Q4_K_M.gguf"
coder = "Qwopus3.5-9B-v3.Q4_K_M.gguf"
chat = "granite-4.0-h-micro-Q8_0.gguf" nebo "granite-4.0-h-tiny-Q8_0.gguf" 

[ui]
theme = "cosmic-dark"
accent_color = "#f6b73c"
background = "#1a1a1a"

[chain]
max_retries = 3
retry_backoff_seconds = 1.0
step_timeout_seconds = 30

[logging]
level = "INFO"
format = "json"
file = "~/.axonex/logs/axonex.log"
```
</details>

<details>
<summary><strong>📎 Appendix B — Glosář pojmů</strong></summary>

| Pojem | Význam |
|---|---|
| **Chain** | Sekvence modelů, kterými projde vstup postupně; výstup jednoho kroku je kontextem dalšího. |
| **Recept** | Předdefinovaný chain pro konkrétní use-case (faktura, kód, dokument). |
| **Adapter** | Konkrétní implementace `LLMAdapterBase` pro daný backend. |
| **JSON mode** | Režim LLM API, kdy je model instruován produkovat pouze validní JSON. |
| **TTFT** | Time To First Token — čas od odeslání requestu po zobrazení prvního tokenu. |
| **COSMIC** | Desktop Environment od System76 (Pop!_OS Epoch 1). |
| **GGUF** | Binární formát pro llama.cpp modely. |
</details>

---

*AXONEX v1.0 — Unifikovaná specifikace schválená k doladění a tvoření hypotéz.*