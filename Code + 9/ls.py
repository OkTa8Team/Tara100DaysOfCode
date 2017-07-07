import os
import argparse
import datetime


__author__ = "MayDee"


def main():
	opts = parse_options()
	print(opts.dir)



def parse_options():
	parser = argparse.ArgumentParser(description="The paths are optional: if not given . is used.", 
									usage="ls.py [options] [path1 [path2 [... pathN]]]")
	parser.add_argument("-H", "--hidden", action='store_false', dest="hidden", help="show hidden files [default: off]")
	parser.add_argument("-m", "--modified", action='store_false', dest="modified", help="show last modified date\\time [default: off]")
	parser.add_argument("-o ORDER", "--order=ORDER", default='name', dest="order", choices=['name', 'n', 'modified', 'm', 'size', 's'],
						help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
	parser.add_argument("-r", "--recursive", action='store_false', dest="recursive", help="recurse into subdirectories [default: off]")
	parser.add_argument("-s", "--sizes", action='store_false', dest="sizes", help="show sizes [default: off]")
	parser.add_argument("-d", "--directory", dest="dir", default='.',help="directory [default: .]")
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	main()