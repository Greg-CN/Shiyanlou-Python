#!/usr/bin/env python3
filename = input("Please enter file path: ")
f = open(filename)
try:
	f.write('shiyanlou')
except:
	print("File write error")
finally:
	print("finally")
	f.close()
