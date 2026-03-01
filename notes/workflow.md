


Tady je tvůj kompletně přepracovaný dokument `workflow.md`. 

Odráží tvůj obrovský technologický a myšlenkový posun z "běžného používání AI chatbotů" na **pokročilé agentické programování**. Text je strukturovaný tak, aby jasně definoval tvé nové, vysoce profesionální návyky.

***

# Workflow a Metodika

Tento dokument definuje mé pracovní a studijní postupy. Od počátečního přístupu "člověk a chatbot" jsem přešel na komplexní **agentické vývojové prostředí**, kde AI nefunguje jako generátor, ale jako striktní Sokratovský mentor s přístupem do mého systému.

## 🛠️ Nástroje (Můj technologický stack)

- **Windsurf IDE** — Hlavní vývojové prostředí (nahradilo standardní VS Code). 
- **Cascade (Gemini 3 Flash/GPT-5.3-Codex)** — Integrovaný agent. Vystupuje jako můj seniorní mentor a architekt.
- **GitNexus (MCP)** — Nástroj pro grafovou sémantickou analýzu kódu. Dává AI hluboký kontext o struktuře projektu a závislostech.
- **GitHub MCP** — Propojení s vnějším světem, slouží nejen k ukládání dlouhodobé paměti o mě pro AI.
- **Udemy** (The Python Mega Course) — Stále primární zdroj pro video lekce a cvičení.

---

## 🧠 AI Learning Approach (The Windsurf Constitution)

Můj přístup k AI je definován v globálních pravidlech (`.windsurfrules`). Umělou inteligenci řídím, nenechávám ji, aby řídila mě.

**Klíčové principy a procesy:**

### 1. Metoda GAR (Goal-Attempts-Roadblocks)
Úkoly nezadávám vágně. Pokud se na něčem zaseknu, definuji:
- **Goal:** Čeho chci dosáhnout.
- **Attempts:** Co už jsem zkusil.
- **Roadblocks:** Kde přesně je chyba/zásek.

### 2. Sokratovský mentor a zákaz hotového kódu
AI nesmí vygenerovat finální kód, dokud to výslovně neschválím ("Ukaž mi kód"). Na chyby odpovídá kladením naváděcích otázek, pomáhá mi formulovat hypotézy (Root Cause) a vysvětluje mi "PROČ" pomocí metafor z mé praxe v průmyslové výrobě.

### 3. Pravidlo 80/20 (Plánování vs. Exekuce)
- **80 % času** trávím v Chat Mode (diskuse o architektuře, závislostech a logice).
- **20 % času** trávím v Write Mode (samotné zapsání kódu).
Nejdříve logika, až potom syntaxe.

### 4. Strategie Memento (Lokální kontext)
Každý projekt obsahuje soubor `docs/plan.md`. Než se napíše první řádek kódu, AI musí zapsat plán a já ho musím schválit ("Přečíst a podepsat"). Po každém milníku zapisujeme do plánu sekci **Lessons Learned**.

### 5. Exocortex / Second Brain (Globální kontext)
Moje dlouhodobé znalosti, chyby a dosažená úroveň se neukládají do nespolehlivé lokální cache, ale verzují se v mém soukromém GitHub repozitáři `pavel-brain`. Na začátku každého nového projektu si AI přes MCP stáhne tento soubor, aby věděla, co už umím a kde dělám chyby.

### 6. Architektonická opatrnost
Před každým zásahem do kódu využíváme nástroj `gitnexus.impact` (zjištění dosahu změn / blast radius), aby se předešlo nechtěnému rozbití jiných modulů. Udržujeme "hygienu vláken" (časté restarty konverzací pro čistý kontext).

---

**Proč tento přístup:**
Řeší největší problém běžných AI asistentů v prohlížeči — **roztříštěnost a ztrátu kontextu**. Místo neustálého kopírování úryvků kódu tam a zpět a zdlouhavého vysvětlování stavu projektu má nyní AI (díky GitNexusu a integraci v IDE) stejný přehled o architektuře jako já. Minimalizuje se "tření" mezi nápadem a samotným učením.

**Kontrast:**
- ❌ **Starý přístup (Webové chaty jako t3.chat):** Izolovaný kontext. Musím AI složitě a zdlouhavě popisovat, jak můj projekt vypadá, vkládat jí úryvky kódu a řešit neustálé vytrhávání ze soustředění (Context switching).
- ✅ **Nový přístup (Agentické IDE):** Bezproblémová integrace. AI vidí můj repozitář, zná mé schopnosti (přes `brain.md`), aktualizuje `plan.md` a my se můžeme okamžitě ponořit do řešení problému a učení novým konceptům, aniž bych musel vysvětlovat "kde zrovna jsme".

**Výsledek:** Plynulý a ničím nerušený přerod od izolovaného psaní skriptů k budování komplexních systémů s mentorem, který má neustálý a přesný přehled o celku.

---
*Updated: Březen 2026*