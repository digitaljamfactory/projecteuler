value = 0


while value < 10001:
	for i in range (2, 1000000000) :
		for j in range(2,i) :
			if i % j == 0:
				#print i, 'equals', j , '*', i/j
				break
		else:
		    print i
		    value += 1