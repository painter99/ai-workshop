# AXONEX — Development Toolstack

> **Charakter tohoto dokumentu:** Nejde o striktní příkaz. Je to živá dohoda mezi Pavlem a AI agentem o tom, které nástroje jsou k dispozici a kdy je nejlepší čas je použít. AI agent by měl sám identifikovat vhodný moment a připomenout použití — ne čekat, až se na to Pavel zeptá.

---

## Kontext

AXONEX je malý personal project (local multi-model Python pipeline, ~100–300 řádků). Toolstack tomu odpovídá — žádné enterprise přepalby, jen to, co reálně přidává hodnotu při skromném rozsahu projektu.

---

## Aktivní toolstack (co SKUTEČNĚ použijeme)

### 1. `development` skill — Hlavní motor
**Kdy:** Každý coding task bez výjimky.
**Jak:** SPEC → PLAN → BUILD → TEST → REVIEW → SHIP
**Trigger pro AI agenta:** Kdykoliv Pavel začne popisovat novou funkci, bug, nebo říká "začněme programovat" → okamžitě navrhnout použití development skill.

---

### 2. `context-engineering` skill — Orientace v souborech
**Kdy:** Na začátku každé vývojové session; když agent začíná ztrácet nitku mezi dokumenty.
**Jak:** Strukturované načtení správných souborů ve správném pořadí:
```
1. PLAN_LEHKY_START.md       — aktuální krok a stav
2. docs/tech_spec.md         — technická architektura
3. docs/prd.md               — product requirements
4. SESSION_SUMMARY_*.md      — co bylo hotovo minule
```
**Trigger pro AI agenta:** Na začátku každé session s AXONEX; pokud agent odpoví na něco, co neodpovídá dokumentaci → zastavit a načíst kontext.

---

### 3. `a0_agent_skills` → `code-reviewer` + `test-engineer` (Agent Skills — Engineering Lifecycle)
**Kdy:**
- `code-reviewer`: před každým git commitem, při nejistotě o kvalitě
- `test-engineer`: po implementaci každé funkce, pro psaní testů
**Jak:** Delegovat přes `call_subordinate` s odpovídajícím profile.
**Jak:** Delegovat přes `call_subordinate` s odpovídajícím profilem (např. `code-reviewer`, `test-engineer`).

---

### 4. `karpathy_guidelines` plugin
**Kdy:** Trvale aktivní (background) — stačí jednou zapnout v Settings.
**Jak:** Auto-inject do každé konverzace: think first, simplicity, surgical changes.
**Trigger pro AI agenta:** Pokud vidí, že se přidává zbytečná složitost → připomenout Karpathy principles.

---

### 5. `context_indicator` plugin
**Kdy:** Trvale aktivní (background) — stačí jednou zapnout v Settings.
**Jak:** Ukazuje % využití kontextového okna v UI.
**Trigger pro AI agenta:** Pokud context_indicator ukazuje >70% → navrhnout Pavlovi začít novou session nebo provést compact.

---

## Co NEVYUŽIJEME — a proč

| Nástroj | Důvod |  
|---------|-------|
| `parallel_swarm` | Přepalba pro 100–300 řádkový projekt. Zvážit až při multi-modulárním rozšíření. |
| `rlm` | Pro naše malé soubory zbytečné. Hodí se až na 1000+ řádků logů/dokumentů. |
| `a0_playwright_cli` | AXONEX nemá web UI v první fázi (jen CLI/terminal). |
| `docker_terminal` | Redundantní — terminál je dostupný jinak. |
| `create-skill` skill | Nepíšeme skilly, píšeme Python. |
| `semishape`, `telegram`, `theme_plugin` | Mimo scope AXONEX. |

---

## Kdy přehodnotit toolstack

- AXONEX přeroste 300 řádků a rozroste se do více modulů → zvážit `parallel_swarm`
- Budeme zpracovávat velké logy nebo dokumenty (1000+ řádků) → zvážit `rlm`
- AXONEX dostane web UI → zvážit `a0_playwright_cli`

---

## Instrukce pro AI agenta

> Toto je klíčová sekce. AI agent by měl aktivně a proaktivně připomínat použití nástrojů — **ne čekat, až se Pavel zeptá**.

### Proaktivní triggery pro agenta

| Situace | Doporučená akce agenta |
|---------|------------------------|
| Pavel popíše nový feature/krok z PLAN_LEHKY_START.md | Navrhnout: "Začneme přes development skill — SPEC/PLAN fázi?" |
| Konverzace začíná a mluví se o AXONEX | Ověřit kontext: načíst PLAN_LEHKY_START.md + SESSION_SUMMARY |
| Implementace je hotová | Navrhnout: "Chceš code-reviewer před commitem?" |
| Kód je otestován a schválen | Připomenout: "Commitujeme? Jedeme přes SHIP fázi development skill." |
| Context indicator >70% | Upozornit: "Blížíme se k limitu kontextu — doporučuji novou session nebo compact." |
| Přidává se složitost nad rámec PLAN_LEHKY_START.md | Upozornit: "Karpathy: simplicity first — toto je mimo aktuální scope AXONEX fáze A–D." |

### Tón doporučení
- Krátký, přátelský, bez moralyzování
- Pavel rozhoduje — agent jen připomíná a navrhuje

---

## Sdílení tohoto dokumentu

Tento dokument je **veřejně bezpečný** a nepatří do `.gitignore`.

- Neobsahuje žádné API klíče, hesla, osobní údaje ani citlivá data
- Neobsahuje finanční informace (platy, budgety)
- Je to čistě technická dokumentace vývojového postupu
- **Rozhodnutí: Sdílet veřejně** — je cenným příkladem toho, jak lze strukturovat AI-asistovaný vývoj
- Zároveň slouží jako transparentní record toho, jak pracujeme

---

## Synergie s AXONEX fázemi (PLAN_LEHKY_START.md)

| Fáze AXONEX | Primární nástroje |
|-------------|-------------------|
| A — Config + Ollama init | development skill (SPEC+PLAN+BUILD) |
| B — První prompt chain | development skill (BUILD+TEST) + test-engineer |
| C — Výstup do souboru | development skill (BUILD) + code-reviewer |
| D — JSON parse + validace | development skill (BUILD+TEST) + test-engineer + code-reviewer |
| Každý commit | development skill (SHIP) |

---

*Poslední aktualizace: 2026-04-26*
*Umístění: `/a0/usr/workdir/ai-workshop/projects/axonex/DEVELOPMENT_TOOLSTACK.md`*
