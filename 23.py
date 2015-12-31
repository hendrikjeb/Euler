# -*- coding: utf-8 -*-
"""
Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though 
it is known that the greatest number that cannot be expressed as the sum of two 
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
"""

from time import time
start = time()

maxm = 28123 + 1
# maxm = 1000

resultaten = []
lijst = []

wortel = 3
for getal in range(12, maxm):
	if getal == (wortel + 1) * (wortel + 1):
		wortel += 1

	som = 1
	for d in range(2, wortel + 1):
		if getal % d == 0:
			som += d + getal/d
			if d * d == getal:
				som -= d

	if som > getal:
		lijst.append(getal)

for x in range(1, maxm):
	y = 0
	while True:
		try:
			if x - lijst[y] in lijst:
				# print x
				break
			else:
				if x > lijst[y]:
					y += 1
				else:
					resultaten.append(x)
					# print "!", x
					break
		except IndexError: 
			resultaten.append(x)
			print "(%d)" % x
			break

print sum(resultaten)

print 'Tijd: ', time() - start
