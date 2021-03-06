# -*- coding: utf-8 -*-
"""
Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values 
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible 
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes 
for the consecutive values n = 0 to 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n, starting with 
n = 0.
"""

from time import time
start = time()

# Maak een lijst met priemgetallen
p = 126479
priem = range(0, p)
priem[1] = 0

for i in range(2, p):
	if priem[i] != 0:
		j = i*i
		
		while j < p:
			priem[j] = 0
			j += i

maximum = 0
a = -1000

while a < 1000:
	b = -1000
	while b < 1000:
		n = 0
		while priem[abs(n**2 + a * n + b)] != 0:
			n += 1
		
		if n > maximum: 
			maximum = n
			print a, b, n, a * b
			
		b += 1
	a += 1

print 'Tijd: ', time() - start
