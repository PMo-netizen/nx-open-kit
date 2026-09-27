# nx-open-kit (PMo-netizen)

Curated Siemens **NX Open** handoff for ChatGPT Assemble / TC Demo Builder / Process Simulate / GT1.

**Honesty:** teaching-twin / mesh-derived FreeCAD STEP (or STL → NX Convergent) — **not** OEM CAD, **not** Parasolid source, **not** a digital twin. Astra does **not** emit `.prt`; bridge is mesh or gated STEP → NX Open on a licensed NX install.

## What’s in this repo
- Assemble journals under `ours/examples/` (`01_hello_listing_window.py`, `02_import_step214.py`)
- `INDEX.md` — upstream vendor catalog (Foadsf tutorials, ugopen samples, NX_MCP, cookbooks, …)
- Vendor trees may live as git submodules or local mirrors on the agent box / GT1 — see `INSTALL-NOTES.md`

## Prefer STEP pack
On the agent computer: `/workspace/process-simulate-cbr600/imports/cbr600rr-step-ok-ps-import-2026-09-26/` (20 `solid_ok` of 23). First import target: crankshaft `HONDA_MOTORCYCLES-DEMO-CBR600RR-040.step`.

## Laptop / GT1
- Work laptop deliverables root: `C:\Users\mouland\OneDrive - Siemens AG\Siemens\Business Plan\FY26\AI BOTS\TC Demo Builder`
- GT1 Projects: `C:\Users\pmoaiserver\OneDrive\Projects\nx-open-kit` (synced from agent computer)

## Upstream highlights
| Repo | Why |
|------|-----|
| [Foadsf/NXOpen_Python_tutorials](https://github.com/Foadsf/NXOpen_Python_tutorials) | Python journal hello path |
| [ahmet6141/nxopen-python-cookbook](https://github.com/ahmet6141/nxopen-python-cookbook) | Headless `run_journal` recipes |
| [ugopen/nxopen_lib](https://github.com/ugopen/nxopen_lib) | Versioned UGOPEN samples |
| [DreamEnding/NX_MCP](https://github.com/DreamEnding/NX_MCP) | MCP bridge to NX (needs local NX) |
| [mingfeng6684/nxopen-mcp](https://github.com/mingfeng6684/nxopen-mcp) | NXOpen API RAG MCP |

Licenses remain with each upstream project.
