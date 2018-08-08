

import random
import urllib.request

page = urllib.request.urlopen("http://pastebin.com/raw/q5a2MUz6")

page_2 = urllib.request.urlopen("http://pastebin.com/raw/yxGhQyvY")

# def readLinesSite(site):

		# data = urllib.request.urlopen("site")

		# for lines in data.readlines():
			# print(lines)
#def englishWords():

data_Eng = urllib.request.urlopen("http://pastebin.com/raw/q5a2MUz6")

english_words_list = []

for lines in data_Eng.readlines():
	english_words_list.append(lines)

data_NonEng = urllib.request.urlopen("http://pastebin.com/raw/q5a2MUz6")

non_english_words_list = []

for lines in data_NonEng.readlines():
	non_english_words_list.append(lines)

# english_words = [page.read()]	--> READS THROUGH WHOLE PAGE AS ONE THING
# non_english_words = [page_2.read()] --> READS THROUGH WHOLE PAGE AS ONE THING

from itertools import chain
combined_list = list(chain(*zip(english_words_list, non_english_words_list)))

#combined_list_2 = [j for i in zip(english_words,non_english_words) for j in i]

def isWord():

	x = random.choice(combined_list)

	print("Is %s an English word?" %(x))

	if x in english_words_list:
		print("True")
	elif x in non_english_words_list:
		print("False")

isWord()
