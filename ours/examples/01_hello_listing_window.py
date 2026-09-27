# NX Open Python journal — Hello (run inside NX: File > Execute > NX Open, or run_journal.exe)
# Does nothing to geometry; proves NXOpen import + session.

import NXOpen

def main():
    session = NXOpen.Session.GetSession()
    lw = session.ListingWindow
    lw.Open()
    lw.WriteLine("NX Open smoke OK — ChatGPT Assemble / TC Demo Builder handoff")
    lw.WriteLine("Session: " + str(session))

if __name__ == "__main__":
    main()
