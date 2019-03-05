import PyPDF2 as pdf

import nltk
from nltk.corpus import stopwords

stopping_words = set(stopwords.words('english'))

stop_words = list(stopping_words)
stop_words_upper = [x.upper() for x in stop_words]

# creating an object 
file = open("C:\\Users\\Imam\\Documents\\Data Analytics Club\\SampleBook-English2-Reading.pdf", "rb")

# creating a pdf reader object
fileReader = pdf.PdfFileReader(file)

# print the number of pages in pdf file
textData = []

for pages in fileReader.pages:
    theText = pages.extractText()

    # for char in theText:
    # 	theText.replace(char, "\n")

    textData.append(theText)

final_list = [word for line in textData for word in line.split()]

# for i in set(textData):
#     # if i in stopwords.words('english'):
#     #     pass
#     final_list.append(i.strip('\n'))

# for i in textData:
# 	if i in stopping_words:
# 		textData.remove(i)
# 	final_list.append(i.strip('\n'))

# for i in final_list:
# 	if i in stop_words:
# 		final_list.remove(i)
	# final_list.append(i.strip('\n')

filtered_words = [word for word in final_list if word not in stop_words or stop_words_upper]

print(str(stop_words) + '\n')
print(str(stop_words_upper) + '\n')
print(final_list)


# filtered_word_list = final_list[:] #make a copy of the word_list

# for word in final_list: # iterate over word_list
# 	if word in stopwords.words('english'):
# 		final_list.remove(word) # remove word from filtered_word_list if it is a stopword

# filtered_words = [word for word in final_list if word not in stop_words]

# [s.strip('\n') for s in theText]
# [s.replace('\n', '') for s in theText]


# text_data = []

# for elem in textData:
#         text_data.extend(elem.strip().split('n'))  

# for line in textData:
#     textData.append(line.strip().split('\n'))
#--------------------------------------------------------------------

import os.path

save_path = "C:\\Users\\Imam\\Documents\\Data Analytics Club"

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file + ".txt")   

file1 = open(completeName, "w")

# file1.write(str(final_list))

for line in final_list:
    file1.write(line)

file1.close()

f = open(completeName, "r")

for line in f:
	line = line.strip("\n")
	line = line.strip("\t")

f.close()
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