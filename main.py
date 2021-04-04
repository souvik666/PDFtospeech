import pyttsx3
import PyPDF2

book = open('re.pdf' 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pdfReader = pdfReader.numPages
print(pages)

souvik = pyttsx3.init()
for num in range(9, pages)

page = pdfReader.getPage(9)
text = page.extractTeaxt()


souvik.say(text)
souvik.runAndWait()