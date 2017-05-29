import requests
import sys
import json
from time import sleep
import csv
import datetime


def write_json(data):
	with open('posts.json', 'w') as file:
		json.dump(data, file, indent = 2, ensure_ascii = False)

def to_json(post_dict):
	try:
		data = json.load(open('posts_data.json'))
	except:
		data = []
	data.append(post_dict)

	with open('posts_data.json', 'w') as file:
		json.dump(data, file, indent = 2, ensure_ascii = False)

def write_csv(data):
	with open('posts_data.csv', 'a') as file:
		writer = csv.writer(file)
		writer.writerow((data['likes'],
			data['reposts'],
			data['date'],
			data['id'],
			data['text']))


def get_data(post):
	try:
		post_id = post["id"]
	except:
		post_id = 0

	try:
		post_likes = post['likes']['count']
	except:
		post_likes = 0

	try:
		post_reposts = post['reposts']['count']
	except:
		post_reposts = 0

	try:
		post_text = post['text']
	except:
		post_text = '---'

	try:
		post_date = post['date']
	except:
		post_date = "---"

	data = {
		'id': post_id,
		'likes': post_likes,
		'reposts': post_reposts,
		'date': post_date,
		'text': post_text
	}

	return data

def main():
	start = datetime.datetime.now()

	#non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

	group_id = "-96445590"
	offset = 0
	all_posts = []
	date_x = 1434619787


	while True:
		sleep(1)
		r = requests.get('https://api.vk.com/method/wall.get', params={'owner_id': group_id, 'count': 100, 'offset': offset})
		posts = r.json()['response']

		all_posts.extend(posts)
		try:
			oldest_post_date = posts[-1]['date']
		except:
			break

		offset += 100
		print(offset)

		if oldest_post_date < date_x:
				break
		

	data_posts = []

	for post in all_posts:
		post_data = get_data(post)
		write_csv(post_data)

	end = datetime.datetime.now()
	total = end - start
	print(len(all_posts))
	print(str(total))

if __name__ == '__main__':
	main()
