
value = 0

n = 4000000
a,b = 0,1
while a < n:
		if a%2 == 0:
			value += a;
		a,b = b, a +b
		
		
print value