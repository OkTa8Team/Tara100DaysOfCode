import requests
import json


#https://oauth.vk.com/authorize?client_id=5990267&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=messages,photos,audio&response_type=token&v=5.52

token='2d74c68bffc954b3ac19c7ad4fd16a951fca64777cb9d20cc4c8ab0aa2073b69b2116866a4d66e5faea6e'


def write_json(data):
	with open('photos.json', 'w') as file:
		json.dump(data, file, indent = 2, ensure_ascii = False)

def get_largest(size_dict):
	if size_dict['width'] >= size_dict['height']:
		return size_dict['width']
	else:
		return size_dict['height']

def download_photo(url):
	r = requests.get(url, stream=True)
	filename = url.split('/')[-1]

	with open(filename, 'bw') as file:
		for chunk in r.iter_content(4096):
			file.write(chunk)


def main():
	# Load all the photos into photos.json
	# r = requests.get('https://api.vk.com/method/photos.get', params={'owner_id': 259475165,
	# 																		'album_id': 'saved',
	# 																		'photo_sizes': True,
	# 																		'access_token': token})
	# write_json(r.json())


	photos = json.load(open('photos.json'))['response']

	for photo in photos:
		sizes = photo['sizes']

		max_size_url = max(sizes, key=get_largest)['src']
		download_photo(max_size_url)

if __name__ == '__main__':
	main()