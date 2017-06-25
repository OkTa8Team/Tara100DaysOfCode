import requests
import json




token=''


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
	# r = requests.get('https://api.vk.com/method/photos.get', params={'owner_id': ,
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
