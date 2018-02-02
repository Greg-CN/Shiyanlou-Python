#!/usr/bin/env python3
def connect(ipaddress, *ports, **kw):
	print("IP: ", ipaddress)
	for port in ports:
		print("Port: ", port)
	for key,value in kw.items():
		print('{}: {}'.format(key,value))
params = (22, 23, 24)
prop = {'devices': 'eth0', 'proto': 'static'}
connect('192.168.1.1',*params, **prop)
