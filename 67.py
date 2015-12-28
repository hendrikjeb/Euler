# -*- coding: utf-8 -*-
"""
Problem 67: Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in 67_triangle.txt 
a 15K text file containing a triangle with one-hundred rows.
"""

from time import time
start = time()

oefendriehoek = map(lambda x: map(lambda y: int(y), x.split(" ")), """\
3
7 4
2 4 6
8 5 9 3\
""".split("\n"))

# print de driehoek
# for rij in driehoek:
#   str_rij = "%02d" % rij[0]
#   for x in range(1, len(rij)):
#     str_rij += "  " + "%02d" % rij[x]
#   print "{:^58}".format(str_rij)

for x in xrange(len(driehoek) - 1):
  x = len(driehoek) - 1 - x
  for y in xrange(len(driehoek[x-1])):
	if driehoek[x][y + 1] > driehoek[x][y]:
	  driehoek[x-1][y] += driehoek[x][y + 1]
	else:
	  driehoek[x-1][y] += driehoek[x][y]

print driehoek[0][0]

print 'Tijd: ', time() - start
