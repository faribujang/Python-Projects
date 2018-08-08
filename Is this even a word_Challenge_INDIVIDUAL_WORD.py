

import random
import urllib.request

page = urllib.request.urlopen("http://pastebin.com/raw/q5a2MUz6")
english_words = [page.read()]

page_2 = urllib.request.urlopen("http://pastebin.com/raw/yxGhQyvY")
non_english_words = [page_2.read()]

def isWord(character_string):
	print("Is %s an English word?" %(character_string))

	character_string = random.choice(english_words)

	if character_string in english_words:
		print("True")
	elif character_string in non_english_words:
		print("False")

combined_list = list(chain(*zip(english_words, non_english_words)))

print(combined_list)

# x = random.choice(combined_list)

# isWord("bang")


