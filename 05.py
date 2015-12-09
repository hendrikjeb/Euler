# -*- coding: utf-8 -*-
"""2520 is the smallest number that can be divided by each of the numbers 
	from 1 to 10 without any remainder. 
	What is the smallest positive number 
	that is evenly divisible by all of the numbers from 1 to 20?"""

doorgaan = True
getal = 2520

while doorgaan == True:
	doorgaan = False
	for x in xrange(11, 21):
		if getal % x != 0:
			if getal % 1000 == 0:
				print getal, x
			getal += 2520
			doorgaan = True
			break

print getal