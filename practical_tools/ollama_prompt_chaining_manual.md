# Prompt Chaining s Ollama: Kompletní technická dokumentace (Multi-Model)

**Systém:** Pop!_OS (nebo jakýkoli Ubuntu/Debian-based Linux)
**Modely:** `qwen3.5:9b` (analýza) + `granite4:tiny-h` (formátování)
**Metoda:** 2-fázový Multi-Model Prompt Chain přes Python skript s knihovnou `ollama`

---

## 1 — Co je Prompt Chaining a proč existuje

### Fundamentální problém: LLM modely jsou špatné multitaskery

Když do jednoho promptu vložíte současně požadavek na analýzu, strukturu, formátování, jazyk a styl, model se pokouší splnit všechny cíle najednou. Kapacita pozornosti (attention) je konečná — čím víc instrukcí v promptu, tím méně pozornosti dostane každá z nich.

Výsledek je předvídatelný:

| Co se stane | Proč |
|---|---|
| Začátek odpovědi je dobrý, konec se rozpadá | Instrukce ze systémového promptu postupně „vyblednou" |
| Model přestane vykat, přepne do angličtiny | Překonala se kapacita modelu udržet všechny omezení |
| Fakta jsou správná, ale formát špatný (nebo naopak) | Model obětoval jeden cíl ve prospěch druhého |

### Tři základní důvody existence Prompt Chainingu

**1. Princip jedné odpovědnosti** — každý krok dělá jednu věc. Fáze 1 řeší *co říct* (analýza). Fáze 2 řeší *jak to říct* (jazyk, formát, styl).

**2. Kontrola mezi kroky** — mezi fázemi můžete vidět meziprodukt a opravit ho, než ho pošlete dál. U jednoho mega-promptu vidíte až finální rozbitý výstup.

**3. Izolace chyb** — pokud selže Fáze 1, víte přesně kde. Nemusíte luštit, jestli problém byl v analýze, formátování, nebo jazyce.

### Multi-Model Prompt Chaining: Silný analytik + lehký pisatel

Klíčová výhoda Prompt Chainingu: každá fáze je nezávislé API volání. Kontext se předává explicitně jako text. To znamená, že **každá fáze může běžet na jiném modelu**:

```
Fáze 1: qwen3.5:9b        →  surová osnova (string)
                                    │
              prostý text, žádná magie
                                    ▼
Fáze 2: granite4:tiny-h   ←  osnova jako vstup v promptu
```

Modelu ve Fázi 2 je úplně jedno, kdo text vygeneroval. Dostane ho jako vstup v promptu — stejně jako kdybyste ho napsali ručně.

**Princip přiřazení modelů:**

| Typ úkolu | Náročnost | Model |
|---|---|---|
| Analýza, reasoning, identifikace kroků a rizik | Vysoká | Nejsilnější dostupný (`qwen3.5:9b`) |
| Rozepsání do odstavců, formátování, styl | Střední | Lehčí model stačí (`granite4:tiny-h`) |

### Známé nevýhody Prompt Chainingu

| Nevýhoda | Vysvětlení |
|---|---|
| **Vyšší latence** | Dvě sekvenční volání + přepnutí modelu v VRAM: $t_{total} = t_{F1} + t_{swap} + t_{F2}$ |
| **Propagace chyb** | Pokud Fáze 1 vygeneruje špatnou osnovu, Fáze 2 ji krásně naformátuje — ale obsah bude stále chybný. Řešení: kontrolovat meziprodukty (`DEBUG = True`). |
| **Vyšší spotřeba tokenů** | Fáze 2 dostává na vstupu celý výstup Fáze 1 plus nové instrukce |
| **VRAM přepínání** | Pokud se oba modely nevejdou do GPU paměti současně, Ollama musí jeden vyložit a druhý nahrát (~5–15 sekund) |

---

## 2 — Příprava systému: Ollama

### Krok 2.1: Ověření, že Ollama běží

Otevřete terminál a zadejte:

```bash
systemctl status ollama
```

- **Očekávaný výsledek:** Zelený nápis `active (running)`. Stiskněte `q` pro návrat do příkazové řádky.
- **Pokud neběží:**
  ```bash
  sudo systemctl start ollama
  ```
- **Pokud `systemctl` hlásí, že jednotka neexistuje** (některé instalace nepoužívají systemd):
  ```bash
  ollama serve
  ```
  > Tento příkaz nechte běžet v **samostatném okně terminálu** — blokuje ho.

### Krok 2.2: Ověření verze Ollama

Parametr `think=False` (nutný pro `qwen3.5`) vyžaduje **Ollama >= 0.9.0**:

```bash
ollama --version
```

Pokud máte starší verzi, aktualizujte:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Krok 2.3: Stažení modelů

Stáhněte oba modely, které skript používá:

```bash
ollama pull qwen3.5:9b
ollama pull granite4:tiny-h
```

### Krok 2.4: Ověření, že modely existují

```bash
ollama list
```

Ve výpisu musíte vidět řádky obsahující `qwen3.5:9b` a `granite4:tiny-h`. Přesné názvy musí odpovídat konstantám ve slovníku `MODELS` ve skriptu.

<details>
<summary>📝 Poznámka o použitých modelech</summary>

**qwen3.5:9b (Fáze 1 — Analytik)**
- **Výrobce:** Alibaba / Qwen Team
- **Parametry:** ~9B
- **Velikost na disku:** ~6.6 GB
- **Klíčová vlastnost:** Reasoning model s `<think>` blokem (proto musíme použít `think=False`)
- **Licence:** Apache 2.0

**granite4:tiny-h (Fáze 2 — Pisatel)**
- **Plný název:** `granite4:7b-a1b-h` (alias `granite4:tiny-h`)
- **Výrobce:** IBM
- **Architektura:** Hybrid Mamba-2 (proto `-h` v názvu)
- **Parametry:** ~6.94B
- **Kvantizace:** Q4_K_M (výchozí)
- **Velikost na disku:** ~4.2 GB
- **Podporované jazyky:** angličtina, němčina, španělština, francouzština, japonština, portugalština, arabština, **čeština**, italština, korejština, nizozemština, čínština
- **Licence:** Apache 2.0

</details>

---

## 3 — Příprava Python prostředí

### Krok 3.1: Instalace `venv` (pokud chybí)

```bash
sudo apt update && sudo apt install python3-venv -y
```

### Krok 3.2: Vytvoření virtuálního prostředí

```bash
python3 -m venv ~/ai-prostredi
```

### Krok 3.3: Aktivace prostředí

```bash
source ~/ai-prostredi/bin/activate
```

**Očekávaný výsledek:** Před promptem se objeví `(ai-prostredi)`.

### Krok 3.4: Instalace knihovny `ollama`

```bash
pip install ollama --upgrade
```

> **Ověření nainstalované verze:**
> ```bash
> python -c "import ollama; print(ollama.__version__)"
> ```
> Skript počítá s verzí **0.4+**. Pokud máte starší verzi, `pip install ollama --upgrade` ji aktualizuje.

---

## 4 — Python skript: `brainstorm.py`

### Krok 4.1: Vytvoření (editace) souboru

```bash
nano ~/brainstorm.py
```

### Krok 4.2: Obsah skriptu

Zkopírujte následující blok kódu a vložte jej do editoru (pomocí `Ctrl+Shift+V` nebo pravým tlačítkem myši).

```python
import ollama
import sys

# ======================================================================
# KONFIGURACE
# ======================================================================
MODELS = {
    "analytik": "qwen3.5:9b",        # Silný model pro analýzu
    "pisatel":  "granite4:tiny-h",    # Lehký model pro formátování
}
DEBUG = False  # True = zobrazí meziprodukt mezi fázemi


def call_model(model, messages, temperature=0.2, num_predict=500, num_ctx=2048,
               think=None):
    """
    Synchronní volání modelu. Vrací text odpovědi.

    Parametr think:
      - None  = nechá výchozí chování modelu (non-thinking modely ho ignorují)
      - False = explicitně vypne thinking (nutné pro qwen3.5 a podobné)

    DŮLEŽITÉ: think musí být top-level parametr funkce ollama.chat(),
    NE uvnitř options. Uvnitř options je tiše ignorován.
    Viz: https://github.com/ollama/ollama/issues/14793
    """
    kwargs = {
        "model": model,
        "messages": messages,
        "options": {
            "temperature": temperature,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "repeat_penalty": 1.1,
        },
    }
    if think is not None:
        kwargs["think"] = think

    response = ollama.chat(**kwargs)
    return response.message.content


def stream_model(model, messages, temperature=0.2, num_predict=1200, num_ctx=4096,
                 think=None):
    """Streamované volání modelu. Tiskne tokeny průběžně na terminál."""
    kwargs = {
        "model": model,
        "messages": messages,
        "options": {
            "temperature": temperature,
            "num_predict": num_predict,
            "num_ctx": num_ctx,
            "repeat_penalty": 1.1,
        },
        "stream": True,
    }
    if think is not None:
        kwargs["think"] = think

    stream = ollama.chat(**kwargs)
    full_output = []
    for chunk in stream:
        text = chunk.message.content
        print(text, end="", flush=True)
        full_output.append(text)
    return "".join(full_output)


def debug_print(label, content):
    """Vytiskne meziprodukt, pokud je DEBUG zapnutý."""
    if DEBUG:
        print(f"\n{'~'*60}")
        print(f"  DEBUG — {label}")
        print(f"{'~'*60}")
        print(content)
        print(f"{'~'*60}\n")


def run_brainstorming():
    print("\n" + "=" * 60)
    print(" 🤖 LOKÁLNÍ AI ASISTENT (2-fázový Multi-Model Prompt Chain)")
    print(f"    Fáze 1: {MODELS['analytik']}")
    print(f"    Fáze 2: {MODELS['pisatel']}")
    print("=" * 60)

    topic = input("\nZadejte téma k řešení: ")
    if not topic.strip():
        print("Téma nebylo zadáno. Ukončuji.")
        sys.exit(0)

    # ==================================================================
    # FÁZE 1: ANALYTIK (qwen3.5:9b)
    #
    # think=False vypíná reasoning mód přes API parametr.
    # Bez toho thinking spotřebuje celý num_predict budget
    # a message.content bude prázdný.
    # ==================================================================
    print("\n[1/2] 🔍 Analýza problému (qwen3.5)...")

    osnova = call_model(
        model=MODELS["analytik"],
        messages=[{
            "role": "user",
            "content": (
                f"Téma: '{topic}'\n\n"
                "Vypiš česky:\n"
                "A) Hlavní cíl uživatele (1 věta).\n"
                "B) 3 konkrétní kroky k řešení (označ B1, B2, B3).\n"
                "C) 1 kritické riziko (formuluj jako varování pro uživatele).\n\n"
                "Nic dalšího nepiš. Žádné úvody ani závěry."
            ),
        }],
        temperature=0.2,
        num_predict=400,
        num_ctx=2048,
        think=False,
    )

    debug_print("FÁZE 1 — surová osnova (qwen3.5)", osnova)

    if not osnova.strip():
        print("\n[CHYBA] Fáze 1 vrátila prázdný výstup.")
        print("  Možné příčiny:")
        print("  - think=False nefunguje (vyžaduje Ollama >= 0.9.0)")
        print("  - num_predict je příliš nízký")
        print("  - Model není dostupný (zkontrolujte: ollama list)")
        sys.exit(1)

    # ==================================================================
    # FÁZE 2: PISATEL + FORMÁTOR (granite4:tiny-h)
    #
    # granite4:tiny-h nemá thinking mód — think parametr není potřeba.
    # Instrukce jsou krátké s few-shot příkladem pro tučné písmo.
    # ==================================================================
    print("[2/2] ✍️  Generování textu (granite4:tiny-h)...\n")
    print("-" * 60 + "\n")

    system_prompt = (
        "Jsi český konzultant. Piš pouze česky. Vždy vykej.\n"
        "Rozepiš každý bod do uceleného odstavce.\n"
        "Nadpisy piš přirozeně bez písmen a čísel z osnovy "
        "(nepoužívej A), B1), C) apod.).\n"
        "Formátuj výstup takto:\n"
        "- ## pro hlavní nadpis\n"
        "- ### pro každou sekci\n"
        "- **tučně** klíčová slova\n"
        "  Příklad: 'Připravte si **strukturované odpovědi** na otázky.'\n"
        "- Na konec přidej ## 💡 TIP s jednou praktickou radou."
    )

    user_prompt = (
        f"Téma: {topic}\n\n"
        f"Osnova k rozepsání (zpracuj VŠECHNY body A, B1, B2, B3 i C):\n"
        f"{osnova}\n\n"
        "Rozepis každý bod do plného odstavce (minimálně 3 věty na bod). "
        "NESMÍŠ text zkracovat."
    )

    final_text = stream_model(
        model=MODELS["pisatel"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
        num_predict=1500,
        num_ctx=4096,
    )

    print("\n\n" + "=" * 60)
    print(" ✅ Proces dokončen.")


if __name__ == "__main__":
    try:
        run_brainstorming()
    except KeyboardInterrupt:
        print("\n\n[INFO] Skript přerušen uživatelem (Ctrl+C).")
        sys.exit(0)
```

### Krok 4.3: Uložení souboru

1. Stiskněte `Ctrl+O` (uložení).
2. Stiskněte `Enter` (potvrzení názvu souboru).
3. Stiskněte `Ctrl+X` (ukončení editoru).

---

## 5 — Vysvětlení technických parametrů

### Parametr `think=False` (kritické pro reasoning modely)

`qwen3.5:9b` má ve výchozím stavu zapnutý reasoning mód. Při generování odpovědi nejdřív „přemýšlí" v bloku `<think>...</think>`, který spotřebovává tokeny z budgetu `num_predict`. U krátkých výstupů (osnova ~5 řádků) thinking snadno spotřebuje **celý budget** a na skutečnou odpověď nezbude nic → `message.content` je prázdný řetězec.

```
┌────────────── num_predict: 400 tokenů ──────────────┐
│                                                      │
│  BEZ think=False:                                    │
│  <think>přemýšlení... 400 tokenů...</think>          │
│  [odpověď: PRÁZDNÁ]                                  │
│                                                      │
│  S think=False:                                      │
│  A) Hlavní cíl: ...                                  │
│  B1) Krok 1: ...                                     │
│  B2) Krok 2: ...     ← celý budget jde na odpověď   │
│  B3) Krok 3: ...                                     │
│  C) Riziko: ...                                      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

**Důležité:** `think` musí být **top-level parametr** funkce `ollama.chat()`, **ne** uvnitř slovníku `options`. Uvnitř `options` je tiše ignorován (potvrzeno v [GitHub issue #14793](https://github.com/ollama/ollama/issues/14793)).

```python
# ❌ NEFUNGUJE — think uvnitř options
ollama.chat(model="qwen3.5:9b", options={"think": False})

# ✅ FUNGUJE — think jako top-level parametr
ollama.chat(model="qwen3.5:9b", think=False, options={...})
```

### Parametry per-fáze

| Parametr | Fáze 1 (qwen3.5) | Fáze 2 (granite4:tiny-h) | Důvod rozdílu |
|---|---|---|---|
| `temperature` | $0.2$ | $0.4$ | Fáze 1: strohá fakta. Fáze 2: přirozený jazyk. |
| `num_predict` | $400$ | $1500$ | Fáze 1: krátká osnova (~5 řádků). Fáze 2: plný text (~300 slov). |
| `num_ctx` | $2048$ | $4096$ | Fáze 2 má na vstupu osnovu + systémový prompt — potřebuje větší okno. |
| `think` | `False` | — (nepotřeba) | qwen3.5 má reasoning mód. granite4:tiny-h ne. |

### Výchozí hodnoty Ollama (pro referenci)

Ověřeno ze zdrojového kódu ([`api/types.go`](https://github.com/ollama/ollama/blob/main/api/types.go)):

| Parametr | Výchozí v Ollama | Poznámka |
|---|---|---|
| `temperature` | $0.8$ | Skript ji ve všech fázích snižuje |
| `num_ctx` | $2048$ | Fáze 2 ji zvyšuje na $4096$ |
| `num_predict` | $-1$ (neomezeno) | Skript nastavuje explicitní strop |
| `repeat_penalty` | $1.1$ | Skript ponechává výchozí hodnotu |

---

## 6 — Přístup k odpovědi modelu: Jak to funguje v knihovně `ollama`

Od verze `ollama` **0.4+** odpověď modelu podporuje dva ekvivalentní způsoby přístupu:

```python
response: ChatResponse = ollama.chat(model='qwen3.5:9b', messages=[...])

# Oba způsoby jsou ekvivalentní:
print(response['message']['content'])     # dict přístup
print(response.message.content)           # atributový přístup
```

Odpověď je Pydantic model (`ChatResponse`), který podporuje jak `__getattr__`, tak `__getitem__`. Skript používá atributový přístup — je čitelnější.

---

## 7 — DEBUG mód: Kontrola meziproduktů

Skript obsahuje proměnnou `DEBUG` na začátku souboru:

```python
DEBUG = False  # Přepněte na True pro zobrazení meziproduktů
```

Když nastavíte `DEBUG = True`, skript po Fázi 1 vytiskne kompletní osnovu vygenerovanou modelem qwen3.5. To vám umožní:

- **Ověřit, že osnova obsahuje všech 5 prvků** (cíl, 3 kroky, riziko)
- **Zkontrolovat jazyk osnovy** — qwen3.5 by měl odpovídat česky (instrukce „Vypiš česky"), ale pokud přepne do angličtiny, uvidíte to
- **Identifikovat propagaci chyb** — pokud je osnova špatná, víte, že problém je v Fázi 1, ne v Fázi 2

Doporučený postup pro nové uživatele: Spusťte první běh s `DEBUG = True`.

---

## 8 — Prompt Engineering: Klíčové techniky použité ve skriptu

Tato sekce shrnuje konkrétní techniky, které byly empiricky ověřeny během vývoje skriptu.

### 8.1: Few-shot příklad pro tučné písmo

Holá instrukce *„použij tučné písmo pro klíčová slova"* byla v **4 po sobě jdoucích testech ignorována**. Teprve přidání konkrétního příkladu (few-shot) problém vyřešilo:

```python
# ❌ Nefunguje — holá instrukce
"- **tučně** klíčová slova"

# ✅ Funguje — instrukce + příklad
"- **tučně** klíčová slova\n"
"  Příklad: 'Připravte si **strukturované odpovědi** na otázky.'"
```

### 8.2: Explicitní výčet bodů k zpracování

Holá instrukce *„zpracuj všechny body"* vedla ke ztrátě 2/5 prvků. Explicitní výčet to opravil:

```python
# ❌ Nefunguje — příliš vágní
"Zpracuj všechny body z osnovy."

# ✅ Funguje — explicitní výčet
"Zpracuj VŠECHNY body A, B1, B2, B3 i C."
```

### 8.3: Minimální délka a zákaz krácení

Bez explicitního omezení model komprimoval odstavce na 1–2 věty:

```python
"Rozepis každý bod do plného odstavce (minimálně 3 věty na bod). "
"NESMÍŠ text zkracovat."
```

### 8.4: Zákaz přenosu struktury osnovy do nadpisů

Model mechanicky převzal označení `A)`, `B)`, `C)` z osnovy do nadpisů finálního textu:

```python
"Nadpisy piš přirozeně bez písmen a čísel z osnovy "
"(nepoužívej A), B1), C) apod.)."
```

### 8.5: Formulace rizika pro vykání

Osnova z Fáze 1 popisovala riziko ve 3. osobě (*„uchazeč podcení..."*), což v textu s vykáním vytvořilo stylistickou nekonzistenci. Oprava v promptu Fáze 1:

```python
"C) 1 kritické riziko (formuluj jako varování pro uživatele)."
```

---

## 9 — Každodenní rutina

### A) Aktivace prostředí + spuštění

```bash
source ~/ai-prostredi/bin/activate
python3 ~/brainstorm.py
```

### B) Opakované spouštění

Skript můžete spouštět opakovaně — každé spuštění je nezávislé. Virtuální prostředí stačí aktivovat jednou na začátku práce.

### C) Ukončení práce

```bash
deactivate
```

> Pokud aktivaci vynecháte, Python ohlásí chybu `ModuleNotFoundError: No module named 'ollama'`.

---

## 10 — Řešení problémů

| Symptom | Příčina | Řešení |
|---|---|---|
| `Failed to connect to Ollama` | Služba Ollama neběží | `sudo systemctl start ollama` nebo `ollama serve` v jiném terminálu |
| `model "qwen3.5:9b" not found` | Překlep nebo model není stažen | `ollama list` → `ollama pull qwen3.5:9b` |
| `model "granite4:tiny-h" not found` | Překlep nebo model není stažen | `ollama list` → `ollama pull granite4:tiny-h` |
| `ModuleNotFoundError: No module named 'ollama'` | Virtuální prostředí není aktivováno | `source ~/ai-prostredi/bin/activate` |
| `AttributeError` u `response.message.content` | Stará verze knihovny `ollama` (< 0.4) | `pip install ollama --upgrade` |
| **Fáze 1 vrátí prázdný výstup** | `think=False` nefunguje (stará Ollama) | Aktualizujte Ollama: `curl -fsSL https://ollama.com/install.sh \| sh` (vyžaduje >= 0.9.0) |
| **Fáze 1 vrátí prázdný výstup** | `think` je uvnitř `options` místo top-level | Zkontrolujte, že `think=False` je mimo dict `options` (viz sekce 5) |
| Text se usekne uprostřed věty | Nízký `num_predict` | Zvyšte `num_predict` v příslušné fázi |
| Model přešel na tykání nebo angličtinu | Model ztratil instrukce u složitého tématu | Zjednodušte téma. Zvyšte `num_ctx`. |
| Halucinace (neexistující slova / fakta) | Limit malého modelu | Zjednodušte zadání. |
| Nadpisy obsahují A), B), C) z osnovy | Model kopíruje strukturu osnovy | Ověřte, že systémový prompt Fáze 2 obsahuje instrukci o přirozených nadpisech |
| Pomalé přepínání mezi fázemi (~10–15s pauza) | Ollama vyměňuje modely v VRAM | Normální chování. Oba modely se nevejdou do GPU současně. |

---

## 11 — Přehled architektury

```
┌──────────────────────┐          surová osnova          ┌──────────────────────┐
│                      │          (5 bodů, ~80 slov)     │                      │
│   FÁZE 1: ANALYTIK   │ ─────────────────────────────►  │  FÁZE 2: PISATEL     │
│                      │                                 │                      │
│   Model: qwen3.5:9b  │                                 │  Model: granite4:    │
│   think=False        │                                 │         tiny-h       │
│   temp: 0.2          │                                 │  temp: 0.4           │
│   num_predict: 400   │                                 │  num_predict: 1500   │
│   num_ctx: 2048      │                                 │  num_ctx: 4096       │
│                      │                                 │  stream: True        │
└──────────────────────┘                                 └──────────┬───────────┘
                                                                    │
                                                              finální text
                                                              na obrazovku
```

---

## 12 — Výsledky empirického testování

Během vývoje byly otestovány 4 architektury se stejným zadáním (*„Jak se připravit na pracovní pohovor?"*):

| Architektura | Slov | Prvky (z 5) | Chyby/slovo | Tučné | Halucinace |
|---|---|---|---|---|---|
| 2-fázový, granite + granite | ~180 | 3/5 | 1:26 | ❌ | ✅ „ušištěte" |
| 4-fázový, granite × 4 (Běh 1) | ~95 | 3/5 | 1:24 | ❌ | ❌ |
| 4-fázový, granite × 4 (Běh 2) | ~95 | 3/5 | 1:32 | ❌ | ✅ „pohovkové" |
| **2-fázový, qwen3.5 + granite** | **~300** | **5/5** | **1:100** | **✅ 7×** | **❌** |

---

Tento dokument je výchozí bod pro vlastní empirické testování. Doporučuji začít s `DEBUG = True`, prozkoumat osnovu z Fáze 1 a parametry ladit podle potřeby. Všechny hodnoty závisí na konkrétní verzi Ollama, verzi modelů a vašem hardware.