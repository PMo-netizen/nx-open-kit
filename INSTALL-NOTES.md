# Install notes

## What “install” means here
- **NXOpen** is not a pip package that talks to NX by itself. Journals run **inside** a licensed Siemens NX session (`Developer` > Play, or `run_journal.exe`).
- Vendor clones on disk are **reference source**, not Siemens-signed plugins.

## Agent computer (box)
- Full pack: `/workspace/nx-open-kit/` (~670MB mostly `ugopen-nxopen_lib`)
- Our journals: `/workspace/nx-open-kit/ours/examples/`
- Prefer STEP: `/workspace/process-simulate-cbr600/imports/cbr600rr-step-ok-ps-import-2026-09-26/`

## GitHub
- Curated public repo: https://github.com/PMo-netizen/nx-open-kit
- Contains our journals + index; heavy vendor trees stay on box/GT1 mirrors (or clone upstream yourself).

## GT1_Mega
- Target folder: `C:\Users\pmoaiserver\OneDrive\Projects\nx-open-kit`
- Pip-safe helper: `python -m pip install nxopentse` (helpers only; still needs NX to call NXOpen)
- DreamEnding `NX_MCP` / ugopen full tree: optional; skip full ugopen if disk is tight — use slim Sample tree or clone on demand.

## Work laptop (DI1HKHGK0034WNB) when on
- Deliverables: `C:\Users\mouland\OneDrive - Siemens AG\Siemens\Business Plan\FY26\AI BOTS\TC Demo Builder`
- Smoke: `01_hello_listing_window.py` then `02_import_step214.py` on crankshaft `-040.step`
