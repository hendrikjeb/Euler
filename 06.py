# -*- coding: utf-8 -*-
"""


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares 
of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum 
of the squares of the first one hundred natural numbers and the square of the sum.


"""

j = 0
k = 0

for i in range(1, 101):
	j += i*i
	k += i

print k*k - j

# Zo kan het ook, schijnt:
print sum(range(1,101)) ** 2  -  sum([i*i for i in range(1,101)])