# AXONEX — Product Requirements Document (PRD)

| Položka | Hodnota |
|---|---|
| **Produkt** | AXONEX — Local Multi-Model Pipeline Orchestrator |
| **Verze PRD** | 1.0 |
| **Datum** | 24. 04. 2026 |
| **Status** | Draft ke schválení |
| **Typ projektu** | Hobby / Open-source |
| **Vlastník** | Autor projektu (solo developer) |
| **Cílová platforma** | Linux (Pop!_OS 22.04+ / COSMIC Desktop Epoch 1) |

---

## 1. Executive Summary

**AXONEX** je nativní desktopová aplikace pro Linux, která umožňuje entuziastům a vývojářům vizuálně řetězit lokálně běžící jazykové modely (LLM) do ucelených pracovních postupů. Produkt kombinuje **multimodální vstup** (text + obraz), **garantovaně strukturovaný JSON výstup** a **plnou lokální suverenitu dat** — vše v designu konzistentním s prostředím COSMIC Desktop.

> **Elevator pitch:** _„n8n pro lokální LLM — ale nativně na Linuxu, bez cloudu a s garantovaným JSON výstupem."_

---

## 2. Problémové pozadí a příležitost

### 2.1 Problém

Současné nástroje pro práci s lokálními LLM se dělí do dvou nevyhovujících kategorií:

| Kategorie | Příklady | Omezení |
|---|---|---|
| **CLI / Python knihovny** | Ollama CLI, llama.cpp, LangChain | Neexistuje vizuální UI, high entry-barrier pro non-developery. |
| **Webové orchestrátory** | n8n, Flowise, LangFlow | Cloud-first, browser-bound, vyžadují server, chybí nativní integrace s desktopem. |

Chybí **lehký, nativní desktopový nástroj**, který by spojil vizuální chainování (jako n8n) s plně lokální inference (jako Ollama) a zároveň garantoval strukturovaný výstup (jako PydanticAI).

### 2.2 Příležitost

- Rostoucí dostupnost kvalitních GGUF modelů pod 10 B parametrů spustitelných na consumer GPU.
- Vzestup COSMIC Desktop Epoch 1 jako moderní Linux DE hledající nativní AI aplikace.
- Sílící poptávka po **privacy-first** nástrojích, které neexportují data do cloudu.

---

## 3. Produktová vize a cíle

### 3.1 Vize

> Umožnit každému nadšenci do lokálního AI vytvořit během několika minut **multimodální pipeline** z několika jazykových modelů — bez psaní kódu, bez cloudu a bez kompromisu v latenci.

### 3.2 Strategické cíle produktu

| # | Cíl | Měřitelnost |
|---|---|---|
| **G1** | Doručit funkční MVP demonstrující end-to-end chain (obraz → JSON → Markdown). | Demo „Analýza faktury" projde integračním testem (M3). |
| **G2** | Udržet UX na úrovni native desktop aplikace. | Startup < 3 s, TTFT < 500 ms. |
| **G3** | Zajistit přenositelnost mezi LLM enginy. | Přepnutí Ollama ↔ llama.cpp pouze změnou `config.toml`. |
| **G4** | Distribuovat jako jediný standalone binární soubor. | `.AppImage` / ELF < 150 MB, `.desktop` integrace do COSMIC. |

### 3.3 Non-goals (co produkt **nebude** dělat)

- ❌ Integrovat cloudové LLM providery (OpenAI, Anthropic, Google).
- ❌ Nabízet uživatelské ladění parametrů modelů (temperature, top-p atd.) — vše je pevně v receptech.
- ❌ Podporovat Windows/macOS v první verzi.
- ❌ Být multi-user / serverová aplikace.
- ❌ Trénovat nebo fine-tunovat modely.

---

## 4. Cílové persony

<details>
<summary><strong>👤 Persona 1 — „Tomáš, Linux power-user"</strong> (primární)</summary>

- **Profil:** 30 let, backend developer, Pop!_OS uživatel, privacy-conscious.
- **Potřeba:** Rychle vyzkoušet kombinaci vision + text modelu na vlastních dokumentech bez nahrávání do cloudu.
- **Pain point:** Neumí / nechce psát vlastní LangChain skripty pro každý experiment.
- **Jak AXONEX pomáhá:** Drag-and-drop rozhraní, předpřipravené recepty, okamžitá vizuální zpětná vazba.
</details>

<details>
<summary><strong>👤 Persona 2 — „Klára, AI nadšenec"</strong> (sekundární)</summary>

- **Profil:** Studentka informatiky, experimentuje s lokálními LLM, programuje v Pythonu na úrovni hobby.
- **Potřeba:** Porozumět, jak fungují multi-model pipelines, a prototypovat vlastní workflow.
- **Jak AXONEX pomáhá:** Recepty jako plug-in moduly, které lze číst a upravovat jako Python kód.
</details>

---

## 5. Use cases a uživatelské scénáře

### 5.1 Hlavní use cases (v1.0)

| ID | Scénář | User story |
|---|---|---|
| **UC-1** | Analýza faktury | _Jako uživatel chci přetáhnout fotografii účtenky a dostat strukturovanou tabulku položek s celkovou sumou, abych je mohl rychle zkopírovat do účetnictví._ |
| **UC-2** | Generování kódu | _Jako vývojář chci popsat funkci slovy a dostat validní Python kód včetně automatické opravy syntaxe, abych urychlil prototypování._ |
| **UC-3** | Analýza dokumentu | _Jako uživatel chci nahrát dokument a dostat strukturované shrnutí klíčových bodů, abych nemusel číst celý text._ |

### 5.2 Flagship demo scénář (M3 acceptance test)

**„Blesková analýza faktury"** — end-to-end test celé architektury:

```
Drag&Drop účtenky + text
        ↓
Vision model (LFM2.5-VL-1.6B) → JSON (InvoiceSchema)
        ↓
Analytický model (Qwopus3.5-9B) → Markdown shrnutí v češtině
        ↓
OutputRenderer → tabulka v UI
```

**Akceptační kritérium:** Proces proběhne do 15 s na doporučeném HW, JSON je validní nebo je po max. 3 retry pokusech korigován.

---

## 6. Funkční požadavky

### 6.1 Must-have (v1.0)

| ID | Požadavek | Priorita |
|---|---|---|
| **FR-1** | Async orchestrace sekvenčního řetězení modelů s propagací kontextu. | P0 |
| **FR-2** | Abstraktní LLM vrstva podporující backend Ollama (prototyp) i llama.cpp (produkce). | P0 |
| **FR-3** | Token-by-token streaming výstupu do UI bez blokace. | P0 |
| **FR-4** | Validace LLM výstupů vůči Pydantic v2 schématům s retry repair (max 3×). | P0 |
| **FR-5** | Multimodální vstup: Drag & Drop obrázků (PNG/JPG/WebP) → Base64. | P0 |
| **FR-6** | Min. 3 předpřipravené recepty (faktura, kód, dokument). | P0 |
| **FR-7** | Nativní COSMIC design (tmavé téma, accent barva, zaoblené rohy, tiling-aware). | P0 |
| **FR-8** | Konfigurace přes `config.toml` (žádný zásah do kódu pro výměnu modelů). | P0 |
| **FR-9** | Health-check backendu při startu + graceful error overlay. | P0 |
| **FR-10** | Distribuce jako standalone ELF binárka + `.desktop` integrace. | P0 |

### 6.2 Should-have (v1.x)

| ID | Požadavek | Priorita |
|---|---|---|
| **FR-11** | Podmíněné větvení chainu (`BranchRouter`) na základě JSON klíčů. | P1 |
| **FR-12** | Strukturované JSON logování (structlog) s trace per krok. | P1 |

### 6.3 Nice-to-have (v2.0+)

| ID | Požadavek | Priorita |
|---|---|---|
| **FR-13** | Grafická vizualizace běžícího chainu (`ChainVisualizer`). | P2 |
| **FR-14** | Paralelní (fan-out/fan-in) chainy. | P2 |
| **FR-15** | Export chainu do sdíletlného formátu (recept-as-file). | P2 |

---

## 7. Nefunkční požadavky

### 7.1 Výkon

| Metrika | Cíl |
|---|---|
| Startup aplikace | $< 3$ s (doporučený HW) |
| Time To First Token (TTFT) | $< 500$ ms |
| Streaming latence per token | $< 100$ ms (llama.cpp direct) |
| Velikost binárky | $< 150$ MB |

### 7.2 Spolehlivost a UX

- **Zero-crash policy:** Žádná neošetřená výjimka nesmí shodit aplikaci; vše přes `ErrorOverlay`.
- **Retry loop:** Nevalidní JSON → max 3 pokusy s opravným promptem.
- **Timeouty:** Konfigurovatelné, default 30 s per krok.
- **First-run experience:** Aplikace se musí spustit a zobrazit jasné instrukce i bez běžícího backendu.

### 7.3 Bezpečnost a privacy

- Veškerá inference běží lokálně; žádný síťový provoz mimo `localhost` (vyjma případného stahování modelů přes Ollama).
- Data uživatele nikdy neopouštějí jeho stroj.
- Logy uloženy pouze lokálně v `~/.axonex/logs/`.

### 7.4 Systémové požadavky

| Komponenta | Minimum | Doporučeno |
|---|---|---|
| OS | Linux se systemd | Pop!_OS 22.04+ / COSMIC |
| GPU | CPU-only fallback | NVIDIA CUDA ≥ 12.0 / AMD ROCm ≥ 5.7 |
| RAM | 8 GB | 16 GB+ |
| Disk | 200 MB (app) | + prostor pro GGUF modely |

---

## 8. Technologická strategie (souhrn)

| Vrstva | Volba | Odůvodnění v kostce |
|---|---|---|
| Jazyk | Python 3.10+ | asyncio, Pydantic v2, `tomllib`. |
| UI | Flet (Flutter) | GPU akcelerace, streaming text, drag-drop out-of-the-box. |
| LLM backend (MVP) | Ollama | Rychlý setup pro iterativní ladění. |
| LLM backend (produkce) | llama.cpp via `llama-cpp-python` | Nižší latence, menší footprint. |
| Validace | Pydantic v2 + PydanticAI | Garantovaný JSON + retry repair. |
| Build | Nuitka | Standalone binárka, C-kompilace. |

> 🔗 Detailní architektonický rozklad na atomické moduly (A1.x–A4.x) viz **samostatný dokument „Technická specifikace v1.0"**.

<details>
<summary><strong>🔬 Otevřené technologické hypotézy k validaci před M1</strong></summary>

| # | Otázka | Výchozí volba | Kritérium rozhodnutí |
|---|---|---|---|
| 1 | Flet vs. PySide6 pro COSMIC look? | Flet | Musí podporovat zaoblené rohy a accent barvy. |
| 2 | Nuitka vs. PyApp? | Nuitka | Binárka < 150 MB, startup < 3 s. |
| 3 | `ollama-python` vs. čistý `httpx`? | httpx | Kontrola streaming granularity. |
| 4 | Formát konfigurace? | TOML | Nativní v 3.11, čitelnější než YAML. |
| 5 | llama.cpp integrace? | `llama-cpp-python` | Jednotné Python API. |
</details>

---

## 9. Milestones a roadmap

| Fáze | Sprint | Focus | Deliverable | Akceptace |
|---|---|---|---|---|
| **M1** | 1 | Core backend | Async Ollama adapter, streaming, health-check, model registry | Streaming tokenů v konzoli |
| **M2** | 2 | Data logic | Pydantic schémata, JSON enforcer, chain manager, orchestrator | Validní JSON round-trip |
| **M3** | 3 | UI + multimodal | COSMIC okno, input zone, output renderer, error overlay | Kompletní UI + drag-drop |
| **M4** | 4 | Recepty | R1 (faktura), R2 (kód), R3 (dokument) | Demo „Analýza faktury" E2E |
| **M5** | 5 | Distribuce | Nuitka build, `.desktop`, config template | Instalovatelný binár |
| **M6** | 6 | Backend swap | llama.cpp adapter | Regression testy pass |
| **M7** | v2 | Vizualizace | `ChainVisualizer` | — |

---

## 10. Úspěch produktu — metriky

### 10.1 Kvantitativní (v1.0 release)

| KPI | Cíl |
|---|---|
| Demo „Analýza faktury" úspěšně dokončeno | 100 % průchodů při 10 test-runech |
| Startup time | $< 3$ s |
| TTFT | $< 500$ ms |
| Binary size | $< 150$ MB |
| Pokrytí unit testy | $\geq 70\%$ core modulů |

### 10.2 Kvalitativní (hobby-appropriate)

- Aplikace je vizuálně nerozeznatelná od nativní COSMIC aplikace.
- Non-developer dokáže spustit recept bez čtení zdrojového kódu.
- Přepnutí backendu proběhne bez úpravy kódu.

---

## 11. Konkurence a pozicování

| Projekt | Silná stránka | Mezera, kterou AXONEX plní |
|---|---|---|
| Ollama CLI | Snadná správa modelů | Chybí vizuální UI a chainování |
| n8n | Vizuální workflows | Vyžaduje browser + není lokální |
| LangFlow | Chain designer | Browser-based, těžký setup |
| PydanticAI | Strukturovaný output | Není aplikace, pouze knihovna |
| Yacana / TalkPipe / MultiBot | Multi-model patterns | CLI-only, bez GUI |

**Unikátní hodnota AXONEXu:** _Jediná nativní Linux desktop aplikace pro vizuální chainování lokálních LLM s garantovaným JSON výstupem a COSMIC designem._

---

## 12. Rizika a mitigace

| # | Riziko | Dopad | Pravděpodobnost | Mitigace |
|---|---|---|---|---|
| **R1** | Flet nepodpoří všechny COSMIC vizuální prvky | Střední | Střední | Validovat před M3; fallback na PySide6. |
| **R2** | Nuitka build překročí 150 MB | Nízký | Střední | Optimalizovat přes `--lto`, fallback PyInstaller. |
| **R3** | llama.cpp API se změní během vývoje | Střední | Nízká | Verze `llama-cpp-python` pinovaná v `pyproject.toml`. |
| **R4** | Rozsah hobby projektu překročí kapacitu autora | Vysoký | Vysoká | Přísná atomizace; v2 features odložit; milestone-gate. |
| **R5** | Vision modely budou mít vysokou chybovost JSON výstupu | Střední | Střední | JSONEnforcer retry + fallback na raw output v UI. |

---

## 13. Dependencies a předpoklady

**Externí závislosti:**
- Ollama runtime (pro MVP) — uživatel si instaluje sám.
- Předpoklad, že GGUF modely uvedené v `config.toml` existují na disku.

**Předpoklady:**
- Uživatel má Linux a základní znalost instalace balíčků.
- Dostupné GGUF modely jsou kompatibilní s aktuální verzí llama.cpp.

---

## 14. Open questions

| # | Otázka | Vlastník | Deadline |
|---|---|---|---|
| Q1 | Jaká licence? (MIT / Apache 2.0 / GPL-3.0) | Autor | Před v1.0 release |
| Q2 | Bude projekt publikovaný na GitHubu od začátku? | Autor | Před M1 |
| Q3 | Bude existovat možnost přispívání komunitou (CONTRIBUTING.md)? | Autor | Před v1.0 |
| Q4 | Podpora Flatpak/AppImage vedle ELF? | Autor | Před M5 |

---

## 15. Appendices

<details>
<summary><strong>📎 A — Glosář pojmů</strong></summary>

| Pojem | Význam |
|---|---|
| **Chain** | Sekvence modelů, kterými vstup projde; výstup kroku $N$ je kontextem kroku $N+1$. |
| **Recept** | Předdefinovaný chain pro konkrétní use-case. |
| **Adapter** | Konkrétní implementace `LLMAdapterBase` pro daný backend. |
| **JSON mode** | Režim LLM, kdy je model instruován produkovat pouze validní JSON. |
| **TTFT** | Time To First Token. |
| **COSMIC** | Desktop Environment od System76 (Pop!_OS Epoch 1). |
| **GGUF** | Binární formát modelů pro llama.cpp. |
</details>

<details>
<summary><strong>📎 B — Návaznost na ostatní dokumenty</strong></summary>

- **Technická specifikace v1.0** — atomický rozklad modulů (A1.x–A4.x), kontrakty, Definition of Done.
- **Implementační guide pro AI agenta** — instrukce pro kódovacího asistenta.
- **Default `config.toml` šablona** — runtime konfigurace.
</details>

---

### Schvalovací blok

| Role | Jméno | Datum | Status |
|---|---|---|---|
| Product Owner | _(autor projektu)_ | — | ⏳ K doplnění |
| Tech Lead | _(autor projektu)_ | — | ⏳ K doplnění |

---

*AXONEX PRD v1.0 — Draft pro hobby projekt · 24. 04. 2026*