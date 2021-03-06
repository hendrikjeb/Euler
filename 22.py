# -*- coding: utf-8 -*-
"""
Problem 22: Names scores

Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position in the list 
to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from time import time
from csv import reader

start = time()

resultaat = 0

with open("22_names.txt") as names:
	csvreader = reader(names, delimiter=',', quotechar='"')

	for namen in csvreader:
		namen = sorted(namen)

		for x in xrange(len(namen)):
			som = 0
			for letter in namen[x][:]:
				som += ord(letter) - 64

			resultaat += (x + 1) * som

print resultaat

print 'Tijd: ', time() - start
