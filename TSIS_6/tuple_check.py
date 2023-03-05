# prompt the user to enter the values of the tuple (separated by commas)
input_str = input()

# convert the input string to a tuple of boolean values
my_tuple = tuple(map(bool, input_str.split(',')))

# use the "all()" function to check if all elements of the tuple are true
result = all(my_tuple)

# print the result
print(result)
