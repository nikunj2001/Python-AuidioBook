import pyttsx3
import PyPDF2
book=open('DBMS-ASS4.pdf','rb')
speaker= pyttsx3.init()
pdf_reader=PyPDF2.PdfFileReader(book)
pages=pdf_reader.numPages
for num in range(0,pages):
    page=pdf_reader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()