#!/usr/bin/env python3
class Test:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Test: {}'.format(self.name)

t = Test('Phthon')
print(t)
print(t.name)
