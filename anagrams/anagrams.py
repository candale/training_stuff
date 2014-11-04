import codecs
import re


file_path = "luceafarul"
word_pattern = re.compile("\w+", re.UNICODE)
min_no_letters = 3
anagrams = {} # takes the form {anagram: {"no": int, "words": {"letter" : {"is_word": boolean, "sub_tree": {... }}}} 
			  # no    - the number of anagrams found
			  # words - the words from which the anagrams were obtained

def word_is_processed(sorted_word, word):
	if sorted_word not in anagrams:
		return False

	tree = anagrams[sorted_word]["words"]

	index = 0
	word_len = len(word)
	while index < word_len:
		letter = word[index]
		if letter not in tree:
			return False

		if index == word_len - 1:
			# if a previous word ended here
			if tree[letter]["is_word"]:
				return True
			else:
				return False

		tree = tree[letter]["sub_tree"]
		index += 1


def add_unprocessed_word(sorted_word, word):
	tree = anagrams[sorted_word]["words"]

	index = 0
	word_len = len(word)
	while index < word_len:
		letter = word[index]
		if letter not in tree:
			# if we reched the end of the word, is_word is true
			tree[letter] = {"is_word": index == word_len - 1, "sub_tree": {}} 

		tree = tree[letter]["sub_tree"]
		index += 1

def add_word(word):
	sorted_word = "".join(sorted(word))

	# if an anagram was alredy obtained from the current word
	if word_is_processed(word, sorted_word):
		return

	if sorted_word in anagrams:
		# if an anagram was not already obtained from the current word
		if not word_is_processed(sorted_word, word):
			add_unprocessed_word(sorted_word, word)
			anagrams[sorted_word]["no"] += 1
	else:
		# create node for current anagram and add the word it was obtained from
		anagrams[sorted_word] = {"no": 1, "words": {}}
		add_unprocessed_word(sorted_word, word)


with codecs.open(file_path, "r", encoding='utf8') as text_file:
	for line in text_file:
		for word in word_pattern.findall(line):
			if len(word) >= min_no_letters:
				add_word(word)

print sorted([(x, anagrams[x]["no"]) for x in anagrams if anagrams[x]["no"] >= 2], key=lambda x: x[1])