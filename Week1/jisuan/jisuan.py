#!/usr/bin/env python3
#gong zi = gz
#she bao bi li = bl
#ji shu xia xian = xx
#ji shu shang xian = sx
#ying na shui = yns
#ge shui = gs
#shui hou = sh
#she bao = sb

def jisuan(gz,bl,xx,sx):
	global sb
	global gs
	if gz <= xx:
		sb = float(format(xx * bl, ".2f"))
	elif gz >= sx:
		sb = float(format(sx * bl, ".2f"))
	else:
		sb = float(format(gz * bl, ".2f"))
	if gz - sb <= 3500:
		gs = format(0,".2f")
	else:
		yns = gz - sb - 3500
		if yns <= 1500:
			gs = format(yns * 0.03 - 0,".2f")
		elif yns <= 4500:
			gs = format(yns * 0.1 - 105,".2f")
		elif yns <= 9000:
			gs = format(yns * 0.2 - 555,".2f")
		elif yns <= 35000:
			gs = format(yns * 0.25 - 1005,".2f")
		elif yns <= 55000:
			gs = format(yns * 0.3 - 2755,".2f")
		elif yns <= 80000:
			gs = format(yns * 0.35 - 5505,".2f")
		elif yns > 80000:
			gs = format(yns * 0.45 - 13505,".2f")
if __name__=='__main__':
	jisuan(50000,0.165,2193,16446)
	print('she bao ', sb)
	print('ge shui ', gs)
