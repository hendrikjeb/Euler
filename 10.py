# -*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from math import sqrt

from time import time
start = time()

# lijst = range(3, 50, 2)

# for x in lijst:
# 	if x == 0:
# 		continue
# 	#print x,
# 	if x in [11, 101, 1003, 10001, 100001]:
# 		lijst = list(set(lijst))
# 		print x
# 	for y in range(x, len(lijst)):
# 		if lijst[y] <= x:
# 			continue
# 		if lijst[y] % x == 0:
# 			lijst[y] = 0
# 	# print ''

getal = 20000000

lijst = range(0, getal)

for i in range(2, getal):
	if lijst[i] != 0:
		j = i*i
		
		while j < getal:
			lijst[j] = 0
			j += i
		
		
lijst[1] = 0


lijst = list(set(lijst))

z = 0

for h in lijst:
	z += h

print z

print 'Tijd: ', time() - start