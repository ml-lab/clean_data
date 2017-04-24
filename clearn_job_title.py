import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import enchant 
import nltk
from nltk.corpus import words
import re
import html
import re
dict_en = enchant.Dict("en_US")


def remove_special_character(word):
	result = ''.join(e for e in word if e.isalnum() or e == ' ')
	result = re.sub('[!@#$%^&*()]', '', result)
	return result

def remove_after_character(word, special_character):
	below_charactor = word.find(special_character)
	if below_charactor != -1:
		return suggest_title[:below_charactor]
	return word

def add_suggest_word_to_dict(original_word, suggest_word):

	words_not_in_en = pd.read_csv("words_not_in_en.csv")
	words_not_in_en = words_not_in_en.drop('Unnamed: 0', 1)

	word = str.lower(original_word)
	new_words = words_not_in_en[words_not_in_en.word == word].head(1)


	frequency = 0 
	if len(new_words) != 0:
		frequency = words_not_in_en.get_value(new_words.index[0], 'frequency') + 1 

	words_not_in_en.set_value(new_words.index[0], 'frequency', frequency)
	words_not_in_en.set_value(new_words.index[0], 'score', 200)
	words_not_in_en.set_value(new_words.index[0], 'suggest_word', suggest_word)

	words_not_in_en.to_csv("words_not_in_en_2.csv")




def standard_job_title(original_job_title, suggest_words_dict):
	job_title_lower_case = str.lower(original_job_title)
	job_title_remove_unicode = html.unescape(job_title_lower_case)

	suggest_title = job_title_remove_unicode
	original_title = remove_special_character(job_title_remove_unicode)
	
	# Remove all word between "(" and ")"
	open_bracket = suggest_title.find("(")
	close_bracket = suggest_title.find(")") 
	if open_bracket != -1 and close_bracket != -1:
		suggest_title = suggest_title[:open_bracket] + suggest_title[(close_bracket + 1):]
	
	# Remove all word after "/", or "-"
	print("Suggeset title 1: ", suggest_title)
	suggest_title = remove_after_character(suggest_title, "/")
	print("Suggeset title 2: ", suggest_title)
	suggest_title = remove_after_character(suggest_title, "-")

	

	for word in original_title.split():
		wrong_words = suggest_words_dict[suggest_words_dict.word == word].head(1)
		if (len(wrong_words) == 1):

			suggest_word = wrong_words.get_value(wrong_words.index[0], 'suggest_word')
			wrong_word = wrong_words.get_value(wrong_words.index[0], 'word')
			score = wrong_words.get_value(wrong_words.index[0], 'score')


			if score >= 95:
				suggest_title = suggest_title.replace(wrong_word, suggest_word)
   

	score = fuzz.ratio(original_title,suggest_title)
	return (suggest_title, score)  



# words_not_in_en = pd.read_csv("words_not_in_en.csv")
# words_not_in_en = words_not_in_en.drop('Unnamed: 0', 1)

# print(standard_job_title("Sr. Product Marketing Manager", words_not_in_en))
	
   
