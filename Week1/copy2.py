#!/usr/bin/env python3

import sys

def copy_file(yuan, mu):
	with open(yuan, 'r') as yuan_file:
		with open(mu, 'w') as mu_file:
			mu_file.write(yuan_file.read())

if __name__ == '__main__':
	if len(sys.argv) == 3:
		copy_file(sys.argv[1], sys.argv[2])
	else:
		print("Parameter Error")
		print(sys.argv[0], 'yuan mu')
		sys.exit(-1)
	sys.exit(0)
