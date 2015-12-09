# -*- coding: utf-8 -*-
"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
from time import time
s = time()

x = 3
priem = [2, 3]

while len(priem) < 10001:
	x += 2
	for y in priem:
		if x % y == 0:
			break
	else:
		priem.append(x)

print priem[-1]

print time() - s