#!/usr/bin/env python3

#The Russian Peasant's Algorithm

#Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

import time

def russian(a,b):

	x = a; y = b 						# Semicolon -> Compund Statement
	z = 0								# Acmulator
	while x > 0:  						# While loop begins
		if x % 2 == 1: z += y 			# Modulo operator
		y = y << 1 						# Shift binary over to left = multiply with 2
		x = x >> 1 						# Shift binary over to right = divide by 2
	return z							# Return z
	 							

def test_russian():
	start_time = time.time()
	print russian(357, 16)
	print "Russian Algoritm took %f seconds" % (time.time() - start_time)
	assert russian(357, 16) == 5712

if __name__ == '__main__':
	test_russian()