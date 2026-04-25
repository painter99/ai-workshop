# AXONEX — Registr hypotéz a experimentů

| Položka | Hodnota |
|---|---|
| **Projekt** | AXONEX — Local Multi-Model Pipeline Orchestrator |
| **Dokument** | Hypothesis Registry & Experiment Log |
| **Verze** | 1.0 (prázdná šablona) |
| **Datum založení** | 24. 04. 2026 |
| **Vlastník** | Autor projektu |
| **Status** | 🟢 Živý dokument — průběžně aktualizovaný |

---

## 📖 Úvod a účel dokumentu

Tento dokument slouží jako **centrální registr všech hypotéz, předpokladů a experimentů** prováděných v rámci projektu AXONEX. Každé technické či produktové rozhodnutí, které není zcela jisté, má být zde **formálně zaznamenáno, otestováno a uzavřeno** (validováno / vyvráceno).

### Proč vést hypotézy?

| Důvod | Přínos |
|---|---|
| **Traceability** | Víme, proč jsme udělali konkrétní rozhodnutí, i za 6 měsíců. |
| **Redukce rizika** | Každý předpoklad je vědomě pojmenovaný a ověřený, nikoli „nějak se to vyřeší". |
| **Učení** | Vyvrácené hypotézy jsou cenné — dokumentují slepé uličky. |
| **Scope discipline** | Hypotézy brání feature creepu; bez validace se nepokračuje. |
| **Komunikace** | Případní přispěvatelé rychle pochopí rozhodovací kontext. |

### Jak tento dokument používat

1. **Každá nejistota → hypotéza.** Nezačínej implementaci modulu, pokud máš >20 % pochybnost o technologické volbě.
2. **Hypotéza má vždy falsifikační kritérium.** Pokud ji nelze vyvrátit, není to hypotéza, ale přesvědčení.
3. **Experiment → záznam → rozhodnutí → changelog.** Nikdy nepřeskakuj záznam výsledku.
4. **Status updaty jsou povinné.** Otevřená hypotéza starší než 30 dní je buď priorita, nebo se odkládá (`DEFERRED`).

---

## 🗂️ Taxonomie hypotéz

### Kategorie (použij jako prefix ID)

| Prefix | Kategorie | Příklady |
|---|---|---|
| **H-TECH** | Technologická volba | Framework, knihovna, build tool |
| **H-PERF** | Výkon / latence | TTFT, startup time, memory footprint |
| **H-UX** | Uživatelské rozhraní a zkušenost | Layout, interakce, responzivnost |
| **H-ARCH** | Architektonický vzor | Abstrakce, vrstvení, modularita |
| **H-MODEL** | LLM modely a inference | Volba modelu, prompt strategie, JSON reliability |
| **H-BUILD** | Kompilace a distribuce | Binary size, packaging, platform compat |
| **H-PROD** | Produktová hypotéza | User need, use case fit, workflow value |
| **H-OPS** | Provoz a spolehlivost | Error handling, logging, recovery |

### Statusy hypotézy

| Status | Emoji | Význam |
|---|---|---|
| `PROPOSED` | 💡 | Hypotéza sepsaná, zatím neověřovaná |
| `IN_EXPERIMENT` | 🔬 | Probíhá experiment / spike |
| `VALIDATED` | ✅ | Potvrzena daty → promítnuto do rozhodnutí |
| `REJECTED` | ❌ | Vyvrácena → alternativní řešení zvoleno |
| `DEFERRED` | ⏸️ | Odloženo na pozdější milestone |
| `OBSOLETE` | 🗑️ | Ztratila relevanci (kontext se změnil) |

### Priorita

| Priorita | Kritérium |
|---|---|
| **P0 — Blocker** | Bez vyřešení nelze pokračovat v aktuálním milestonu. |
| **P1 — Vysoká** | Blokuje další milestone nebo má velký dopad na architekturu. |
| **P2 — Střední** | Ovlivňuje kvalitu, ale existuje fallback. |
| **P3 — Nízká** | Optimalizace nebo kosmetika. |

### Confidence levels

| Úroveň | Definice |
|---|---|
| **High (≥ 80 %)** | Silné indicie z dokumentace/benchmarků/PoC |
| **Medium (50–79 %)** | Zkušenost říká ano, ale chybí tvrdá data |
| **Low (< 50 %)** | Odhad / intuice / analogie z jiných projektů |

---

## 📐 Formát zápisu hypotézy

Každá hypotéza se zapisuje do sekce **§ 4. Registr hypotéz** podle následující šablony. Šablonu zkopíruj a vyplň pro každou novou hypotézu.

---

### 🔖 ŠABLONA — Jednotlivá hypotéza

```markdown
### H-XXXX-NNN — [Stručný název hypotézy]

| Atribut | Hodnota |
|---|---|
| **ID** | H-XXXX-NNN |
| **Kategorie** | TECH / PERF / UX / ARCH / MODEL / BUILD / PROD / OPS |
| **Status** | 💡 PROPOSED |
| **Priorita** | P0 / P1 / P2 / P3 |
| **Confidence (initial)** | High / Medium / Low |
| **Autor** | — |
| **Vytvořeno** | YYYY-MM-DD |
| **Poslední update** | YYYY-MM-DD |
| **Cílový milestone** | M1 / M2 / … |
| **Vázáno na moduly** | A1.2a, A3.4, … |
| **Related hypotézy** | H-TECH-002, H-PERF-001 |

#### 📝 Znění hypotézy
> _Jednou větou ve formátu: „Věříme, že [akce/volba] povede k [výsledek], protože [důvod]."_

#### 🎯 Kontext a motivace
_Proč tuto hypotézu zkoumáme? Jaké rozhodnutí na ní závisí? Co se stane, když ji ignorujeme?_

#### 🔍 Falsifikační kritérium
_Jak poznáme, že je hypotéza NEPRAVDIVÁ? Musí být měřitelné a specifické._

- **Prahová hodnota:** …
- **Metrika:** …
- **Metoda měření:** …

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | … | … |
| 2 | … | … |
| 3 | … | … |

**Odhadovaný časový rozpočet:** X hodin
**Potřebné zdroje:** HW, knihovny, testovací data

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
- **Plán B:** …
- **Plán C:** …

#### 📊 Výsledky experimentu
_Vyplnit po provedení experimentu._

- **Datum experimentu:** YYYY-MM-DD
- **Skutečně naměřeno:** …
- **Interpretace:** …
- **Artefakty:** (odkazy na benchmark skripty, screenshoty, logy)

#### 🏁 Rozhodnutí
_Konečný verdikt a jeho zdůvodnění._

- **Status final:** VALIDATED / REJECTED / DEFERRED
- **Rozhodnutí:** …
- **Dopad na PRD / Tech spec:** (odkaz na sekci, která byla upravena)

#### 📚 Získané poznatky (Lessons learned)
_Co jsme se naučili? Co bychom příště udělali jinak?_

#### 🔗 Reference
- [Odkaz 1](…)
- [Odkaz 2](…)
```

---

## 📋 Rychlý přehled (Index)

> **Pokyn:** Tato tabulka se aktualizuje při každé změně statusu hypotézy. Slouží jako „dashboard" stavu projektu.

| ID | Název | Kategorie | Priorita | Status | Milestone | Poslední update |
|---|---|---|---|---|---|---|
| _(zatím prázdné — doplnit při vytvoření první hypotézy)_ | | | | | | |

### Statistika registru (aktualizovat ručně nebo skriptem)

| Status | Počet |
|---|---:|
| 💡 PROPOSED | 0 |
| 🔬 IN_EXPERIMENT | 0 |
| ✅ VALIDATED | 0 |
| ❌ REJECTED | 0 |
| ⏸️ DEFERRED | 0 |
| 🗑️ OBSOLETE | 0 |
| **Celkem** | **0** |

---

## 4. Registr hypotéz

> Tato sekce obsahuje **všechny hypotézy projektu**. Každá hypotéza je samostatný podsekce vycházející z výše uvedené šablony. Hypotézy jsou seřazeny **podle ID v rámci kategorie**.

### 4.1 Technologické hypotézy (H-TECH)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy z PRD — k převedení do plné šablony</strong></summary>

Následující hypotézy byly identifikovány v PRD / Technické specifikaci jako „otevřené otázky k ověření před M1". Každou z nich je třeba rozpracovat do plné šablony výše.

| Návrh ID | Stručné znění | Výchozí volba |
|---|---|---|
| `H-TECH-001` | Flet zvládne COSMIC vizuální jazyk (zaoblené rohy, accent barvy, tiling-aware layout) stejně dobře jako PySide6 + libadwaita. | Flet |
| `H-TECH-002` | Nuitka vyprodukuje standalone binárku pod 150 MB se startup time pod 3 s. | Nuitka |
| `H-TECH-003` | Čisté `httpx` poskytne lepší kontrolu nad streaming granularity než `ollama-python`. | httpx |
| `H-TECH-004` | TOML je pro konfiguraci čitelnější a udržitelnější než YAML/JSON v kontextu tohoto projektu. | TOML |
| `H-TECH-005` | `llama-cpp-python` bindings poskytnou stejný kontrakt jako subprocess wrapper nad llama.cpp binárkou, s menší provozní režií. | `llama-cpp-python` |

</details>

---

_(zde následují plně rozepsané hypotézy dle šablony; při vytvoření nové zkopíruj šablonu z § „Formát zápisu hypotézy")_

### 4.2 Výkonnostní hypotézy (H-PERF)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-PERF-001` | TTFT pro Ollama backend zůstane pod 500 ms při modelu do 9 B parametrů na doporučeném HW. |
| `H-PERF-002` | Streaming latence per token zůstane pod 100 ms při použití llama.cpp direct integration. |
| `H-PERF-003` | Flet UI nebude blokovat vykreslování při streamingu > 50 tokenů/s. |

</details>

### 4.3 UX hypotézy (H-UX)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-UX-001` | Drag & Drop na hybridní InputZone je pro uživatele intuitivnější než samostatná „Upload" tlačítka. |
| `H-UX-002` | Sidebar s recepty (bez multi-level menu) je dostatečný pro ≤ 10 receptů. |
| `H-UX-003` | Non-blocking toast notifikace v ErrorOverlay nezpůsobí, že uživatel přehlédne kritickou chybu. |

</details>

### 4.4 Architektonické hypotézy (H-ARCH)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-ARCH-001` | Abstrakce `LLMAdapterBase` umožní výměnu backendu změnou jediné hodnoty v `config.toml` bez regrese. |
| `H-ARCH-002` | Recepty jako plug-in moduly v `recipes/` umožní přidání nového use-case bez zásahu do jádra. |
| `H-ARCH-003` | `BranchRouter` založený na lambda podmínkách nad JSON klíči je dostatečně expresivní pro plánované use-casy. |

</details>

### 4.5 Model-level hypotézy (H-MODEL)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-MODEL-001` | LFM2.5-VL-1.6B-Q8_0 produkuje validní JSON dle `InvoiceSchema` v ≥ 80 % případů bez retry. |
| `H-MODEL-002` | JSONEnforcer s max 3 retry dosáhne ≥ 95 % úspěšnosti validního JSON výstupu na testovací sadě. |
| `H-MODEL-003` | Qwopus3.5-9B Q4_K_M zvládne českou sumarizaci na úrovni srovnatelné s cloudovými modely pro běžné faktury. |

</details>

### 4.6 Build a distribuce (H-BUILD)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-BUILD-001` | Nuitka `--onefile --standalone` vyprodukuje spustitelný ELF na čistém Pop!_OS 22.04 bez dodatečných závislostí. |
| `H-BUILD-002` | `.desktop` integrace zobrazí aplikaci korektně v COSMIC App Grid včetně ikony. |

</details>

### 4.7 Produktové hypotézy (H-PROD)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-PROD-001` | Cílová persona „Tomáš" zvládne spustit recept R1 (faktura) do 5 minut od prvního otevření aplikace. |
| `H-PROD-002` | Tři výchozí recepty (faktura, kód, dokument) pokryjí ≥ 70 % reálných use-case potřeb early-adopterů. |

</details>

### 4.8 Provoz a spolehlivost (H-OPS)

<details>
<summary><strong>🔭 Předvyplněné kandidátní hypotézy</strong></summary>

| Návrh ID | Stručné znění |
|---|---|
| `H-OPS-001` | Startup health-check spolehlivě detekuje nedostupný Ollama backend do 2 s. |
| `H-OPS-002` | JSON strukturované logy (`structlog`) umožní rekonstrukci chainu post-mortem z jediného log souboru. |

</details>

---

## 5. Review proces

### 5.1 Kadence review

| Frekvence | Akce |
|---|---|
| **Před každým milestonem** | Projít všechny hypotézy s cílovým milestonem = aktuální; vyřešit všechny P0. |
| **Týdně** (solo developer) | Projít `IN_EXPERIMENT` hypotézy, rozhodnout o pokračování. |
| **Měsíčně** | Projít `PROPOSED` starší než 30 dní — buď priorita nebo `DEFERRED`. |
| **Ad-hoc** | Při změně architektury projít všechny `VALIDATED` hypotézy pro potvrzení stále platnosti. |

### 5.2 Kdo rozhoduje

V hobby kontextu je rozhodovací autorita autor projektu. Přesto je doporučeno:
- Při zásadních architektonických rozhodnutích (změna backend abstrakce, UI framework) požádat o **second opinion** (komunita, forum, AI asistent).
- Dokumentovat i zamítnuté alternativy, aby budoucí „já" nemuselo opakovat analýzu.

---

## 6. Anti-patterns — čemu se vyhnout

| Anti-pattern | Proč je špatně | Lepší přístup |
|---|---|---|
| **„Vím, že to bude fungovat"** bez testu | Bias, iluze jistoty | Napsat hypotézu + min. 30min spike |
| **Hypotéza bez falsifikačního kritéria** | Nelze ji nikdy zavřít | Vždy uveď měřitelnou prahovou hodnotu |
| **Validace vlastními přáními** | Sebe-podvod | Definovat kritérium PŘED experimentem |
| **Zapomenout zavřít hypotézu po validaci** | Registr hnije | Changelog + update PRD v rámci stejného commitu |
| **Hypotézy jako „todo list"** | Mísí tasky a nejistoty | Jasně oddělit: task = JAK; hypotéza = CO/PROČ |
| **Příliš široká hypotéza** | „Flet je dobrý" nelze otestovat | Rozbít na specifické: „Flet zvládne X pod Y ms" |

---

## 7. Workflow zpracování hypotézy (Lifecycle)

```
┌──────────────┐
│ 💡 PROPOSED  │  ← vytvořena v registru
└──────┬───────┘
       │ priorita stanovena, experiment naplánován
       ▼
┌──────────────┐
│ 🔬 IN_EXPER. │  ← probíhá spike / benchmark / PoC
└──────┬───────┘
       │ výsledky zaznamenány
       ▼
   ┌───┴────┐
   ▼        ▼
┌─────┐  ┌─────┐
│ ✅  │  │ ❌  │
│VALID│  │REJCT│
└──┬──┘  └──┬──┘
   │        │
   ▼        ▼
 update    update
 PRD +     PRD +
 tech      výběr
 spec      plánu B
```

---

## 8. Changelog dokumentu

| Datum | Verze | Změna | Autor |
|---|---|---|---|
| 2026-04-24 | 1.0 | Založení šablony registru hypotéz | — |
| _YYYY-MM-DD_ | _1.x_ | _popis změny_ | _autor_ |

---

## 9. Appendices

<details>
<summary><strong>📎 A — Checklist před založením nové hypotézy</strong></summary>

Před přidáním nové hypotézy si projdi následující checklist:

- [ ] Je to opravdu **nejistota**, ne úkol? (úkol patří do issue trackeru, ne sem)
- [ ] Dokážu definovat **falsifikační kritérium** s konkrétní prahovou hodnotou?
- [ ] Mám plán experimentu s časovým odhadem?
- [ ] Existují **alternativy** (Plán B), pokud bude hypotéza vyvrácena?
- [ ] Není už **podobná hypotéza** v registru? (zkontroluj index)
- [ ] Je **priorita** nastavena v souladu s aktuálním milestonem?
- [ ] Je hypotéza navázána na konkrétní moduly / sekce PRD?

</details>

<details>
<summary><strong>📎 B — Šablona experimentálního logu (spike notes)</strong></summary>

Pro každý experiment veď stručný samostatný log. Doporučené umístění: `docs/experiments/H-XXXX-NNN_spike.md`.

```markdown
# Spike log — H-XXXX-NNN [název]

**Datum:** YYYY-MM-DD
**Časový rozpočet:** X h (plánováno) / Y h (skutečně)
**Prostředí:** (OS, HW, verze knihoven)

## Cíl spike
_Co konkrétně chci změřit/ověřit?_

## Setup
_Kroky k reprodukci (commity, data, config)._

## Měření / pozorování
| Iterace | Vstup | Výstup | Metrika |
|---|---|---|---|
| 1 | … | … | … |

## Závěr
_Hypotéza podporována / vyvrácena? Confidence po experimentu?_

## Artefakty
- `benchmark.py`
- `results.csv`
- screenshot.png
```

</details>

<details>
<summary><strong>📎 C — Příklad vyplněné hypotézy (referenční)</strong></summary>

_Příklad je ilustrativní a neodráží skutečné měření — slouží jako šablona stylu._

### H-PERF-001 — TTFT pod 500 ms s Ollama backendem

| Atribut | Hodnota |
|---|---|
| **ID** | H-PERF-001 |
| **Kategorie** | PERF |
| **Status** | 💡 PROPOSED |
| **Priorita** | P0 |
| **Confidence (initial)** | Medium |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-24 |
| **Poslední update** | 2026-04-24 |
| **Cílový milestone** | M1 |
| **Vázáno na moduly** | A1.2a (OllamaAdapter), A1.3 (StreamHandler) |
| **Related hypotézy** | H-TECH-003 |

#### 📝 Znění hypotézy
> Věříme, že Ollama backend s modelem do 9 B parametrů dosáhne TTFT pod 500 ms na doporučeném HW (RTX 3060+), protože llama.cpp vrstva pod Ollamou má nativní GPU podporu a síťová režie localhost HTTP je zanedbatelná.

#### 🎯 Kontext a motivace
TTFT je klíčové UX kritérium (FR-3, NFR 6.1). Pokud by TTFT překročilo 500 ms, celková percepce aplikace jako „nativní" padá.

#### 🔍 Falsifikační kritérium
- **Prahová hodnota:** TTFT > 500 ms v > 20 % měření z 50 pokusů
- **Metrika:** medián a p95 TTFT v ms
- **Metoda měření:** Python timer mezi odesláním requestu a přijetím prvního tokenu přes `httpx` stream

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | Nainstalovat Ollama + stáhnout `qwen2.5:7b` | Model připravený |
| 2 | Napsat `benchmark_ttft.py` s 50 průchody | CSV s měřeními |
| 3 | Spustit na cílovém HW, vypočítat percentily | p50, p95 |

**Odhadovaný časový rozpočet:** 3 h
**Potřebné zdroje:** RTX 3060+, 16 GB RAM

#### 🔀 Alternativní řešení
- **Plán B:** Použít menší model (3 B) a akceptovat kvalitativní kompromis.
- **Plán C:** Přeskočit MVP na llama.cpp direct integration dříve.

#### 📊 Výsledky experimentu
_Dosud neproběhl._

#### 🏁 Rozhodnutí
_Čeká na experiment._

#### 📚 Získané poznatky
—

#### 🔗 Reference
- [Ollama FAQ — performance](https://github.com/ollama/ollama/blob/main/docs/faq.md)

</details>

---

*AXONEX Hypothesis Registry v1.0 — Prázdná šablona k postupnému naplňování · 24. 04. 2026*