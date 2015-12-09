# -*- coding: utf-8 -*-

a = 1
b = 1
z = 0

while a <= 4000000:
	a, b = b, a + b
	if a % 2 == 0:
		z += a

print z