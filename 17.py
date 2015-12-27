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

teller = 0

for x in range(0, 10):
	if x != 0:
		# maak voor de getallen 1 - 9 het eerste honderdtal
		teller += len(getallen[x]) + 7
		print getallen[x], "hundred",
		print len(getallen[x]) + 7,
		print teller

		# voorbereidingen om later bijv "one hundred and" voor een getal te 
		# kunnen zetten
		honderdtal = "{} {} {} ".format(getallen[x], "hundred", "and")
		lengte_honderdtal = len(getallen[x]) + 10
	else:
		# voor de getallen onder de honderd
		honderdtal = ""
		lengte_honderdtal = 0

	for g in range(1, 100):
		if g > 19 and g < 100 and g % 10 != 0:
			teller += len(getallen[g - (g % 10)]) + len(getallen[g % 10]) + lengte_honderdtal
			print honderdtal + getallen[g - (g % 10)] + "-" + getallen[g % 10],
			print len(getallen[g - (g % 10)]) + len(getallen[g % 10]) + lengte_honderdtal,
			print teller
		else:
			teller += len(getallen[g]) + lengte_honderdtal
			print honderdtal + getallen[g],
			print len(getallen[g]) + lengte_honderdtal,
			print teller

teller += len("one") + len("thousand")
print "one", "thousand",
print len("one") + len("thousand"),
print teller

print 'Tijd: ', time() - start
