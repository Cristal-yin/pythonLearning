def findMinAndMax(L):
	for x in L:
		min = x
		max = x
		print(min,max)
		if min > x:
			min = x
		if max < x:
			max = x
	return min,max
