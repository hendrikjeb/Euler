# -*- coding: utf-8 -*-
"""
Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

from time import time
start = time()

teller = 1
max100 = 200

while max100 >= 0:
	max50 = max100
	max100 -= 100

	while max50 >= 0:
		max20 = max50
		max50 -= 50

		while max20 >= 0:
			max10 = max20
			max20 -= 20

			while max10 >= 0:
				max5 = max10
				max10 -= 10	

				while max5 >= 0:
					teller += max5/2 + 1
					max5 -= 5
					
print teller

print 'Tijd: ', time() - start
