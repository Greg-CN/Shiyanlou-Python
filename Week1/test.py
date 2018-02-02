#!/usr/bin/env python3
#gong zi = gz
#gong hao = id
#ying na shui = yns
#shui qian = sq
#shui hou = sh
import sys
def jisuan(gz, bili=0.165):
	sq = gz - gz * bili
	if sq <= 3500:
		print(id, end=':')
		print(format(sq,".2f"))
	else:
		yns = sq - 3500
		if yns <= 1500:
			print(id, end=':')
			print(format(sq - (yns * 0.03 - 0),".2f"))
		elif yns <= 4500:
			print(id, end=':')
			print(format(sq - (yns * 0.1 - 105),".2f"))
		elif yns <= 9000:
			print(id, end=':')
			print(format(sq - (yns * 0.2 - 555),".2f"))
		elif yns <= 35000:
			print(id, end=':')
			print(format(sq - (yns * 0.25 - 1005),".2f"))
		elif yns <= 55000:
			print(id, end=':')
			print(format(sq - (yns * 0.3 - 2755),".2f"))
		elif yns <= 80000:
			print(id, end=':')
			print(format(sq - (yns * 0.35 - 5505),".2f"))
		elif yns > 80000:
			print(id, end=':')
			print(format(sq - (yns * 0.45 - 13505),".2f"))
if __name__=="__main__":
	for arg in sys.argv[1:]:
		arg = arg.split(':')
		try:
			int(arg[1])
		except:
			print("Parameter Error")
			exit()
		gz = int(arg[1])
		id = arg[0]
		jisuan(gz)
