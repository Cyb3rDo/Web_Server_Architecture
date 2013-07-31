#!/usr/bin/env python3

# Server names
SERVERS = ['APP1', 'APP2', 'APP3']
#SERVERS = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7']

# --Algoritm 1--

# n = -1
# def get_server():
#  	global n
#  	n += 1
#  	return SERVERS[n % len(SERVERS)]

# --Algoritm 2--

# import itertools
# ## Infinite loop iterator
# cycle = itertools.cycle(SERVERS)
# def get_server():
# 	global cycle
# 	return cycle.next()

# --Algoritm 3--
def get_server():
	try:
		return next(get_server.s)
	except StopIteration:
		get_server.s = iter(SERVERS)
		return next(get_server.s)
setattr(get_server, 's', iter(SERVERS))

# --Algoritm 4--
# def get_server():
# 	def f():
# 		while True:
# 			i = SERVERS.pop(0)
# 			SERVERS.append(i)
# 			yield i
# 	return next(f())



## Testing load which needs balancing
if __name__ == '__main__':
	for i in range(9):
		print get_server()

