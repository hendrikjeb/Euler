# -*- coding: utf-8 -*-
"""
Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it 
lexicographic order. 

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
6, 7, 8 and 9?
"""

from time import time
start = time()

permutatie = ""
aant = 10 # aantal getallen in de permutatie 
getallen = range(0, aant) # de getallen in de permutatie

# maak een lijstje met voor het aantal getallen de bijbehorende faculteiten
f = map(lambda x: reduce(lambda x, y: x * y, range(1, x + 2)), xrange(aant))
f.insert(0, 1)

g = 1000000 # het nde getal waarvan je wil weten hoe zijn permutatie eruit ziet

for x in xrange(aant):
	g %= f[aant]
	aant -= 1
	
	permutatie += str(getallen[(g - 1) / f[aant]])
	
	for y in xrange(len(getallen)):
		if getallen[y] == getallen[(g - 1) / f[aant]]:
			getallen.pop(y)
			break
	
print permutatie

print 'Tijd: ', time() - start
