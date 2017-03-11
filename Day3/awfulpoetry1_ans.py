import random

"""awfulpoetry1_ans.py

    Displays 5 awful random poetries made up from the lists of articles, subjects, verbs and adverbs or without adbvers.

"""

__author__ = "maydee"


articles = ["the", "a", "her", "other", "another", "his", "its"]
subjects = ["cat", "dog", "man", "woman"]
verbs = ["sang", "ran", "jumped"]
adverbs = ["loudly", "quietly", "well", "badly"]

for _ in range(5):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    if random.randint(0, 1):
        print(article, subject, verb)
    else:
        print(article, subject, verb, adverb)