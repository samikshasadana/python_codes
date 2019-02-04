import PyPDF2
pdfFileObj=open('C:\\Users\\RISHABH\\Downloads\\DEC.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(1)
print(pageObj.extractText())
pdfFileObj.close()
