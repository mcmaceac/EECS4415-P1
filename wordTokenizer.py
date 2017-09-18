# Proper attribution to come!
# Revised by Parke Godfrey
# 2017-09-11

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = filter(None, re.split('\W+', line))
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word.lower(), 1))