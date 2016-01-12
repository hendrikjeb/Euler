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

munten = [200, 100, 50, 10, 5, 2, 1]
lijst = [[200]]

x = 0
while True:
	try:
		x += 1
		lijst.append([])
		_200 = 200
		y = 0
		while _200 > 0:
			if _200 < munten[y] or munten[y] == lijst[x - 1][-1]:
				y += 1
			else:
				lijst[x].append(munten[y])
				_200 -= munten[y]
				print munten[y]
	except IndexError:
		print "!"
		break

print 'Tijd: ', time() - start
