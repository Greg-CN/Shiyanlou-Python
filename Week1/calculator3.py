#!/usr/bin/env python3

import sys
import json
import os

args = sys.argv[1:]
try:
	conf_file = args[args.index('-c')+1]
	if os.path.exists(conf_file) == False:
		print("Can't find ", conf_file)
except:
	print("Missing config file")
try:
	usr = args[args.index('-d')+1]
	if os.path.exists(usr) == False:
		print("Can't find ", usr)
except:
	print("Missing user file")
try:
	out = args[args.index('-o')+1]
	if os.path.exists(out) == True:
		print(out, " already exist")
except:
	print("Missing output path")
with open(conf_file) as conf:
	conf = conf.readlines()
config = {}
for cfg in conf:
	try:
		float(cfg.split('=')[1].strip())
	except:
		print("Config file Parameter Errot")
	config[cfg.split('=')[0].strip()] = float(cfg.split('=')[1].strip())
try:
	config['JiShuL']
	config['JiShuH']
	config['YangLao']
	config['YiLiao']
	config['ShiYe']
	config['GongShang']
	config['ShengYu']
	config['GongJiJin']
except:
	print("Config file error")
shebao = config['YangLao'] + config['YiLiao'] + config['ShiYe'] + config['GongShang'] + config['ShengYu'] + config['GongJiJin']
