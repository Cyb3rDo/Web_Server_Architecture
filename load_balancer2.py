#!/usr/bin/env python3

# Import Servers (modules)
import computer1
import computer2
import computer3

# List of servers
SERVERS = [computer1, computer2, computer3]


# -- Load balance algoritm --

n = -1
def get_server():
 	global n
 	n += 1
 	return SERVERS[n % len(SERVERS)]


## Testing load which needs balancing
if __name__ == '__main__':
	from random import randint
	#simulate a number of requests with this loop
	for i in range(10):
		##: Generate som 'Requested' numbers
		#a = randint(5, 99)
		#b = randint(5, 99)
		z = randint(1,21)
		a = [44,85,123,55,32,34,87][z%7]
		b = [54,15,32,98,311,28,54][z%7]

		# Run the load balancer algorithm to get us a computer
		server = get_server()

		# Print results
		print server.printName()
		print server.multiplyHandler(a,b)
		print server.lastMultipliedHandler()
		print " "




