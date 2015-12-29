# -*- coding: utf-8 -*-
"""
Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research 
for yourself.

  - 1 Jan 1900 was a Monday.
  - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  - A leap year occurs on any year evenly divisible by 4, but not on a century 
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
"""

from time import time
start = time()

# Als je het jaar steeds in maart begint, dan geldt dat voor ieder jaar steeds
# twee zondagen op de eerste dag van de maand vallen, behalve als die zondag op 
# 1 augustus of 1 oktober valt. 
# Als 1 oktober een zondag is, dan is 1 augustus een dinsdag. Het volstaat dus 
# om te kijken in welke jaren 1 augustus op een zondag of op een dinsdag valt. 
# In die jaren is er één zondag, in alle andere jaren zijn er twee. Op het eind 
# van de berekening moet je nog even corrigeren voor als januari of februari 
# een zondag had (in welk geval 1 augustus het jaar daarvoor resp. op een maandag 
# of een vrijdag zou vallen).


aug = 3 # in 1900 valt 1 augustus op een woensdag
teller = 0 # in 1901 hebben januari noch februari een zondag als eerste dag

for x in range(1901, 2001):
	aug += 1
	if x % 4 == 0:
		aug += 1
	teller += 2
	if aug % 7 in [0, 2]:
		teller -= 1

if aug in [1, 5]:
	teller -= 1

print teller

print 'Tijd: ', time() - start
