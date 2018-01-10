def quadratic(a,b,c):
	#保证符合方程的构成，只能是数字或者浮点数，非数字时抛错
	for x in [a,b,c]:
		if not isinstance(x,(int,float)):
			raise TypeError('bad operand type')
		#方程由δ决定是否有解，小于0无解
		s = b*b -4*a*c
		if s <0:
			return '此方程无解'
		elif s==0:
			x1=-b/(2*a)
			return '此方程有两个相等的根：x1=x2',x1
		else:
			x1=(-b-s)/(2*a)
			x2=(-b+s)/(2*a)
			return '此方程有两个不同的根，x1=:',x1,'x2:',x2
