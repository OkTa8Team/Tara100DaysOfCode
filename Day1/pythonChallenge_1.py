__author__ = "MayDee"

"""
	Shift 2 letter by alphabet and get instructions and next link.
"""

def decode(text):
	"""
		text - text to be shifted.

		Shifts text by alphabet in 2 letters right.
	"""
	dict_trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
	return text.translate(dict_trans)

if __name__ == '__main__':
	text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	print(text)
	print(decode(text))
	link = "http://www.pythonchallenge.com/pc/def/map.html"
	print(link)
	print(decode(link))
