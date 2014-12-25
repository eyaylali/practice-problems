#Write a method, is_prime?, that takes a number num and returns true if it is prime and false otherwise.

def is_prime(n):
	for num in range(2,n):
		if n % num == 0:
			return False
	return True

print is_prime(4)
print is_prime(15)
print is_prime(7)