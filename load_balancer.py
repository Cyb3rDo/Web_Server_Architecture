#!/usr/bin/env python3

# Server names
import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]

n = -1
def get_server():
	global n
	n += 1
	return SERVERS[n % len(SERVERS)]

## Testing load which needs balancing
if __name__ == '__main__':
	for i in range(3):
		server = get_server()
		print server.printName
		print server.multiplyHandler
		print server.lastMultipliedHandler
		print " "

