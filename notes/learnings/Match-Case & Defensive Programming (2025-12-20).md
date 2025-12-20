## Session: Match-Case & Defensive Programming (2025-12-20)

### Co jsem se naučil

**1. Match-Case Syntaxe**
- Alternativa k `if-elif-else` ve verzi Python 3.10+
- `case _:` je wildcard (vše ostatní), musí být POSLEDNÍ
- Unreachable code = Code Review chyba (VS Code → Problems panel)

**2. Defensive Programming - Tři příklady:**
- Neznámý vstup → feedback uživateli, ne ignorování
- Smazání neexistujícího → kontrola `if x in list` před `remove()`
- Duplikáty → case-insensitive kontrola pomocí `.lower()`

**3. String Manipulation**
- `.lower()` — převede VŠECHNY velké znaky na malé (ne jen první)
- Konsistentní normalizace dat = méně bugů

**4. Logické myšlení (bez copy-paste)**
- Nejdříve logika ("co se má stát?")
- Pak syntax ("jak se to napíše?")
- VS Code Problems panel = tvůj sparing partner

### Blockers & Resolution
- Backticks pro kód — jsou přímo na klávesnici (vedle středníku) ✅
- Kate Snippets — skončilo to na tom, že nepotrebuješ, máš clipboard ✅

### Next Steps
- File I/O (JSON/TXT persistence)
- Pak GUI framework (později, ne teď)

### Lesson Quote
"Defensive Programming není o pesimismu. Je to o respektu k uživateli."
