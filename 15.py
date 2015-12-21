# -*- coding: utf-8 -*-
"""
Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from time import time

# Het aantal routes is steeds de som van de vorige twee knooppunten.
# Als je bij ieder knooppunt het opschrijft hoeveel keuzemogelijkheden je hebt,
# dan ziet dit er zo uit bij een vierkant met zijde 4:
# 70 35 15  5  1
# 35 20 10  4  1
# 15 10  6  3  1
#  5  4  3  2  1
#  1  1  1  1  1
# Draai dit vierkant iets meer dan een slag en je hebt de driehoek van Pascal.
# Het volgende kan je zeggen:
# Het aantal routes is gelijk aan het hoogste getal uit de rij met 
# lengte((2x de zijde van het vierkant) + 1)

# Omdat het kan, gebruikersinput:
zijde = int(raw_input("Zijde: "))

start = time()

maxrijlengte = zijde * 2 + 1
rij = []

while len(rij) < maxrijlengte:
	for x in range(0, len(rij) - 1):
		rij[x] += rij[x + 1]
	
	rij.insert(0, 1)
print rij[zijde]


print 'Tijd: ', time() - start
