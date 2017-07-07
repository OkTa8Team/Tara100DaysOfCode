import sys
import random

"""awfulpoetry2_ans.py

    Displays 5 awful random poetries made up from the lists of articles, subjects, verbs and adverbs or without adbvers.

"""

__author__ = "maydee"


articles = ["the", "a", "her", "other", "another", "his", "its"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

amount = 5
if len(sys.argv) > 1:
    try:
        if 0 < int(sys.argv[1]) <= 10:
            amount = int(sys.argv[1])
        else:
            print("1 <= lines <= 10")
    except ValueError:
        print("usage: awfulpoetry2_ans.py [amount of lines]")

while amount:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    if random.randint(0, 1):
        print(article, subject, verb)
    else:
        print(article, subject, verb, adverb)
    amount -= 1