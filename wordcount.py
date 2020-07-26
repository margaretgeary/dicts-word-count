# put your code here.

def word_count(txt_file):

    lines = open(txt_file)

    word_counts = {}

    for line in lines:
        word = line.split()
    
        for item in word:
            if item in word_counts:
                word_counts[item] += 1
            else:
                word_counts[item] = word_counts.get(item, 0) + 1
    print(word_counts)
    return word_counts
"yaaay"
word_count("test.txt")