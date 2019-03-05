import re
from collections import Counter

filename = "C:\\Users\\Imam\\Documents\\Data Analytics Club\\TESTING.txt"

counter_list = []

with open(filename) as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = list(Counter(cap_words).most_common(10))

# print(word_counts)

# for x in word_counts:
# 	print(str(x) + "\n")

# def printByLine(tuples):
#     print( '\n'.join(' '.join(map(str,t)) for t in tuples) )

# print(word_counts)

#-------------------------------------------------------------------------

import os.path

save_path = "C:\\Users\\Imam\\Documents\\Data Analytics Club"

# name_of_file = input("What is the name of the file: ")

# completeName = os.path.join(save_path, name_of_file + ".txt")

completeName = os.path.join(filename + " Word Counter" + ".txt")  

file1 = open(completeName, "w")

# file1.write(str(final_list))

file1.write("Top 10 Most Common Words:" + "\n" + "\n")

for x in word_counts:
	file1.write((str(x) + "\n"))

file1.close()

#-------------------------------------------------------------------------

# import os.path

# save_path = "C:\\Users\\Imam\\Documents\\Data Analytics Club"

# name_of_file = input("What is the name of the file: ")

# completeName = os.path.join(save_path, name_of_file + ".txt")   

# file1 = open(completeName, "w")

# # file1.write(str(final_list))

# for line in final_list:
#     file1.write(line)

# file1.close()


#-------------------------------------------------------------------------

#FIND OCCURENCES OF SINGLE WORD IN FILE

# fname = input("Enter file name: ")
# word=input("Enter word to be searched:")
# k = 0
 
# with open(fname, 'r') as f:
#     for line in f:
#         words = line.split()
#         for i in words:
#             if(i==word):
#                 k=k+1
# print("Occurrences of the word:")
# print(k)

#-------------------------------------------------------------------------