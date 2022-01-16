from gen import *
import pyperclip

review = Review(read_words_dict("words.csv"), grand(read_templates("templates.json")), ask_fields())
pyperclip.copy(review)
print(review)
