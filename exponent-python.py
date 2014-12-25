#Write a method, pow, that takes two (non-negative, integer) numbers, base and exponent and 
#returns base raised to the exponent power.

def pow(base, exponent):
	result = 1
	for num in range (1, exponent+1):
		result *= base
	return result
		
print pow(2,3)
print pow(4,3)
	
	