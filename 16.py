# -*- coding: utf-8 -*-
"""
Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from time import time
start = time()

som = 0

for l in str(2**1000)[:]:
	som += int(l)

print som

print 'Tijd: ', time() - start
