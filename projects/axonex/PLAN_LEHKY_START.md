# AXONEX — Průvodce pokračujícího vývojáře

> **Filozofie tohoto dokumentu:**
> Už máš za sebou solidní práci — prompt chaining, multi-model experimenty, empirické testování. Nejsi na začátku. Tento plán staví přímo na tom, co umíš, a posouvá to o krok dál. Každý krok je volitelný. Když tě přestane bavit, prostě přestaneš. Dokumenty v `docs/` zůstávají jako reference — možná se k nim vrátíš, možná ne.
>
> **Pravidlo číslo jedna:** Tohle je tvůj projekt. Děláš ho pro radost.

---

## 🏗️ Co už máš (a proč je to dobrý základ)

Tvůj [Ollama Prompt Chaining manuál](https://github.com/painter99/ai-workshop/blob/main/practical_tools/ollama_prompt_chaining_manual.md) ukazuje, že už ovládáš:

| Co umíš | Jak to využijeme v AXONEX |
|---|---|
| **Multi-model chain** (2 fáze, 2 modely) | Základní architektura už funguje — jen ji rozšíříme |
| **Streaming** (`stream=True`) | AXONEX bude zobrazovat odpovědi průběžně |
| **`think=False` a API parametry** | Přesná kontrola nad chováním modelů |
| **Few-shot prompting** | Lepší formátování výstupu |
| **Empirické testování** | Ladění podle výsledků, ne podle teorie |
| **Virtuální prostředí, venv, systemctl** | Vývojové prostředí je připravené |

**To znamená:** Nezačínáš od nuly. Začínáš s funkčním `brainstorm.py` a přidáváš vrstvy.

---

## 🗺️ Nová mapa — 4 kroky (každý volitelný)

```
Krok A: Přidat strukturu (JSON)  →  "Model vrací data, ne jen text!"
    ↓
Krok B: Přidat obrázek           →  "Model vidí fotku a vrací JSON!"
    ↓
Krok C: Spojit A+B               →  "Faktura jako JSON, hotovo!"
    ↓
Krok D: Jednoduché okénko        →  "Mám vlastní program s tlačítkem!"
    ↓
...a pak se uvidí, co dál.
```

Každý krok trvá **1–3 hodiny** a dává ti něco funkčního. Nemusíš dělat všechny. Můžeš skončit po Kroku A a být spokojený.

---

## 📋 Krok A: Přidat strukturu — Pydantic schéma (1–2 hodiny)

**Východisko:** Tvůj `brainstorm.py` vrací text. Fáze 1 vrací osnovu jako text, Fáze 2 ji rozepisuje.

**Cíl:** Model vrací **JSON**, který Python automaticky validuje. Místo toho, abys parsoval text, dostaneš hotový slovník.

### Co budeš mít:
```python
# Místo toho, aby model vrátil:
"A) Cíl: připravit se na pohovor\nB1) Prostuduj firmu..."

# Model vrátí:
{
  "cil": "Připravit se na pracovní pohovor",
  "kroky": [
    {"nazev": "Prostuduj firmu", "popis": "..."},
    {"nazev": "Připrav odpovědi", "popis": "..."}
  ],
  "riziko": "Podcenit přípravu na technické otázky"
}
```

### Proč to stojí za to:
- **Validace:** Když model zapomene pole, Pydantic ti to řekne okamžitě.
- **Programovatelná logika:** Můžeš kontrolovat, jestli jsou všechny kroky vyplněné, počítat je, filtrovat je.
- **Základ pro AXONEX:** Cílem AXONEXu je strukturovaný výstup. Tohle je jádro.

### Mini-cíle:
- [ ] Nainstalovat `pydantic`: `pip install pydantic`
- [ ] Vytvořit schéma `AnalysisSchema` s poli `cil`, `kroky`, `riziko`
- [ ] Upravit prompt Fáze 1: "Vrať výsledek jako JSON v tomto formátu..."
- [ ] Parsovat odpověď přes `AnalysisSchema.model_validate_json()`
- [ ] Když model vrátí špatný JSON, zobrazit chybu místo crashnutí

**Když to funguje:** Máš první AXONEX-like funkci — model vrací data, ne text.

---

## 🖼️ Krok B: Přidat obrázek — multimodalita (2–3 hodiny)

**Východisko:** Už umíš posílat text. Nyní přidáš obrázek.

**Cíl:** Vzít JPG/PNG, zakódovat ho do Base64, poslat modelu s dotazem "Co je na obrázku?"

### Co budeš mít:
Skript `03_vision_llm.py`, který vezme účtenku/fakturu/fotku a model vrátí popis.

### Proč to stojí za to:
- **Wow efekt:** Najednou tvůj program "vidí".
- **Základ pro fakturu:** V Kroku C spojíš "vidění" (Krok B) se " strukturou" (Krok A).
- **Užitečné i mimo AXONEX:** Můžeš digitalizovat účtenky, popisovat fotky, číst text z obrázků.

### Mini-cíle:
- [ ] Načíst obrázek z disku (`PIL.Image` nebo čistý Python)
- [ ] Zakódovat do Base64 (to je jen textová reprezentace obrázku)
- [ ] Poslat modelu s dotazem přes Ollama API (`ollama.chat` s `images=[...]`)
- [ ] Dostat zpět popis v češtině

**Když to funguje:** Máš druhý stavební kámen AXONEXu — multimodální vstup.

---

## 🔗 Krok C: Spojit A+B — Faktura jako JSON (2–3 hodiny)

**Východisko:** Máš JSON strukturu (Krok A) a vidící model (Krok B).

**Cíl:** Vzít fotku faktury/účtenky, model " přečte" položky a vrátí je jako JSON.

### Co budeš mít:
```json
{
  "dodavatel": "Albert",
  "datum": "2026-04-25",
  "celkem": 245.50,
  "polozky": [
    {"nazev": "Mléko", "cena": 32.90},
    {"nazev": "Chleba", "cena": 28.00}
  ]
}
```

### Proč to stojí za to:
- **Tohle je AXONEX:** Spojení vision + struktury + chainování.
- **Okamžitě užitečné:** Můžeš si digitalizovat účtenky a sumarizovat výdaje.
- **Základ pro další recepty:** Faktura funguje? Zkus kód z obrázku, dokument z PDF, cokoli.

### Mini-cíle:
- [ ] Vytvořit schéma `InvoiceSchema` (dodavatel, datum, položky, celkem)
- [ ] Upravit vision prompt: "Přečti účtenku a vrať JSON v tomto formátu..."
- [ ] Zkusit 3–5 různých účtenek, ověřit přesnost
- [ ] Když model chybuje, ladit prompt (zkušenost z manuálu)

**Když to funguje:** Máš funkční AXONEX jádro. Všechno ostatní je jen obálka.

---

## 🪟 Krok D: Jednoduché okénko — Flet (volitelné, 2–4 hodiny)

**Východisko:** Máš funkční skripty v terminálu.

**Cíl:** Jednoduché okno: input pole, tlačítko "Zpracovat", textarea pro výstup.

### Co budeš mít:
`axonex_gui.py` — 40–60 řádků, jedno okno, žádné menu, žádné komplikace.

### Proč to stojí za to:
- **Můžeš to ukázat někomu jinému** — terminál je neatraktivní.
- **Cvičení Fletu** — když ho budeš chtít použít později, už ho trochu znáš.
- **Když nebudeš chtít, přeskoč** — terminál je naprosto v pořádku.

### Mini-cíle:
- [ ] `pip install flet`
- [ ] Okno s textovým polem, tlačítkem a výstupem
- [ ] Při kliknutí se spustí tvůj chain
- [ ] Výsledek se zobrazí v okně (může být raw JSON)

**Když to funguje:** Máš program, který vypadá jako program, ne jako skript.

---

## ⏱️ Realistické časové rozložení

Při 5 hodinách týdně:

| Krok | Odhad | Kdy bys mohl být hotový |
|------|-------|------------------------|
| Krok A (JSON struktura) | 1–2 hod | Za 1–2 týdny |
| Krok B (Obrázek) | 2–3 hod | Za 2–4 týdny |
| Krok C (Faktura) | 2–3 hod | Za 3–6 týdnů |
| Krok D (Okénko) | 2–4 hod | Za 4–8 týdnů |

**To znamená:** Za 1–2 měsíce máš funkční program, který čte účtenky a vrací data. Na 5 hodin týdně **výborné tempo**.

---

## 🆘 Když se zasekneš

**Pravidlo:** Zaseknout se je normální. Stává se to všem.

**Co dělat:**
1. **Dej si pauzu** — hodina, den, týden. Neutíkej před problémem, ale nech ho uležet.
2. **Zjednoduš** — když něco nefunguje, zkus to udělat ještě jednodušší. Odstraň polovinu kódu.
3. **Napiš mi** — pošli, co jsi napsal a co to vypisuje. Máme stejný setup (Pop!_OS, Ollama, Python).
4. **Přeskoč** — můžeš přejít na další krok a vrátit se později. Krok B nefunguje? Zkus C s textovým vstupem místo obrázku.

---

## 📝 Poznámka k původním dokumentům

Tvé původní dokumenty (PRD, Tech spec, Hypothesis Registry) zůstávají v `docs/`. Nejsou to povinná četba — jsou to **reference**. Můžeš je otevřít, když budeš chtít pochopit, proč jsi něco navrhoval určitým způsobem. Ale pro tento plán je nepotřebuješ.

**Jedna věc je užitečná z Hypothesis Registry:** Zvyk hlásit si své předpoklady. Když si myslíš "tohle by mělo fungovat", zapiš si to. Až to otestuješ, máš důkaz — ať už jsi měl pravdu, nebo ne.

---

## 🎯 Jak začít právě teď

Nejrychlejší cesta k prvnímu úspěchu:

1. Otevři terminál
2. `source ~/ai-prostredi/bin/activate`
3. `pip install pydantic`
4. Vezmi svůj `brainstorm.py`
5. Vytvoř nad ním schéma — jedno pole, jedna validace

To je celé. Za 30 minut máš první Pydantic validaci. Za hodinu máš strukturovaný výstup.

---

*AXONEX Průvodce pokračujícího vývojáře v1.0 — Stavíme na tom, co už umíš · 25. 04. 2026*
