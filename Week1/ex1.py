#!/usr/bin/env python3
class Dog(object):
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		sefl._name = value
	def bark(self):
		print(self.get_name() + 'is making sound wang wang wang...')

class Cat(object):
	def __init__(self, name):
		self._name = name
	def get_name(self):
		return self._name
	def set_name(self, value):
		self._name = vlaue
	def mew(self):
		print(self.get_name() + 'is making sound miu miu miu...')

dog = Dog('wangcai')
cat = Cat('Kitty')
dog.bark()
cat.mew()