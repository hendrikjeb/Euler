# -*- coding: utf-8 -*-
# 
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

maxm = 999*999

stop = False
for g in xrange(maxm):
	getal = maxm - g
	s = str(getal)
	#zo test ik of het een palindroom is
	for i in xrange(len(s)/2):
		if s[i] != s[len(s)-(i+1)]:
			break
	else:
		#test of het getal gemaakt kan worden door twee getallen van elk drie cijfers
		#print getal
		for x in range(100, 1000):
			if getal/x < 1000:
				if getal % x == 0:
					#print '{} / {} = {}'.format(getal, x, getal/x)
					print getal
					stop = True
					break
		if stop:
			break
		