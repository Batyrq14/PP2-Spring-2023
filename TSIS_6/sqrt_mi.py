import time
import math

# prompt the user to enter two numbers
num = int(input("Enter a number: "))
delay = int(input("Enter a delay time (in milliseconds): "))

# convert the delay time from milliseconds to seconds
delay_sec = delay / 1000

# wait for the specified delay time
time.sleep(delay_sec)

# compute the square root of the first number using the "math.sqrt()" function
result = math.sqrt(num)

# print the result
print(f"Square root of {num} after {delay} milliseconds is {result}")