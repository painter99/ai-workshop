# AXONEX — Brainstorming Analýza 2026-04-27

> Tento dokument zaznamenává výsledky filtrace 6 brainstorming bloků. Pro každou myšlenku je uvedeno rozhodnutí a zdůvodnění. Slouží jako trvalý záznam toho, CO a PROČ bylo přijato nebo odmítnuto.

---

## Filtrační kritéria

1. **Scope** — Odpovídá hobbyistickému desktopovému projektu (~100–300 řádků kódu)?
2. **KISS** — Nepřidává zbytečnou složitost nad Karpathy principles?
3. **Hardware** — Respektuje ThinkPad E14 Gen2 (NVIDIA MX450, ~1.4 GB VRAM)?
4. **Latence** — Kompatibilní s TTFT < 500 ms (pro interaktivní UX)?
5. **Duplikace** — Není to již pokryto existujícím stackem?

---

## Blok 1 — Docling + Ollama prototyp (Invoice Extractor)

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **Docling** (PDF → Markdown) | ✅ **PŘIJATO** jako v1.x modul A2.6 | IBM knihovna, zachovává tabulky, lokální; doplňuje A2.3 (obrázky) pro PDF vstup. Přidána jako FR-13 (P1 Should-have). |
| **Ollama jako backbone** | ✅ Již v tech_spec.md jako MVP backend | Žádná změna potřeba. |
| **Pydantic pro structured output** | ✅ Již v tech_spec.md (A2.1, A2.2) | Žádná změna potřeba. |
| **LangGraph** | ❌ **ODMÍTNUTO** | Těžká závislost, overkill pro lineární chain; `asyncio` + PydanticAI retry repair pokrývají use-case elegantněji bez dodatečné komplexity. Viz sekce Zamítnuté knihovny v tech_spec.md. |

---

## Blok 2 — Modulární orchestrátor (Library Stack)

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **LangGraph** | ❌ Viz Blok 1 | — |
| **oLLM / AirLLM** | ✅ **PODMÍNĚNĚ PŘIJATO** jako v1.x modul A1.2c | Layer-by-layer disk inference umožňuje spustit 70B+ modely na omezeném HW. Nepoužitelné pro interaktivní UX (latence minuty), ale hodnotné jako volitelný **Deep Analysis backend** pro scénáře 'několik spuštění za směnu'. Přidáno do tech_spec sekce 1.3 a A1.2c. |
| **ExLlamaV2** | ❌ **ODMÍTNUTO** | Vyžaduje VRAM > 4 GB; Pavel má ~1.4 GB dostupných. |
| **ChromaDB + FastEmbed** | ✅ **PŘIJATO** jako v1.x modul A2.7 | Lokální vektorová DB bez cloudu. Hodnotná pro RAG recept (document archiv). Přidána jako FR-20 (P2 Nice-to-have). |
| **Docling** | ✅ Viz Blok 1 | — |
| **CustomTkinter** | ❌ **ODMÍTNUTO** | AXONEX přijal Flet (Flutter) — GPU akcelerace, streaming text, drag-drop out of the box. Tkinter by byl downgrade. |
| **Flet** | ✅ Již v tech_spec.md | Žádná změna potřeba. |
| **SGLang / vLLM / TensorRT-LLM** | ❌ Viz Blok 3 | — |

---

## Blok 3 — Produkční a limitovaný HW stack

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **SGLang, TensorRT-LLM, OpenLLM** | ❌ **ODMÍTNUTO** | Server-side multi-user enginy; AXONEX je single-user desktop aplikace. PRD explicitně vylučuje multi-user serverový provoz. |
| **LocalAI** | ❌ **ODMÍTNUTO** | Přidává síťovou vrstvu navíc. Ollama/llama.cpp řeší to samé s nižší komplexitou. |
| **MLC LLM / WebLLM** | ❌ **ODMÍTNUTO** | AXONEX v1.0 je Linux-only. Mobilní/browser target je mimo scope v1.0. |
| **Unsloth** | ❌ **ODMÍTNUTO** | PRD section 3.3 Non-goals: "Trénovat nebo fine-tunovat modely." |
| **AirLLM** | ❌ Viz Blok 2 | — |
| **KoboldCPP** | ❌ **ODMÍTNUTO** | Alternativa k Ollama/llama.cpp bez jasné výhody; přidává závislost. Ollama pokrývá stejný use-case. |

---

## Blok 4 — oLLM v produkci (analýza nasazení)

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **oLLM jako volitelný Ultra-Precision modul** | ✅ **PŘEHODNOCENO — PODMÍNĚNĚ PŘIJATO** | Pavel upozornil na legitimní use case: offline batch zpracování s 70B+ modely pro maximální soukromí a přesnost (scénář 'několik spuštění za směnu'). oLLM přidáno jako volitelný Deep Analysis backend (A1.2c) — jasně odděleno od interaktivního UX. |
| **Princip: NVMe SSD jako kritická závislost** | ✅ **ZAZNAMENÁNO** jako HW requirement | Pro Deep Analysis mód s oLLM je NVMe SSD kritický — layer-by-layer disk loading přímo závisí na I/O rychlosti. |
| **Princip: latence > přesnost pro desktop UX** | ✅ **UPŘESNĚNO** jako dual-mode princip | Platí pro Interactive mód. Deep Analysis mód má opačnou prioritu: přesnost > latence. Obojí je validní v různých kontextech. |

---

## Blok 5 — Recepty jako YAML/JSON šablony + bezpečnostní prvky

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **Recepty jako YAML/JSON deklarativní soubory** | ⚠️ **ODLOŽENO** na v2.0+ | Recepty v1.0 jsou Python moduly (čitelné, laditelnné). YAML engine by přidal komplexitu bez benefitu pro ~3 recepty. Vhodné přidat jako FR-19 (export/sdílení receptů) v v2.0+. |
| **Sandboxing receptů v izolovaném procesu** | ❌ **ODMÍTNUTO** pro v1.0 | Přepalba pro hobbyistický projekt. Vše běží lokálně, jeden uživatel. Zero-crash policy přes ErrorOverlay je dostatečná. |
| **No-Network Mode indikátor** | ✅ **PŘIJATO** jako UX poznámka | Vizuální "OFFLINE" indikátor v UI je hodnotný pro privacy-conscious uživatele. Přidáno jako doporučení do UX sekce tech_spec.md (FR-9 rozšíření). |
| **Hardware Auto-detect** | ⚠️ **ODLOŽENO** na v1.x | Hodnotné, ale nad scope MVP. Vhodné po stabilizaci Krok A–D. |
| **Marketplace receptů** | ⚠️ **ODLOŽENO** na v2.0+ | Distribuovaný marketplace je PRD v2.0+ vision. |
| **Drag & Drop na ikonu receptu** | ✅ Již v PRD (FR-5, A3.3) | Žádná změna potřeba. |
| **Local Secret Management (keyring)** | ❌ **ODMÍTNUTO** | PRD Non-goal: žádné cloudové providery. Pokud by se přidaly, keyring je správná volba — ale pro v1.0 je bezpředmětné. |

---

## Blok 6 — Python algoritmy repo pro začátečníky

| Myšlenka | Rozhodnutí | Zdůvodnění |
|----------|-----------|------------|
| **Celý blok** | ❌ **MIMO SCOPE** | Blok se týká obecného Python vzdělávání (maths, searches, strings). Nerelevantní pro AXONEX projekt. |

---

## Souhrnná mapa změn provedených do dokumentů

| Dokument | Změna | Sekce |
|----------|-------|-------|
| `tech_spec.md` | Přidána sekce 2.3 Zamítnuté knihovny (11 položek s odůvodněním) | §2 Tech stack |
| `tech_spec.md` | Přidány moduly A2.6 (DoclingPDFParser) a A2.7 (RAGKnowledgeBase) jako v1.x | §3 Atomické moduly |
| `prd.md` | Přidáno FR-13 (PDF vstup přes Docling) do Should-have P1 | §6.2 |
| `prd.md` | Přidáno FR-20 (RAG znalostní archiv) do Nice-to-have P2 | §6.3 |
| `prd.md` | Přečíslováno Nice-to-have FR-13→17, FR-14→18, FR-15→19 (eliminace ID kolize) | §6.3 |

---

## Klíčové architektonické principy potvrzené brainstormem

1. **Latence > Přesnost** pro interaktivní desktop UX. Kvantizované modely (Ollama) jsou správná volba.
2. **asyncio + PydanticAI** stačí pro AXONEX chain logic. LangGraph je overkill.
3. **Hardware limit** 1.4 GB VRAM vylučuje ExLlamaV2, oLLM, a velké modely bez kvantizace.
4. **Docling** je jedinou novou hodnotnou přidanou závislostí (PDF vstup pro faktury).
5. **ChromaDB + FastEmbed** jsou odloženy na v1.x jako volitelný RAG modul.

---

*Datum analýzy: 2026-04-27*
*Autor analýzy: Pavel Mareš + AI agent (Agent Zero / Claude)*
