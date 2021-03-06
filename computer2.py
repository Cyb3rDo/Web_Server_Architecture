#!/usr/bin/env python3

import fake_database
from memcache import Memcache

cache = Memcache()

def printName():
	return str(__name__)

def updateLastMultiplied(a,b, result):
	key = 'lastFive'
	lastFiveList = cache.get(key)
	if lastFiveList:
		if len(lastFiveList) >= 5:
			# The list already had five items in it
			newList =  lastFiveList[1:]
			newList.append('{}x{}={}'.format(a,b,result))
			done = cache.set(key, newList)
		else:
			#The list had less than five items
			lastFiveList.append('{}x{}={}'.format(a,b,result))
			done = cache.set(key, lastFiveList)

	else:
		# There was not a cache so create one

		done = cache.set(key, ['{}x{}={}'.format(a,b,result)])

def lastMultipliedHandler():
	key = 'lastFive'
	last = cache.get(key)
	if last:
		return "Last 5 = {}".format(last)
	else:
		return "Russian not Used Before"
		

def multiplyHandler(a,b):
	
	key = (a,b)
	cachedAnswer = cache.get(key)
	if cachedAnswer:
		return cachedAnswer
	else:
		result = fake_database.russian(a,b)
		updateLastMultiplied(a,b,result)
		done = cache.set(key, result)
		return 'Latest Result: {}'.format(result)
		lastMultipliedHandler()


if __name__ == '__main__':
	multiplyHandler(2,6)
	multiplyHandler(5,6)
	multiplyHandler(10,6)
	multiplyHandler(23,6)
	multiplyHandler(4,6)
	multiplyHandler(11,6)
	multiplyHandler(200,6)
