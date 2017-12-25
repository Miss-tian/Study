def findMinAndMax(L):
	if len(L)==0:
		return (None,None)
	elif len(L)==1:
		return (L[0],L[0])
	else:
		min=L[0]
		max=L[0]
		for x in L:
			if x<min:
				min=x
			if x>max:
				max=x
		return (min,max)
