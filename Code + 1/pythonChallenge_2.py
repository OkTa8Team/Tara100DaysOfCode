"""pythonChallenge_2.py

	Parses the content of inputParseForLetters.txt in order to find rare characters.
"""


__author__ = "MayDee"


import re


def parseForLetters(text):
"""Parses the text and returns the rare characters."""

	return "".join(re.findall("[a-zA-Z]", text))

if __name__ == '__main__':
	with open("inputParseForLetters.txt") as f:
		text = f.read()
	print(parseForLetters(text))