# -*- coding: utf-8 -*-
"""
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise 
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
"""

from time import time
start = time()

# De som van de hoeken van een vierkant met lengte n is steeds:
# (n^2) + (n^2 - (n - 1)) + (n^2 - 2(n - 1)) + (n^2 - 3(n - 1)) =
# (n^2) + (n^2 - n + 1) + (n^2 - 2n + 2) + (n^2 - 3n + 3) =
# 4n^2 - 6n + 6

# Tel de som van de hoeken van alle oneven vierkanten tot 1002 bij elkaar op;
# Tel daar de middelste 1 bij op.

print sum(map(lambda n: 4 * n**2 - 6*n + 6, range(3, 1002, 2))) + 1

print 'Tijd: ', time() - start
