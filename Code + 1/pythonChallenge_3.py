"""pythonChallenge_3.py
	
	Parse to find the letters surrounded by 3 UPPERCASE letters from both sides.
"""


__author__ = "maydee"


import re


def findSurrounded(text):
	"""Returns the string with all surrounded by 3 uppercase letters from both sides."""
	
	return ''.join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", text))


if __name__ == "__main__":
	with open("inputParseChallenge_3.txt") as f:
		text = f.read() 
	print(findSurrounded(text))