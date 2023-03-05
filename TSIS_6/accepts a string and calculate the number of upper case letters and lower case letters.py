# define a function to count the number of upper case and lower case letters
def count_upper_lower(string):
    # initialize counters for upper case and lower case letters
    upper_count = 0
    lower_count = 0
    
    # iterate over each character in the string
    for char in string:
        # increment the counter for upper case letters if the character is upper case
        if char.isupper():
            upper_count += 1
        # increment the counter for lower case letters if the character is lower case
        elif char.islower():
            lower_count += 1
    
    # return a tuple containing the counts of upper case and lower case letters
    return (upper_count, lower_count)

# prompt the user to enter a string
string = input()

# call the count_upper_lower function to count the number of upper case and lower case letters in the string
result = count_upper_lower(string)

# print the results
print(result[0])
print(result[1])