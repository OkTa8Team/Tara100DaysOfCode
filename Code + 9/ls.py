import os
import argparse
import datetime
import locale

locale.setlocale(locale.LC_ALL, "")


__author__ = "MayDee"


def main():
	opts = parse_options()
	#print(opts)
	filenames = []
	dirnames = []
	if opts.recursive:
		#print("os.walk")
		for root, dirnames, files in os.walk(opts.dir):
			for filename in files:
				fullname = os.path.join(root, filename)
				filenames.append(fullname)
	else:
		#print("os.listdir")
		for name in os.listdir(opts.dir):
			fullname = os.path.join(opts.dir, name)
			if os.path.isfile(fullname):
				filenames.append(fullname)
			else:
				dirnames.append(fullname)
	process_lists(opts, filenames, dirnames)
	print("{0} file{1}, {2} director{3}".format("{0:n}".format(len(filenames)) if len(filenames) else "no",
		"s" if len(filenames) != 1 else "", "{0:n}".format(len(dirnames)) if len(dirnames) else "no",
		"ies" if len(dirnames) != 1 else "y"))



def parse_options():
	parser = argparse.ArgumentParser(description="The paths are optional: if not given . is used.", 
									usage="ls.py [options] [path1 [path2 [... pathN]]]")
	parser.add_argument("-H", "--hidden", action='store_true', dest="hidden", help="show hidden files [default: off]")
	parser.add_argument("-m", "--modified", action='store_true', dest="modified", help="show last modified date\\time [default: off]")
	parser.add_argument("-o ORDER", "--order=ORDER", default='name', dest="order", choices=['name', 'n', 'modified', 'm', 'size', 's'],
						help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]")
	parser.add_argument("-r", "--recursive", action='store_true', dest="recursive", help="recurse into subdirectories [default: off]")
	parser.add_argument("-s", "--sizes", action='store_true', dest="sizes", help="show sizes [default: off]")
	parser.add_argument("-d", "--directory", dest="dir", default='.',help="directory [default: .]")
	args = parser.parse_args()
	return args


def process_lists(opts, filenames, dirnames):
	key_data = []
	for file in filenames:
		modified = ""
		if opts.modified:
			try:
				modified = datetime.datetime.fromtimestamp(os.path.getmtime(file)).isoformat(" ")[:19] + " "
			except OSError:
				modified = "{0:>19} ".format("unknown")
		size = ""
		if opts.sizes:
			try:
				size = "{0:>15n}".format(os.path.getsize(file)) + " "
			except OSError:
				size = "{0:15}".format("unknown")
		if opts.order in {"m", "modified"}:
			order_key = modified
		elif opts.order in {"s", "sizes"}:
			order_key = size
		else:
			order_key = file
		key_data.append((order_key, "{modified}{size}{file}".format(**locals())))
	for key, name in sorted(key_data):
		print(name)

	key_data = []
	if not opts.hidden:
		dirnames[:] = [dir for dir in dirnames if not dir.split("\\")[-1].startswith(".")]
	modified = "" if not opts.modified else " " * 20
	size = "" if not opts.sizes else " " * 16
	for dir in sorted(dirnames):
		key_data.append((dir, modified + size + dir))

	for key, name in sorted(key_data):
		print(name)


if __name__ == '__main__':
	main()