import numpy as np 
import matplotlib.pyplot as plot 
import sys
import re

occurences = {}

for line in sys.stdin:
	line = line.strip()
	words = filter(None, re.split('\W+', line))
	for word in words:

		if word not in occurences:
			occurences[word] = 1
		else:
			occurences[word] += 1

print('%s' % str(occurences))
