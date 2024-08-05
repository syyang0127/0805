def fun1():
	print('fun1 함수를 호출')

def fun2():
	print('fun2 합수를 호출')

def fun3():
	fun1()
	fun2()
	print('fun3 합수를 호출')

fun3()
