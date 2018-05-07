import random	#importing required modules and func
from urllib import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"	#var with url declared
WORDS = []	#var of empty list

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}	#dict of PHRASES with key and value declared

#do they want to drill phrases first
PHRASE_FIRST = False	#declaring a var as a bool
if len(sys.argv) == 2 and sys.argv[1] == "english":		#checking if user inputs are totally 2 and 1st input is "english" or not
	PHRASE_FIRST = True		#assigning True to PHRASE_FIRST if cond passes

# load up the words from the website
for word in urlopen(WORD_URL).readlines():		#opening a url and reading its lines and looping every line
	WORDS.append(word.strip())	#appening everyline with whitespaces/tabspaces/newlines....(strip()) removed to a empty var WORDS[]

def convert(snippet, phrase):	#defining a func with two args snippet and phrase
	class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]	#listing the words with its beginning letter capitalized, for the no. of sample words from var "WORDS" having its count of "%%%" from 'snippet'
	other_names = random.sample(WORDS, snippet.count("***"))	#taking sample of words from "WORDS" with its count of "***" in snippet
	results = []	#creating empty vars
	param_names = []

	for i in range(0, snippet.count("@@@")):	#looping for the range of no. of counts of "@@@" in snippet	
		param_count = random.randint(1,3)		#randomly assigning an int btwn 1 and 3 to param_count
		param_names.append(', '.join(random.sample(WORDS,param_count)))	#appending the words from "WORDS and count" separated by , 

	for sentence in snippet,phrase:		
		result = sentence[:]	#copying the entire list of sentence and storing in a var

		#fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)	#for every word in class_names, replacing the 1st occurence of "%%%" as 'word'

		#fake other names
		for word in other_names:
			result = result.replace("***", word, 1)	#for every word in other_names, replacing the 1st occurence of "***" as 'word'

		#fake parameter lists
		for wod in param_names:
			result = result.replace("@@@", word, 1)	#for every word in param_names, replacing the 1st occurence of "@@@" as 'word'

		results.append(result)	#all the above results are appened and returing it

	return results 

#keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()	#storing the list of keys of 'PHRASES' in 'snippets'
		random.shuffle(snippets)	#shuffling the elements in list of snippets

		for snippet in snippets:
			phrase = PHRASE_FIRST[snippet]	#assigning the value of snippet from dict 'PHRASE_FIRST' to var 'phrase'
			question, answer = convert(snippet, phrase)	#two var declared to the func convert 
			if PHRASE_FIRST:
				question, answer = answer, question	#ques is ans and ans is ques if 'PHRASE_FIRST' exists

			print question	

			raw_input("> ")		#getting input for the ans
			print "ANSWER %s \n\n" %answer
except EOFerror:	#catching End of file error
	print "\nBye"
