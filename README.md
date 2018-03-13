# Readme for wordcount
- wordcount.py
- test_wordcount.py

## Module doc
	Total numbeCounts lines, words, characters and e-mail addresses

	Uses three 'Counter' objects to:
	1. Find the most common words in a given text file (a Counter type object)
	2. Find all email addresses in that file (re module for regular expressions)
	3. Count all the lines, words, characters and e-mails
	
	Argument:
	file        the name of the file to be parsed
	
	Options:
	-w          print the word count
	-mc         print the most common words - 5 by default
	-A          print all the words - with counter
	-E          print all the e-mails
