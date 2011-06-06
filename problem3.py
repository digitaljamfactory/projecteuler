
def prime_factorise(number, factors=None):
	if factors is None:
		factors = []
	max = int(number**.5) +1
	for i in xrange(2,max):
		if not number%i:
			factors.append(i)
			break
	else:
		factors.append(number)
		return factors
	return prime_factorise(number/i, factors)	
			
			
print prime_factorise(600851475143)
		
	