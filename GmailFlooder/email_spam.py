import random
import string
import smtplib
import multiprocessing

from multiprocessing import current_process

def send_email(reciever, username, password):
	try:
		smtp_server.login(username, password)
	except:
		print('Error Logging In')
	while True:
		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
			try:
				content = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
				message = f"Subject: {content}\n\n{content}"
				smtp_server.sendmail(username, reciever, message)
			except:
				print("Error Sending Email")

def main():
	procs = 4 # You can edit this however you want
	jobs = []
	username = input('Your Gmail Address: ')
	password = input('Your Gmail Password: ')
	reciever = input('Reciever Address: ')
	for i in range(0, procs):
		process = multiprocessing.Process(target=send_email, args=(reciever, username, password))

		jobs.append(process)

	for j in jobs:
		j.start()

	for j in jobs:
		j.join()

if __name__ == '__main__':
	main()