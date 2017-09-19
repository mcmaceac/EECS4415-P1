import numpy as np 
import matplotlib.pyplot as plot 
import sys
import re

occurences = {}
stopWords = []

with open('stopwords-MySQL.txt', 'r') as f:		#open the file and read the contents line
	stopWords = [line.strip() for line in f]	#by line, adding each stripped stop word to the list


for line in sys.stdin:
	line = line.strip()
	words = filter(None, re.split('\W+', line))
	for word in words:

		if word not in stopWords:		#checking to see if the word is a stop word
			if word not in occurences:	#the word is not already in the dictionary
				occurences[word] = 1
			else:
				occurences[word] += 1	#the word is in the dictionary, increment count by 1

print('%s' % str(occurences))
