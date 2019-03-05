pdf = open("Samplebook-English2-Reading.pdf", "r").splitlines()

# print the number of pages in pdf file
# textData = list(pdf)

# for pages in fileReader.pages:
#     theText = pages.extractText()

#     textData.append(theText)

# print(textData)
    
fh = open("EngII2011.txt", "w")
fh.write(str(pdf))
fh.close()

file = open(“testfile.txt”,”w”) 