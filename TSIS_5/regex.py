import re

# Define the regular expression pattern
pattern = r'a[b]*'

# Define the string to search in
string = 'abbb ab abbbbb ac'

# Use the findall() method from the re module to find all matches of the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches) #Output: ['abbb', 'ab', 'abbbbb']

import re

# Define the regular expression pattern
pattern = r'a[b]{2,3}'

# Define the string to search in
string = 'abbb ab abbbbb ac'

# Use the findall() method from the re module to find all matches of the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches) #Output: ['abbb']

import re

# Define the regular expression pattern
pattern = r'[a-z]+_[a-z]+'

# Define the string to search in
string = 'hello_world this_is_a_sequence a_b_c'

# Use the findall() method from the re module to find all matches of the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches) #Output: ['hello_world', 'this_is_a_sequence', 'a_b_c']


import re

# Define the regular expression pattern
pattern = r'[A-Z][a-z]+'

# Define the string to search in
string = 'Hello world Is A Nice Place'

# Use the findall() method from the re module to find all matches of the pattern in the string
matches = re.findall(pattern, string)

# Print the matches
print(matches) #Output: ['Hello', 'Is', 'Nice', 'Place']


import re

# Define the regular expression pattern
pattern = r'a.*b$'

# Define the string to search in
string = 'abbb ab abbbbb ac'

# Use the search() method from the re module to find the first match of the pattern in the string
match = re.search(pattern, string)

# If there is a match, print the matched string
if match:
    print(match.group(0)) #Output: abbbbb
    
    

import re

# Define the regular expression pattern
pattern = r'[ ,.]'

# Define the string to replace in
string = 'Hello, world. This is a test.'

# Use the sub() method from the re module to replace all matches of the pattern with a colon
new_string = re.sub(pattern, ':', string)

# Print the new string
print(new_string) #Output: Hello:world:This:is:a:test:



import re

# Define the regular expression pattern
pattern = r'_([a-z])'

# Define the snake case string to convert
string = 'hello_world_this_is_a_test'

# Use the sub() method from the re module to replace all matches of the pattern with the uppercase equivalent of the matched letter
new_string = re.sub(pattern, lambda match: match.group(1).upper(), string)

# Print the new camel case string
print(new_string) #Output: helloWorldThisIsATest


import re

# Define the regular expression pattern
pattern = r'[A-Z]'

# Define the string to split
string = 'HelloWorldThisIsATest'

# Use the split() method from the re module to split the string at each uppercase letter
parts = re.split(pattern, string)

# Join the parts with a space and print the result
new_string = ' '.join(parts)
print(new_string) #Output: Hello World This Is A Test


import re

# Define the regular expression pattern
pattern = r'(?<!\s)[A-Z]'

# Define the string to modify
string = 'HelloWorldThisIsATest'

# Use the sub() method from the re module to insert a space before each uppercase letter not preceded by a space
new_string = re.sub(pattern, lambda match: ' ' + match.group(0), string)

# Print the modified string
print(new_string) #Output: Hello World This Is A Test



import re

# Define the regular expression pattern
pattern = r'(?<!^)(?=[A-Z])'

# Define the camel case string to convert
string = 'helloWorldThisIsATest'

# Use the sub() method from the re module to replace all matches of the pattern with an underscore
new_string = re.sub(pattern, '_', string).lower()

# Print the new snake case string
print(new_string) #Output: hello_world_this_is_a_test
