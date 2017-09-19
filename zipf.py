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
	words = filter(None, re.split('[^a-zA-Z0-9\']', line))		#separating on white space(had to include ' becuase it was filtering on contractions)
	words = map(lambda x:x.lower(), words)			#convering words to lowercase
	
	for word in words:
		if word not in stopWords:		#checking to see if the word is a stop word
			if word[-2:] == '\'s':		#required in order to filter multiples of words
				word = word[:-2]
			if word not in occurences:	#the word is not already in the dictionary
				occurences[word] = 1
			else:
				occurences[word] += 1	#the word is in the dictionary, increment count by 1

#sorting by value


#extracting the top ten entries in the dictionary
topTen = sorted(occurences, key=occurences.get, reverse=True)[:10]
xAxis = []
yAxis = []
for val in topTen:
	#print('%s\t%s' % (val, occurences[val]))
	xAxis.append(val)
	yAxis.append(occurences[val])

#print(xAxis)
#print(yAxis)

#setting up the graph of the top words
yPos = np.arange(len(xAxis))
plot.bar(yPos, yAxis, align='center', alpha=0.5)
plot.xticks(yPos, xAxis)
plot.ylabel('#occurences')
plot.title('top ten words')

plot.show()








































