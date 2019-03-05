import PyPDF2 as pdf
from nltk.corpus import stopwords

filename = "E:\\DATA ANALYTICS CLUB\\ReadPDFtoTXT2.py"

# creating an object 
file = open(filename, "rb")

# creating a pdf reader object
fileReader = pdf.PdfFileReader(file)

# print the number of pages in pdf file
textData = []

for pages in fileReader.pages:
    theText = pages.extractText()

    # for char in theText:
    # 	theText.replace(char, "\n")

    textData.append(theText)

final_list = []

for i in textData:
	final_list.append(i.strip('\n'))

for word in final_list: # iterate over word_list
  if word in stopwords.words('english'): 
    final_list.remove(word)

# ...  
# filtered_words = list(filter(lambda word: word not in stopwords.words('english'), final_list))

# filtered_words = []

# filtered_words.append(word for word in final_list if word not in stopwords.words('english'))

# filtered_words = [word for word in final_list if word not in stopwords.words('english')]

# filtered_word_list = final_list[:] #make a copy of the word_list
# for word in final_list: # iterate over word_list
#   if word in stopwords.words('english'): 
#     filtered_word_list.remove(word)

# [s.strip('\n') for s in theText]
# [s.replace('\n', '') for s in theText]


# text_data = []

# for elem in textData:
#         text_data.extend(elem.strip().split('n'))  

# for line in textData:
#     textData.append(line.strip().split('\n'))
#--------------------------------------------------------------------

import os.path

save_path = "E:\\DATA ANALYTICS CLUB"

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file + ".txt")   

file1 = open(completeName, "w")

# file1.write(str(final_list))

for line in final_list:
    file1.write(line)

file1.close()

# ------------------------------------------------

# f = open(completeName, "r")

# for line in f:
# 	line = line.strip("\n")
# 	line = line.strip("\t")

# f.close()
#--------------------------------------------------------------------



# print(textData)



#--------------------------------------------------------------------

# fh = open("EngII2011.txt", "w")
# fh.write(str(textData))
# fh.close()

# with open(file1, "w") as f:
# 	content = f.write(str(textData))
# 	lines = f.readlines()
# 	lines = [line.rstrip('\n') for line in open(file1)]

# with open(completeName, "w") as file2:

# 	file2.write(name_of_file)

# 	content = file2.write(str(textData))
# 	lines = file2.readlines()
# 	lines = [line.rstrip('\n') for line in open(file2)]

# 	# for x in lst:
# 	# 	file2.write(str(x) + "\n")

# file2 = open(completeName, "w")

# file2.write(str(textData))

# file2.close()

# lines = [line.rstrip('\n') for line in open(file2)]

# lines = open(filename).read().splitlines()

# def splitlines_read():
# 	with open(file1, "r") as file3:
# 		lines = file3.read().splitlines()
# 	return lines

# 	file3.close()

# splitlines_read()

# file3 = open(file1, "r")

# file3.read().splitlines()

# file3.close()

# file2 = open(, "w")

# file2.write("DOES THIS WORK")

# file2.close()