# AXONEX — Aktivní hypotézy (M1 kritické)

| Položka | Hodnota |
|---|---|
| **Projekt** | AXONEX — Local Multi-Model Pipeline Orchestrator |
| **Dokument** | Aktivní hypotézy — rozpracované do plné šablony |
| **Verze** | 1.0 |
| **Datum** | 2026-04-25 |
| **Status** | 🟢 Připraveno k experimentům |

---

## 📋 Rychlý přehled (Index)

| ID | Název | Kategorie | Priorita | Status | Milestone | Poslední update |
|---|---|---|---|---|---|---|
| H-TECH-001 | Flet zvládne COSMIC vizuální jazyk | TECH | P0 | 💡 PROPOSED | M1 | 2026-04-25 |
| H-TECH-002 | Nuitka vyprodukuje binárku < 150 MB | TECH | P0 | 💡 PROPOSED | M1 | 2026-04-25 |
| H-TECH-003 | httpx poskytne lepší kontrolu než ollama-python | TECH | P1 | 💡 PROPOSED | M1 | 2026-04-25 |
| H-PERF-001 | TTFT < 500 ms s Ollama backendem | PERF | P0 | 💡 PROPOSED | M1 | 2026-04-25 |
| H-ARCH-001 | LLMAdapterBase umožní bezregresní swap backendu | ARCH | P1 | 💡 PROPOSED | M2 | 2026-04-25 |

### Statistika registru

| Status | Počet |
|---|---:|
| 💡 PROPOSED | 5 |
| 🔬 IN_EXPERIMENT | 0 |
| ✅ VALIDATED | 0 |
| ❌ REJECTED | 0 |
| ⏸️ DEFERRED | 0 |
| 🗑️ OBSOLETE | 0 |
| **Celkem** | **5** |

---

## 4. Registr hypotéz — plně rozpracované

---

### H-TECH-001 — Flet zvládne COSMIC vizuální jazyk

| Atribut | Hodnota |
|---|---|
| **ID** | H-TECH-001 |
| **Kategorie** | TECH |
| **Status** | 💡 PROPOSED |
| **Priorita** | P0 |
| **Confidence (initial)** | Medium |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-25 |
| **Poslední update** | 2026-04-25 |
| **Cílový milestone** | M1 |
| **Vázáno na moduly** | A3.1 (CosmicWindow), A3.2 (UseCaseSelector), A3.3 (InputZone) |
| **Related hypotézy** | H-TECH-002 |

#### 📝 Znění hypotézy
> Věříme, že Flet (Flutter-based) dokáže vizuálně imitovat COSMIC Desktop design language (tmavé téma #1a1a1a, accent #f6b73c, zaoblené rohy 8–12 px, tiling-aware layout) dostatečně přesvědčivě, protože Flutter podporuje custom theming a Flet poskytuje kontrolu nad barvami, border radius a layout responsivitou.

#### 🎯 Kontext a motivace
COSMIC look & feel je klíčové UX kritérium (FR-7, NFR 6.3). Pokud Flet nezvládne vizuální soulad, celá UI vrstva musí být přepsaná v PySide6 + libadwaita, což je zásadní architektonická změna.

#### 🔍 Falsifikační kritérium
- **Prahová hodnota:** Aplikace vypadá vizuálně cizorodě v COSMIC prostředí (hodnocení „neakceptovatelné" v subjektivním testu)
- **Metrika:** Binární + subjektivní hodnocení (1–5, kde 4+ = akceptovatelné)
- **Metoda měření:** Spustit 20řádkový Flet app v COSMIC, porovnat s nativními aplikacemi (např. COSMIC Terminal, COSMIC Files)

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | Nainstalovat Flet (`pip install flet`) | Flet dostupný v prostředí |
| 2 | Napsat `test_cosmic_look.py` s tmavým tématem, accent barvou, zaoblenými rohy | Flet okno se zobrazí |
| 3 | Spustit v COSMIC Desktop, porovnat vzhled | Fotografie/screenshot |
| 4 | Otestovat tiling behavior (přichycení k okraji) | Okno se chová korektně v tiling WM |

**Odhadovaný časový rozpočet:** 1 hodina
**Potřebné zdroje:** COSMIC Desktop prostředí (Pop!_OS 22.04+), Flet ≥ 0.24

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
- **Plán B:** PySide6 + libadwaita pro autentický GTK/COSMIC vzhled
- **Plán C:** Tauri (Rust) + Python backend via IPC (výrazně větší režie)

#### 📊 Výsledky experimentu
_Dosud neproběhl._

#### 🏁 Rozhodnutí
_Čeká na experiment._

#### 📚 Získané poznatky
—

#### 🔗 Reference
- [Flet docs — Theming](https://flet.dev/docs/cookbook/theming)
- [COSMIC Design guidelines](https://github.com/pop-os/cosmic)

---

### H-TECH-002 — Nuitka vyprodukuje standalone binárku pod 150 MB

| Atribut | Hodnota |
|---|---|
| **ID** | H-TECH-002 |
| **Kategorie** | TECH |
| **Status** | 💡 PROPOSED |
| **Priorita** | P0 |
| **Confidence (initial)** | Low |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-25 |
| **Poslední update** | 2026-04-25 |
| **Cílový milestone** | M5 |
| **Vázáno na moduly** | A4.1 (Nuitka Build) |
| **Related hypotézy** | H-TECH-001, H-BUILD-001 |

#### 📝 Znění hypotézy
> Věříme, že Nuitka zkompiluje AXONEX (Python + Flet + Pydantic + httpx) do standalone ELF binárky pod 150 MB se startup time pod 3 s, protože Nuitka provádí C-kompilaci Python kódu a `--onefile --standalone` eliminuje runtime závislosti.

#### 🎯 Kontext a motivace
Distribuce jako jediný binární soubor je klíčový produktový cíl (G4, FR-10). Pokud binárka překročí 150 MB nebo startup bude > 3 s, percepce „lehké nativní aplikace" padá.

#### 🔍 Falsifikační kritérium
- **Prahová hodnota:** Binárka > 150 MB NEBO startup > 3 s na doporučeném HW
- **Metrika:** Velikost souboru (MB), cold startup time (s)
- **Metoda měření:** `ls -lh axonex`, `time ./axonex` na čistém Pop!_OS (bez Pythonu)

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | Vytvořit minimální Flet app (Hello World) | `hello.py` |
| 2 | Zkompilovat přes Nuitka (`--onefile --standalone`) | `hello.bin` |
| 3 | Změřit velikost a startup time | Velikost < 50 MB, startup < 2 s |
| 4 | Přidat Pydantic + httpx, zopakovat měření | Velikost < 100 MB, startup < 3 s |
| 5 | Přidat llama-cpp-python, zopakovat měření | Velikost < 150 MB, startup < 3 s |

**Odhadovaný časový rozpočet:** 3 hodiny
**Potřebné zdroje:** Pop!_OS 22.04+, Nuitka, dostatek diskového prostoru

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
- **Plán B:** PyInstaller (větší binárka, ale jednodušší konfigurace)
- **Plán C:** Distribuce jako Python package (`pip install axonex`) místo binárky
- **Plán D:** AppImage místo standalone ELF

#### 📊 Výsledky experimentu
_Dosud neproběhl._

#### 🏁 Rozhodnutí
_Čeká na experiment._

#### 📚 Získané poznatky
—

#### 🔗 Reference
- [Nuitka docs — Standalone](https://nuitka.net/doc/user-manual.html#standalone-program)
- [Nuitka Commercial — Onefile](https://nuitka.net/doc/commercial.html)

---

### H-TECH-003 — Čisté httpx poskytne lepší kontrolu nad streaming granularity

| Atribut | Hodnota |
|---|---|
| **ID** | H-TECH-003 |
| **Kategorie** | TECH |
| **Status** | 💡 PROPOSED |
| **Priorita** | P1 |
| **Confidence (initial)** | Medium |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-25 |
| **Poslední update** | 2026-04-25 |
| **Cílový milestone** | M1 |
| **Vázáno na moduly** | A1.2a (OllamaAdapter), A1.3 (StreamHandler) |
| **Related hypotézy** | H-PERF-001 |

#### 📝 Znění hypotézy
> Věříme, že čisté `httpx` poskytne lepší kontrolu nad streaming granularity (token-by-token zpracování) než oficiální `ollama-python` knihovna, protože httpx umožňuje přímý přístup k raw SSE/NDJSON streamu bez abstrakční vrstvy.

#### 🎯 Kontext a motivace
Token-by-token streaming (FR-3) je klíčové UX kritérium. `ollama-python` může bufferovat nebo agregovat tokeny předtím, než je předá callbacku. Přímý httpx stream nám dává plnou kontrolu.

#### 🔍 Falsifikační kritérium
- **Prahová hodnota:** `httpx` stream neumožňuje spolehlivé token-by-token zpracování NEBO `ollama-python` poskytuje ekvivalentní granularitu s menší režií
- **Metrika:** Latence mezi přijetím tokenu a jeho zobrazením v UI (ms)
- **Metoda měření:** Porovnat `ollama-python` callback frekvenci vs. `httpx` raw stream chunk frekvenci

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | Nainstalovat `httpx` a `ollama-python` | Oba klienti dostupní |
| 2 | Napsat `benchmark_streaming.py` — obě varianty, 50 pokusů | CSV s latencemi per token |
| 3 | Spustit na cílovém HW s `qwen2.5:7b` | Porovnání mediánů a p95 |

**Odhadovaný časový rozpočet:** 2 hodiny
**Potřebné zdroje:** Ollama běžící lokálně, model qwen2.5:7b

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
- **Plán B:** Použít `ollama-python` pro M1, přepnout na httpx v M6 pokud se ukáže jako nutné
- **Plán C:** Implementovat vlastní wrapper nad `ollama-python` s nižší režií

#### 📊 Výsledky experimentu
_Dosud neproběhl._

#### 🏁 Rozhodnutí
_Čeká na experiment._

#### 📚 Získané poznatky
—

#### 🔗 Reference
- [httpx Streaming docs](https://www.python-httpx.org/quickstart/#streaming-responses)
- [ollama-python GitHub](https://github.com/ollama/ollama-python)

---

### H-PERF-001 — TTFT pod 500 ms s Ollama backendem

| Atribut | Hodnota |
|---|---|
| **ID** | H-PERF-001 |
| **Kategorie** | PERF |
| **Status** | 💡 PROPOSED |
| **Priorita** | P0 |
| **Confidence (initial)** | Medium |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-25 |
| **Poslední update** | 2026-04-25 |
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

**Odhadovaný časový rozpočet:** 3 hodiny
**Potřebné zdroje:** RTX 3060+, 16 GB RAM

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
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

---

### H-ARCH-001 — Abstrakce LLMAdapterBase umožní výměnu backendu bez regrese

| Atribut | Hodnota |
|---|---|
| **ID** | H-ARCH-001 |
| **Kategorie** | ARCH |
| **Status** | 💡 PROPOSED |
| **Priorita** | P1 |
| **Confidence (initial)** | High |
| **Autor** | autor |
| **Vytvořeno** | 2026-04-25 |
| **Poslední update** | 2026-04-25 |
| **Cílový milestone** | M2 |
| **Vázáno na moduly** | A1.2 (LLMAdapterBase), A1.2a (OllamaAdapter), A1.2b (LlamaCppAdapter) |
| **Related hypotézy** | H-TECH-005 |

#### 📝 Znění hypotézy
> Věříme, že abstrakce `LLMAdapterBase` (ABC) umožní přepnutí backendu z Ollama na llama.cpp změnou jediné hodnoty v `config.toml` bez regrese funkcionality, protože oba adaptery implementují identický kontrakt (`generate()`, `chat()`, `stream()`, `health_check()`).

#### 🎯 Kontext a motivace
Backend-agnostic design je klíčový strategický cíl (G3). Pokud abstrakce nefunguje, přechod Ollama → llama.cpp vyžaduje změny v mnoha modulech.

#### 🔍 Falsifikační kritérium
- **Prahová hodnota:** Přepnutí backendu vyžaduje změny v > 1 souboru NEBO způsobí selhání > 0 existujících testů
- **Metrika:** Počet změněných souborů při přepnutí, počet failing testů
- **Metoda měření:** Implementovat oba adaptery, napsat unit testy, provést swap a spustit testy

#### 🧪 Návrh experimentu
| Krok | Akce | Očekávaný výstup |
|---|---|---|
| 1 | Implementovat `LLMAdapterBase` (ABC) | Abstraktní třída s 4 metodami |
| 2 | Implementovat `OllamaAdapter` | Funkční adapter pro Ollama |
| 3 | Napsat unit testy proti ABC (ne konkrétnímu adapteru) | Testy passují s OllamaAdapter |
| 4 | Implementovat mock `LlamaCppAdapter` | Funkční adapter (mock nebo reálný) |
| 5 | Přepnout `config.toml` → llama.cpp, spustit testy | Stejné testy passují bez úprav |

**Odhadovaný časový rozpočet:** 4 hodiny
**Potřebné zdroje:** Ollama běžící lokálně, pytest, pytest-asyncio

#### 🔀 Alternativní řešení (pokud bude hypotéza vyvrácena)
- **Plán B:** Větší abstrakce s middleware vrstvou pro normalizaci rozdílů mezi backendy
- **Plán C:** Přijmout, že swap vyžaduje minimální změny v 2–3 souborech a dokumentovat je

#### 📊 Výsledky experimentu
_Dosud neproběhl._

#### 🏁 Rozhodnutí
_Čeká na experiment._

#### 📚 Získané poznatky
—

#### 🔗 Reference
- [Python ABC docs](https://docs.python.org/3/library/abc.html)
- [Strategy pattern — Refactoring Guru](https://refactoring.guru/design-patterns/strategy)

---

## 8. Changelog dokumentu

| Datum | Verze | Změna | Autor |
|---|---|---|---|
| 2026-04-25 | 1.0 | Rozpracování 5 kritických hypotéz do plné šablony | Agent Zero |

---

*AXONEX Active Hypotheses v1.0 — Připraveno k experimentům · 25. 04. 2026*
