#!/usr/bin/env python3

class BaseClass:
	def c(self):
		return 3

class TestClass(BaseClass):
	def __init__(self):
		self.b = 2
		self._d = 4
	def add(self):
		pass
	def plusOne(self):
		c = self.c
		return self.add()+1

	

c = TestClass()
c.a = 1

print c.a
print c.b
print c.c()
print c._d