"""Dubstep_codewars.py

	Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
	Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.
	For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
	Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
Input
	The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
Output
	Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.
"""

__author__ = "maydee"



def song_decoder(song):
	"""Return the words separated with a space not 'WUB'.
	"""
	remove = 'WUB'
	raw = song.split(remove)
	return ' '.join([i for i in raw if i != ''])


if __name__ == '__main__':
	text = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'	# WE ARE THE CHAMPIONS MY FRIEND
	print(song_decoder(text))
	text = 'AWUBBWUBC'						# WUB should be replaced by 1 space
	print(song_decoder(text))
	text = 'AWUBWUBWUBBWUBWUBWUBC'			# multiples WUB should be replaced by only 1 space
	print(song_decoder(text))
	text = 'WUBAWUBBWUBCWUB'				# heading or trailing spaces should be removed
	print(song_decoder(text))