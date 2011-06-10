
#from itertools import *

#for i in count(10) :
	
#	if (i%2 ==0 and i%3 ==0 and i%4 == 0 and i%5 == 0 and i%6==0 and i%7 == 0 and i%8 == 0 and i%9 == 0 and i%11 == 0 and i%12 == 0 and i%13 == 0 and i%14 ==0 and i%15 == 0 and i%16 ==0 and i%17 == 0 and i%18 == 0 and i%19 == 0 and i%20 == 0) :
#		print i
#		break
#232792560



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
			

def lcm(min,max) :
	
	for i in xrange(min,max) :
		prime_factorise(i)
		
			
if __name__ == '__main__' :
	lcm(2,10)