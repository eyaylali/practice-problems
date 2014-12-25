#Write a method, sum which takes a list of numbers and returns the sum of the numbers. 

def sum(lst):
	final_sum = 0
	for num in lst:
		final_sum += num
	return final_sum
	
print sum([1,2,3,4])
print sum([2,10,3])
