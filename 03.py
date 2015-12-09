# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
getal = 600851475143  

lijst = []

p = 2
while getal > 1:
	if getal % p == 0:
		print p, getal
		getal /= p
	else:
		p += 1

print p

# Oude code
# # priemgetallen vinden
# helft = getal / 2
# priem = []
# for x in range(2, helft + 1):
# 	for y in priem:
# 		if x % y == 0:
# 			break
# 	else:
# 		priem.insert(0, x)

# print priem

# for x in priem:
# 	if getal % x == 0:
# 		print x