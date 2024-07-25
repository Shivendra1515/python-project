
import PyPDF2

pdfiles = ["python cheatsheet.pdf", "python_complete_Notes.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfiles = open(filename, 'rb')
    pdfreader = PyPDF2.PdfReader(pdfiles)
    merger.append(pdfreader)
    pdfiles.close()
    merger.write('merged.pdf')
