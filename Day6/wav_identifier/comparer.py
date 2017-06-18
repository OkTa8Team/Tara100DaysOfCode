import hashlib

def hashCreator(filename):
	BLOCKSIZE = 65535
	hasher = hashlib.sha1()
	with open(filename, 'rb') as afile:
		buf = afile.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

def main():
	file1 = "20170316220551049_9033.wav"
	file2 = "20170317160746394_9033.wav"

	print("File1: {0}. File2: {1}. Comparison result: {2}".format(hashCreator(file1), hashCreator(file2), hashCreator(file1) == hashCreator(file2)))

main()