#!/usr/bin/env python3


def User(user_file):
	with open(user_file) as users:
		global id_gz
		id_gz = []
		for usr in users.readlines():
			try:
				int(usr.strip().split(',')[1])
			except:
				print("User file parameter error")
				exit()
			id_gz.append(usr.strip().split(','))





User('/home/shiyanlou/user.csv')
print(id_gz)
