#!/usr/bin/env python3
import sys
import json
import os
class Config:
	def __init__(self,conf_file):
		with open(conf_file) as conf:
			conf = conf.readlines()
		self.config = {}
		for cfg in conf:
			try:
				float(cfg.split('=')[1].strip())
			except:
				print("Config file Parameter Errot")
			self.config[cfg.split('=')[0].strip()] = float(cfg.split('=')[1].strip())
		try:
			self.config['JiShuL']
			self.config['JiShuH']
			self.config['YangLao']
			self.config['YiLiao']
			self.config['ShiYe']
			self.config['GongShang']
			self.config['ShengYu']
			self.config['GongJiJin']
		except:
			print("Config file error")
	def get_config(self,cf):
		return self.config[cf]
	def get_shebao(self):
		return self.config['YangLao'] + self.config['YiLiao'] + self.config['ShiYe'] + self.config['GongShang'] + self.config['ShengYu'] + self.config['GongJiJin']
	def get_JiShuL(self):
		return self.config['JiShuL']
	def get_JiShuH(self):
		return self.config['JiShuH']


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



def Write(info,write_file):
        with open(write_file, 'w') as wfile:
                wfile.write(info)



if __name__=='__main__':
	args = sys.argv[1:]
	try:
		conf_file = args[args.index('-c')+1]
		if os.path.exists(conf_file) == False:
			print("Can't find ", conf_file)
			exit()
	except:
		print("Missing config file")
		exit()
	try:
		usr = args[args.index('-d')+1]
		if os.path.exists(usr) == False:
			print("Can't find ", usr)
			exit()
	except:
		print("Missing user file")
		exit()
	try:
		out = args[args.index('-o')+1]
		if os.path.exists(out) == True:
			print(out, " already exist")
			exit()
	except:
		print("Missing output path")
		exit()
	config = Config(conf_file)
	
