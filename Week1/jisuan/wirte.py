#!/usr/bin/env python3
def Write(info,write_file):
	with open(write_file, 'w') as wfile:
#		wfile.write(info)
		wfile.write(info\n)
if __name__=='__main__':
	Write('101,3500,500.5,0.00,2500','/home/shiyanlou/gongzi.csv')
