# NX Open Python — import one STEP214 file into the work part (or new part).
# Edit STEP_PATH before run. Teaching-twin STEP only.
#
# Headless example (adjust UGII_ROOT_DIR to your NX install):
#   $env:UGII_ROOT_DIR = "C:\Program Files\Siemens\NX2412\NXBIN"
#   & "$env:UGII_ROOT_DIR\run_journal.exe" 02_import_step214.py

import NXOpen

# <<< set this on the laptop when testing >>>
# Prefer solid_ok pack (20 parts), not the full 23-on-disk freecad-gate step folder.
STEP_PATH = r"C:\Users\mouland\OneDrive - Siemens AG\Siemens\Business Plan\FY26\AI BOTS\TC Demo Builder\packs\cbr600rr-realmesh-2026-09-24\step\HONDA_MOTORCYCLES-DEMO-CBR600RR-040.step"
OUT_PRT = r"C:\Users\mouland\OneDrive - Siemens AG\Siemens\Business Plan\FY26\AI BOTS\TC Demo Builder\packs\cbr600rr-realmesh-2026-09-24\nx-out\CBR600RR-040-imported.prt"

def main():
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()
    lw.WriteLine("Importing STEP: " + STEP_PATH)

    importer = session.DexManager.CreateStep214Importer()
    importer.SimplifyGeometry = True
    importer.ObjectTypes.Solids = True
    importer.ObjectTypes.Surfaces = True
    importer.ObjectTypes.Curves = False
    importer.InputFile = STEP_PATH
    importer.OutputFile = OUT_PRT
    importer.FileOpenFlag = False
    # Prefer new part destination when supported by the journal version:
    try:
        importer.ImportTo = NXOpen.Step214Importer.ImportToOptionNewPart
    except Exception:
        pass

    result = importer.Commit()
    importer.Destroy()
    lw.WriteLine("Commit done. Result: " + str(result))
    lw.WriteLine("Saved/targeted PRT: " + OUT_PRT)
    lw.WriteLine("NOTE: Mesh-derived STEP = teaching twin, not OEM B-rep.")

if __name__ == "__main__":
    main()
