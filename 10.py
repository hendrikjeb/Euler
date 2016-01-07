# -*- coding: utf-8 -*-
"""
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from time import time
start = time()

getal = 20000000

lijst = range(0, getal)
lijst[1] = 0

for i in range(2, getal):
	if lijst[i] != 0:
		j = i*i
		
		while j < getal:
			lijst[j] = 0
			j += i

print sum(lijst)

print 'Tijd: ', time() - start
