#Written by: Matthew MacEachern
#Student #: 213960216
#York email: mcmaceac@my.yorku.ca


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
	words = filter(None, re.split('[\W+_]', line))		#separating on white space
	words = map(lambda x:x.lower(), words)			#convering words to lowercase
	
	for word in words:
		if word not in stopWords and len(word) != 1:		#checking to see if the word is a stop word or word of length 1
			if word not in occurences:	#the word is not already in the dictionary
				occurences[word] = 1
			else:
				occurences[word] += 1	#the word is in the dictionary, increment its count by 1


topTen = occurences.items()			#converting dictionary to list for easier sorting
topTen = sorted(topTen, key=lambda x: x[0])						#sorting by the key ascending first
topTen = sorted(topTen, key=lambda x: x[1], reverse=True)[:10]	#sorting by the value descending second
																#and extracting the top 10



#extracting the top ten entries in the dictionary
#topTen = sorted(occurences, key=occurences.get, reverse=True)[:10]
xAxis = []
yAxis = []
for val in topTen:
	#print('%s\t%s' % (val, occurences[val]))
	xAxis.append(val[0])
	yAxis.append(occurences[val[0]])

#print(xAxis)
#print(yAxis)

#setting up the graph of the top
yPos = np.arange(len(xAxis))
plot.bar(yPos, yAxis, align='center', alpha=0.5)
plot.xticks(yPos, xAxis)
plot.ylabel('#occurences')
plot.title('top ten words')

plot.show()








































