#! /usr/bin/python3

nums = []

m = 2020

for n in nums:
	if (m - n) in nums:
		print( n * (m - n) )
		break

for n in nums:
	for o in nums:
		if (m - n - o) in nums:
			print( n * o * (m - n - o) )
			break
