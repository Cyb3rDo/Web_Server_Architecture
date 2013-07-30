#!/usr/bin/env python3

import fake_database

CACHE = {}

def printName():
	print str(__name__)

def updateLastMultiplied(a,b, result):
	key = 'lastFive'
	lastFiveList = CACHE.get(key)
	if lastFiveList:
		if len(lastFiveList) >= 5:
			# The list already had five items in it
			newList =  lastFiveList[1:]
			newList.append('{}x{}={}'.format(a,b,result))
			CACHE[key] = newList
		else:
			#The list had less than five items
			lastFiveList.append('{}x{}={}'.format(a,b,result))
			CACHE[key] = lastFiveList

	else:
		# There was not a Cache so create one

		CACHE[key] = ['{}x{}={}'.format(a,b,result)]

def lastMultipliedHandler():
	key = 'lastFive'
	if key in CACHE:
		print "Last 5 = {}".format(CACHE[key])
		print "-"*8
		print " "
	else:
		print "Russian not Used Before"
		print "-"*8
		print " "

def multiplyHandler(a,b):
	
	cacheKey = (a,b)
	if cacheKey in CACHE:
		print CACHE[cacheKey]
	else:
		result = fake_database.russian(a,b)
		updateLastMultiplied(a,b,result)
		CACHE[cacheKey] = result
		print 'Latest Result: {}'.format(result)
		lastMultipliedHandler()


if __name__ == '__main__':
	multiplyHandler(2,6)
	multiplyHandler(5,6)
	multiplyHandler(10,6)
	multiplyHandler(23,6)
	multiplyHandler(4,6)
	multiplyHandler(11,6)
	multiplyHandler(200,6)
