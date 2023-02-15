#generate the squares of numbers up to some number input n
n = int(input())
i = 0 
for i in range(n):
    print(i*i)
#2nd form 
print(*[x**2 for x in range(1,int(input()))])


#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i # yield is keyword to generate the current value of i as an output of the generator function.

n = int(input("Enter a number: "))
even_nums = even_numbers(n)

print(",".join(str(num) for num in even_nums))

#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by_3_and_4(n):
    for i in range(0,n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
number = int(input())
print(divisible_by_3_and_4(number))

#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares():
    a = int(input())
    b = int(input())
    for i in range(a, b+1):
        yield i*i
        
#Implement a generator that returns all numbers from (n) down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
num = int(input())
for i in countdown(num):
    print(i)
    