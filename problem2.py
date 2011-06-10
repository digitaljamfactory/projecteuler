


def even_valued_fib_numbers(num):
	a,b = 0,1
	while a < num:
		if a%2 == 0:
			yield a
		a,b = b, a +b


if __name__ == '__main__' :	
	print sum(even_valued_fib_numbers(4000000))		

