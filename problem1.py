

def sum_natural_numbers(num):
		return sum(n for n in xrange(num) if n%3 == 0 or n%5 ==0)
		
if __name__ == '__main__' :
	print sum_natural_numbers(1000)