import sys
import collections
import string

"""uniquewords_ans.py

    Count unique words in file.

"""

__author__ = "maydee"


def sort_by_frequency(pair):
    return pair[1]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word, count in sorted(words.items(), key=sort_by_frequency):
    print("'{0}' occurs {1} times".format(word, count))