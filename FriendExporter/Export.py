import requests
import json
import io

with open('config.json') as r:
	config = json.load(r)

Token = config.get('DiscordToken')

headers = {
	'Authorization': Token,
	'User-Agent': 'Samsung/Fridge 6.9/9.6'
}

Output = []

def export_friends():
	friend_request_url = 'https://discord.com/api/v8/users/@me/relationships'
	friend_request = requests.get(url=friend_request_url, headers=headers)
	friend_big_data = friend_request.json()
	return friend_big_data

def export_to_json(uid, type, nickname, username, discriminator):
	friend_dict = {
		"User ID" : uid,
		"Type" : type,
		"Nickname" : nickname,
		"Username": username,
		"Discriminator": discriminator
		}
	json_object = json.dumps(friend_dict, indent = 4)
	with io.open('Exported/Exported.json', 'a', encoding='utf-8') as f:
		Output.append(friend_dict)
		return Output

def sort_friends():
	friend_data = export_friends()
	for count, friend in enumerate(friend_data):
		export_to_json(friend['id'], friend['type'], friend['nickname'], friend['user']['username'], friend['user']['discriminator'])
		print(f"{count} - Friend {friend['user']['username']}#{friend['user']['discriminator']} Exported To JSON File")
	with io.open('Exported/Exported.json', 'a', encoding='utf-8') as f:
		f.write(str(json.dumps(Output, indent=4)))

sort_friends()
