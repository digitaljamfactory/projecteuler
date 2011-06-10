
def sum_of_squares(num):
	return sum((num * num for num in xrange(num)))
	
def square_of_sums(num):
	
	return sum(num for num in xrange(num)) * sum(num for num in xrange(num)) 

def difference_sum_of_squares_and_square_of_sums(num) :	
	return square_of_sums(num) - sum_of_squares(num)
	
if __name__ == '__main__' :
	print difference_sum_of_squares_and_square_of_sums(101)