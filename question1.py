
value = 0

for i in range(1000):
    q,r = divmod(i,3)
    if i%3 == 0 or i%5 == 0:
	    value += i

	
print value