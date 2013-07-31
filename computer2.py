#!/usr/bin/env python3

import fake_database

CACHE = {}

def printName():
	return str(__name__)

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
		return "Last 5 = {}".format(CACHE[key])
	else:
		return "Russian not Used Before"
		

def multiplyHandler(a,b):
	
	cacheKey = (a,b)
	if cacheKey in CACHE:
		return CACHE[cacheKey]
	else:
		result = fake_database.russian(a,b)
		updateLastMultiplied(a,b,result)
		CACHE[cacheKey] = result
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
