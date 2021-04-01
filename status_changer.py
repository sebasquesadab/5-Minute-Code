import requests
import time

from time import sleep

yes = input('Please Enter Text lol: ')

token = ''

def split_str(string):
    split = string.split()
    return split

def status_changer(status):
    for i in range(0, 1):
        requests.patch(
            'https://discordapp.com/api/v8/users/@me/settings', headers={
                'Authorization': token,
                "user-agent": "Soy Is Sexy 6/9",
                "Content-Type": "application/json"}, json={
                    'custom_status': {'text': status}
            })

def main():
    for i in split_str(yes):
        status_changer(i)
        time.sleep(1)

while True:
    main()
