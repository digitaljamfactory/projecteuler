
def find_largest_palindrome(min, max): 
	largest = 0
	for i in range(min,max):
		for j in range(min,max) :
			a = i*j
			if str(a) == str(a)[::-1] :
				if a > largest :
					largest = a		
	return largest				
				
if __name__ == '__main__' :	
	print find_largest_palindrome(100,1000)


