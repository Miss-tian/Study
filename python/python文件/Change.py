def scope_test():
	def do_local():
		spam="我是局部变量"
	def do_nonlocal():
		spam="我不是局部变量也不是全局变量"
	def do_global():
		global spam
		spam="我是全局变量"
	spam="原来的值"
	do_local()
	print("局部变量赋值后：",spam)
	do_nonlocal()
	print("nonlocal 变量赋值后:",spam)
	do_global()
	print("全局变量赋值后",spam)
	
scope_test()
print("全局变量：",spam)
