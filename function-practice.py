# Write a function that takes a list and returns a new list with only the odd numbers.

def odd_list(lst):
    final_list = []
    for element in lst:
        if element % 2 != 0:
            final_list.append(element)
    return final_list

# Write a function that takes a list and returns a new list with only the even numbers.

def even_list(lst):
    final_list = []
    for element in lst:
        if element % 2 == 0:
            final_list.append(element)
        return final_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.

def four_greater(lst):
    final_list = []
    for element in lst:
        if len(element) >= 4:
            final_list.append(element)
        return final_list

# Write a function that finds the smallest element in a list of integers and returns it.

def smallest(lst):
    smallest_int = lst[0]
    for element in lst:
        if element < smallest_int:
            smallest_int = element
    return smallest_int


# Write a function that finds the largest element in a list of integers and returns it.

def smallest(lst):
    largest_int = 0
    for element in lst:
        if element > largest_int:
            largest_int = element
    return largest_int

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.

def divByTwo(lst):
    final_list = []
    for element in lst:
        final_list.append(element/2.0)
    return final_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.

def lengthMachine(lst):
    final_list = []
    for element in lst:
        final_list.append(len(element))
    return final_list

# Write a function (using iteration) that sums all the numbers in a list.

def summingMachine(lst):
    final_sum = 0
    for element in lst:
        final_sum += element
    return final_sum

# Write a function that multiplies all the numbers in a list together.

def multiplyingMachine(lst):
    final = 0
    for element in lst:
        final *= element
    return final

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.

def concat(lst):
    final = ""
    for element in lst:
        final += element
    return final

# Write a function that takes a list of integers and returns the average (without using the avg method)

def averageIt(lst):
    final_sum = 0
    for element in lst:
        final_sum += element
    return final_sum / float(len(lst))




