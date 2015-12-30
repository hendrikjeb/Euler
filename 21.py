# -*- coding: utf-8 -*-
"""
Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from time import time
start = time()

lijst = 10001 * [0]
vrienden = []

wortel = 1
for getal in range(1, 10001):
	if getal == (wortel + 1) * (wortel + 1):
		wortel += 1

	som = 1
	for d in range(2, wortel + 1):
		if getal % d == 0:
			som += d + getal/d
			if d * d == getal:
				som -= d
	lijst[getal] = som

	if som < getal:
		if lijst[som] == getal:
			vrienden.append(lijst[som] + lijst[getal])
			print ":)", lijst[som], lijst[getal]

print sum(vrienden)

print 'Tijd: ', time() - start
