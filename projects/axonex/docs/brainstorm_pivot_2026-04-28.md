# AXONEX — Brainstorm Pivot 2026-04-28

> **Proč tento dokument existuje:** Během session 2026-04-28 vyšlo najevo, že původní vize AXONEX (nástroj pro Linux developery a AI nadšence) je odlišná od skutečného záměru autora. Tento dokument zaznamenává **produktový pivot** a novou vizi před tím, než dojde k přepisu PRD, Tech spec a dalších dokumentů.
>
> **Status:** Brainstorm working paper — nezahrnuje se do oficiální release dokumentace dokud neprojde review a nebude promítnut do PRD.

---

## 1. Proč pivot

Původní dokumentace (PRD, Tech spec) definovala AXONEX jako:
- Cílovka: Linux power-user, backend developer, CS student
- Komplexnost: multi-model chain, Pydantic validace, COSMIC Desktop integrace, standalone binary
- Charakter: plnohodnotná desktopová aplikace

**Reálný záměr autora je jiný:**
> „Chci vytvořit jednoduchý multi-model prompt chaining orchestrator — workflow aplikaci, která pomůže tak trochu komukoli s čímkoli, tedy s jednoduššími úkoly. Prostě chci něco, co bude potenciálně moci být součástí jakéhokoliv linuxového OS — malý utility / tool."

---

## 2. Nová produktová vize

### Elevator pitch (nový)
> **„Vezmi fotku účtenky, přetáhni ji sem, dostaneš přehledné položky — bez cloudu, bez registrace, bez toho aby ses musel učit programovat."**

### Co AXONEX NENÍ
- ❌ Obecný chatbot (neconcurence Jan/LM Studio/AnythingLLM)
- ❌ RAG systém pro správu dokumentů
- ❌ AI experiment platforma
- ❌ Developer tool pro programátory

### Co AXONEX JE
- ✅ **Task-specific utility** — otevřu, vyřeším jednu věc, zavřu
- ✅ **Pro každodenní linuxáře** — od asistentek po účetní
- ✅ **Human-in-the-loop** — člověk vždy vidí a může zkontrolovat výstup
- ✅ **Max 1–2 úrovně hierarchie** — žádné složité menu
- ✅ **Rychlé UI** — načte se dřív než Ollama/LLM backend

---

## 3. Nové cílové skupiny (personas)

| Jméno | Profil | Potřeba | Jak AXONEX pomáhá |
|-------|--------|---------|-------------------|
| **Jana** | Asistentka v kanceláři, Linux Mint uživatelka | Dostat text z naskenovaného dokumentu | „Přepis skenu" — fotka → text |
| **Petr** | Živnostník, používá Ubuntu | Zpracovat účtenku/fakturu | „Faktura" — fotka → strukturovaný přehled |
| **Klára** | Studentka, Fedora | Přepsat rukou psané poznámky | „Poznámky" — fotka → digitální text |
| **Martin** | Účetní, Debian | Souhrn dlouhého emailu | „Shrnutí" — text → bullet points |

**Žádná z těchto osob není programátorka.** Všechny potřebují: jednoduchost, rychlost, kontrolu nad výstupem.

---

## 4. UI hierarchie — max 1–2 úrovně

```
[AXONEX se otevře — hlavní kategorie]
┌─────────────────────────────────────┐
│  💼 Práce s dokumenty                 │
│  💻 Práce s kódem                     │
│  📊 Práce s daty                      │
│  ⚙️  Nastavení (volitelné)           │
└─────────────────────────────────────┘

Kliknu na „💼 Práce s dokumenty"
┌─────────────────────────────────────┐
│  🖼️ Přepis skenu do textu             │
│  📄 Shrnutí delšího textu             │
│  📝 Přeformulování emailu             │
│  ✍️  Přepsat rukou psané poznámky    │
└─────────────────────────────────────┘

Kliknu na „🖼️ Přepis skenu"
→ Okno: „Přetáhni obrázek sem nebo vyber soubor"
→ Model se spustí (indikátor: „AI pracuje...")
→ Výstup se zobrazí jako prostý text
→ [Kopírovat] [Upravit] [Spustit znovu]
```

**Princip:** Žádné další podnabídky. Max 2 kliknutí od otevření appky po konkrétní úkol.

---

## 5. Human-in-the-loop — pravidla

| Recept typ | HitL chování | Proč |
|-----------|-------------|------|
| **Jednoduchý** (přepis skenu, OCR) | 🔄 Auto — výstup se rovnou zobrazí | Jedna fáze, jasný výstup |
| **Složitější** (faktura → JSON, multi-model) | ⏸ Pauza — uživatel zkontroluje mezivýsledek | Více fází, větší riziko halucinace |
| **Pokročilý / vlastní** (uživatelův recept) | ⚙️ Nastavitelné (A) | Uživatel si vybere |

**Základní pravidlo:** Výchozí chování je bezpečné (pauza u složitějších), uživatel může přepnout na auto-trust u jednoduchých úkolů.

---

## 6. Rychlost UI — nezávislá na LLM

**Požadavek:** UI se musí načíst **okamžitě** — bez ohledu na to, jestli běží Ollama.

| Scénář | Očekávané chování |
|--------|------------------|
| Aplikace otevřena, Ollama běží | UI okamžitě, první token do 500 ms |
| Aplikace otevřena, Ollama offline | UI okamžitě, jasná hláška: „Spusť Ollamu a zkuste znovu" |
| LLM inference probíhá | Neblokující indikátor, UI zůstává responzivní |

**Implementační dopad:** UI musí být oddělené od backendové inference. Flet okno se otevře bez čekání na model.

---

## 7. Distribuce — nejjednodušší možná

| Varianta | Pro vývojáře | Pro uživatele | Doporučení |
|----------|-------------|--------------|-----------|
| **Flatpak** | Střední | Velmi jednoduché (jeden klik v obchodě) | ✅ První volba pro end-user |
| **AppImage** | Jednoduché | Jednoduché (stáhneš, spustíš) | ✅ Fallback pro univerzální Linux |
| **PIP (`pip install axonex`)** | Velmi jednoduché | Vyžaduje Python/venv znalosti | ❌ Ne pro cílovku |
| **Nuitka standalone** | Složité | Jednoduché | ⚠️ Možná později, ne pro MVP |
| **System package** (apt/dnf) | Velmi složité | Nejlepší UX | ❌ Vyžaduje maintainera v distribuci |

**Verdikt pro MVP:** Flatpak nebo AppImage. Nejjednodušší pro uživatele, akceptovatelné pro vývojáře.

---

## 8. Tech stack — co zůstává, co se mění

### ✅ Zůstává
| Komponent | Důvod |
|-----------|-------|
| **Flet (Flutter)** | GPU akcelerace, rychlé UI, multi-platform potenciál |
| **Ollama (MVP backend)** | Snadný setup, lokální inference |
| **Pydantic v2 (interně)** | Validace JSON výstupů pro recepty, uživatel to nevidí |
| **Python 3.10+** | asyncio, tomllib |

### 🔄 Upravuje se
| Komponent | Původně | Nově | Důvod |
|-----------|---------|------|-------|
| **Cílová platforma** | Pop!_OS + COSMIC Desktop | **Jakýkoliv Linux** | Utility pro všechny, ne jen jednu distribuci |
| **Distribuce** | Nuitka standalone ELF | **Flatpak / AppImage** | Jednodušší pro uživatele |
| **UI design** | COSMIC vzhled | **Neutrální, funkční** | Nesvázat s konkrétním DE |
| **Personas** | Developer, CS student | **Kancelářský pracovník, živnostník** | Reálná cílovka |
| **Recepty** | Python moduly | **UI konfigurovatelné + předpřipravené** | Ne-programátor nemůže psát Python |

### ❌ Odpadá
| Komponent | Důvod |
|-----------|-------|
| **COSMIC-specific design** (zaoblené rohy, accent barvy) | Příliš úzká vázanost na jeden DE |
| **Nuitka build jako primární** | Předčasné optimalizace, Flatpak stačí |
| **llama.cpp jako MVP** | Ollama je jednodušší pro non-technical uživatele |

---

## 9. Dopad na existující dokumenty

| Dokument | Dopad | Akce |
|----------|-------|------|
| `PRD` (prd.md) | Zásadní — všechny sekce | Přepsat personas, use cases, NFR, elevator pitch |
| `Tech spec` (tech_spec.md) | Střední — stack, moduly | Upravit backend priority, odstranit COSMIC specifika, přidat Flatpak |
| `README.md` | Střední — pitch, status | Přepsat elevator pitch, use cases, zdůraznit utility charakter |
| `AXONEX_INDEX.md` | Drobný — přidat nový brief | Přidat tento dokument do seznamu |
| `PLAN_LEHKY_START.md` | Střední — 4 kroky | Pravděpodobně zjednodušit nebo přepsat pro novou cílovku |
| `active_hypotheses.md` | Drobný — nové hypotézy | Přidat hypotézy: Flatpak UX, rychlost UI nezávislá na LLM |
| `brainstorm_analysis_2026-04-27.md` | Žádný — historický | Ponechat jako záznam původního směru |

---

## 10. Doporučený postup — od nejjednoduššího

### Krok 0: Ověřit novou vizi (teď)
- [ ] Autor přečte tento brief a potvrdí/popraví
- [ ] Po schválení: přepsat PRD, Tech spec, README

### Krok 1: PoC — jednoduchý recept (2–3 hodiny)
- Jeden use case: „Přepis skenu do textu"
- Jednoduché Flet okno: tlačítko „Vybrat obrázek", textové pole s výstupem
- Bez chainování — jeden model (Ollama vision)
- Bez Pydantic — prostý textový výstup

### Krok 2: Ověření s reálným uživatelem
- Ukázat PoC Janě / Petrovi z personas
- Zjistit: je to dost jednoduché? Chápou to hned?

### Krok 3: Přidat další recept
- „Shrnutí textu" — textový vstup, textový výstup
- Jednodušší než vision — ověřit core loop

### Krok 4: Recepty jako UI nastavení
- Uživatel napíše svůj prompt, vybere model, uloží jako „Můj recept"
- Základní recept editor (ne kód, ne YAML — prosté textové pole)

### Krok 5: Distribuce
- Flatpak manifest nebo AppImage build
- Test na čistém Linuxu bez Pythonu

---

## 11. Otevřené otázky k vyřešení

1. **Flatpak vs AppImage** — který je jednodušší pro Pavla na sestavení? Který pro uživatele?
2. **Recept editor** — jak moc custom může být uživatelův prompt? Může měnit system prompt nebo jen user prompt?
3. **HitL default** — je „pauza u složitějších" skutečně správný default, nebo to bude frustrující?
4. **Multi-model chain** — zůstává jako vnitřní technologie, ale uživatel to nevidí. Jak to komunikovat? („AI pracuje v několika krocích"?)
5. **Cena / monetizace** — zůstává hobby open-source, nebo by mohla existovat placená verze s extra recepty?

---

## 12. Rozdílová analýza v jedné tabulce

| Aspekt | Původní vize (dokumenty 24.–27. 4.) | Nová vize (tento brief) |
|--------|-------------------------------------|------------------------|
| **Cílovka** | Developer, CS student | Kancelářský pracovník, živnostník |
| **Charakter** | Desktopová aplikace | Malý utility / tool |
| **Komplexnost** | Multi-model chain, JSON validace, build | Jednoduchý recept, prostý výstup |
| **UI** | COSMIC nativní | Neutrální, rychlé, univerzální |
| **Platforma** | Pop!_OS / COSMIC | Jakýkoliv Linux |
| **Distribuce** | Nuitka standalone ELF | Flatpak / AppImage |
| **Recepty** | Python moduly | UI konfigurovatelné + předpřipravené |
| **HitL** | Automatická validace (Pydantic) | Uživatel kontroluje výstup |
| **LLM backend** | Ollama → llama.cpp | Ollama (MVP) |

---

*Session: 2026-04-28*
*Autor: Pavel Mareš + Agent Zero*
*Status: Draft — čeká na schválení autorem*
