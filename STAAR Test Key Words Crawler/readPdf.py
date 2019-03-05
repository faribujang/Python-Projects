import PyPDF2 as pdf

# creating an object 
file = open('SampleBook-English2-Reading.pdf', 'rb')

# creating a pdf reader object
fileReader = pdf.PdfFileReader(file)

# print the number of pages in pdf file
textData = []

for pages in fileReader.pages:
    theText = pages.extractText()

    textData.append(theText)

# print(textData)
    
fh = open("EngII2011.txt", "w")
fh.write(str(textData))
fh.close()

