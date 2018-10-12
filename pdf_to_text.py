import PyPDF2
import textract
import webbrowser
filename=raw_input("Enter the filename ")

PdfFileObj=open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(PdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
       text = text
else:
       text = textract.process(fileurl, method='tesseract', language='eng')
text_file = open("Output.txt", "w")
text_file.write("%s" % text)
text_file.close
webbrowser.open("Output.txt")
