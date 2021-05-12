import requests
import kahoot
import multiprocessing
import random
import string

from kahoot import client
from multiprocessing import current_process

bot = client()

def kahoot_join(pin, name):
	print(f'Started Job On Process {current_process().pid}')
	while True:
		name = name + ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
		bot.join(pin, name)

def main():
	procs = 24
	jobs = []
	pin = input("Enter Game Pin: ")
	for i in range(0, procs):
		output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
		process = multiprocessing.Process(target=kahoot_join, args=(pin, output_string))

		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()


if __name__ == '__main__':
	main()