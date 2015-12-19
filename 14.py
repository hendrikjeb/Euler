# -*- coding: utf-8 -*-
"""Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms.  Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# Tijd:  3.09

from time import time
start = time()

lijst = [0, 1] + 10000000 * [0]
maxm = [1, 1]

bugfix = time() # Voorals bij start alleen 999999 wordt opgeschreven...

for start in range(2, 1000000):
	# controleer of de lengte van de Collatz-reeks voor een getal al is gevonden
	if lijst[start] == 0:
		x = start
		tijdelijk = []
		while lijst[start] == 0:

		# Maak een tijdelijke lijst met alle getallen die je vindt. 
		# Vervang daarbij de getallen die buiten de index van de grote lijst 
		# vallen door 0.
			while True:
				try:
					if lijst[x] != 0:
						break
					else:
						tijdelijk.append(x)
				except IndexError:
					tijdelijk.append(0)
				
				if x % 2 == 0:
					x /= 2
				else:
					x = 3 * x + 1	
			
			collatz = lijst[x]

			# Onderstaande loop zorgt dat voor alle gevonden getallen, in de lijst
			# komt te staan hoelang hun Collatzreeks is.
			while len(tijdelijk) != 0:
				collatz += 1
				z = tijdelijk.pop()
				# print "lijst[%d] = %d" % (z, collatz)
				lijst[z] = collatz

		if maxm[1] < lijst[start]:
			maxm = [start, lijst[start]]
			print "%d => %d" % (maxm[0], maxm[1])

print 'Tijd: ', time() - start
print 'Tijd: ', time() - bugfix
