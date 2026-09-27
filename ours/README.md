# NX Open handoff (ChatGPT Assemble ↔ TC Demo Builder)

**Date:** 2026-09-27 (HKT)  
**Owner track:** ChatGPT Assemble; shared with TC Demo Builder  
**Honesty:** Teaching-twin / demo geometry only — not OEM CAD, not digital twin.

## What NX Open is
Siemens NX programming API (journals / automation). Runs **inside a licensed NX install** (GUI journal or headless `run_journal.exe`). Languages: Python, .NET, C++, Java. **Not** a cloud REST API. **Not** something Astra emits as `.prt` by itself.

## Does Astra go “direct” into NX CAD?
**No.** Practical bridge:
1. Astra / Assemble produce **HTML + mesh (STL/GLB)** and/or **STEP via FreeCAD/OCC gate** (approximate solids from mesh).
2. On the Siemens laptop, **NX Open Python** imports STEP (or builds parametric solids) → saves `.prt`.
3. Optional later: Astra generates NX Open journal text that NX executes — still tool-mediated, not a native Astra→PRT modality.

## Prefer STEP
- Slim OK pack (20 solid_ok): `/workspace/process-simulate-cbr600/imports/cbr600rr-step-ok-ps-import-2026-09-26/`
- First import: crankshaft `HONDA_MOTORCYCLES-DEMO-CBR600RR-040.step`

## Journals in this folder
- `examples/01_hello_listing_window.py`
- `examples/02_import_step214.py`

See repo root `INDEX.md` / `INSTALL-NOTES.md`.
