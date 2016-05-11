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

t2 = 1
max100, t100 = 200, 0

while max100 >= 0:
	max50, t50 = max100, 0

	while max50 >= 0:
		max20, t20 = max50, 0

		while max20 >= 0:
			max10, t10 = max20, 0

			while max10 >= 0:
				max5, t5 = max10, 0

				while max5 >= 0:
					max2 = max5
					
					while max2 >= 0:
						max2 -= 2
						t2 += 1
					
					max5 -= 5
					t5 += 1
				
				max10 -= 10
				t10 += 1		

			max20 -= 20
			t20 += 1
		
		max50 -= 50
		t50 += 1

	max100 -= 100
	t100 += 1

print t2

print 'Tijd: ', time() - start
