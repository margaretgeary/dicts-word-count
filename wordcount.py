# put your code here.

import re

def word_count(txt_file):

    lines = open(txt_file)

    word_counts = {}

    for line in lines:
        word = line.split()
    
        for item in word:
            stripped = re.sub(r'\W+', '', item)
            if stripped in word_counts:
                word_counts[stripped] += 1
            else:
                word_counts[stripped] = word_counts.get(stripped, 0) + 1
    print(word_counts)
    return word_counts

word_count("test.txt")