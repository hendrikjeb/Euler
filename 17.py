# -*- coding: utf-8 -*-
"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

from time import time
start = time()

getallen = {
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "fifteen",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "thirty",
40: "forty",
50: "fifty",
60: "sixty",
70: "seventy",
80: "eighty",
90: "ninety"
}

def maakgetal(g):
	if g < 20:
		print getallen[g]
	elif g > 19 and g < 100:
		if g % 10 != 0:
			tiental = g - (g % 10)
			print getallen[tiental] + "-" + getallen[g % 10]
		else:
			print getallen[g]

for x in range(1, 100):
	maakgetal(x)

for y in range(1, 10):
	print getallen[y], "hundred"
	for z in range(1, 100):
		print getallen[y], "hundred", "and",
		maakgetal(z)

print "one", "thousand"

print 'Tijd: ', time() - start
