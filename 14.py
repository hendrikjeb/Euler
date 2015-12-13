# -*- coding: utf-8 -*-
"""Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms.  Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Tijd:  44.3609998226

from time import time
start = time()

lijst = range(0, 1000000)
maxm = 0

for x in lijst:
	teller = 1
	if x == 0:
		continue
	else:
		y = x
		while x > 1:
			teller += 1
			if x % 2 == 0:
				x /= 2
			else:
				x = 3 * x + 1
			
			try:
				lijst[x] = 0
			except IndexError:
				pass

		if maxm < teller:
			maxm = teller
			print y, ":", maxm

print 'Tijd: ', time() - start
