# -*- coding: utf-8 -*-
"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

from time import time
start = time()



a = 1
b = 2
c = 1000 - 3


while a < b and b < c and c > 0:
	stop = False
	#print a

	while b < c:
		# print b, c, ' ',
		if c*c == a*a + b*b:
			print '%d * %d * %d = %d' % (a, b, c, a*b*c)
			stop = True
			break
		b += 1
		c -= 1

	# print ''
	if stop:
		break

	a += 1
	b = a + 1
	c = 1000 - (a + b)






print 'Tijd: ', time() - start
