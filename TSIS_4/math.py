#Program to convert degree to radian

import math

degree = int(input())
radian = degree * math.pi / 180

print(radian)

#Program to calculate the area of a trapezoid

height = int(input())
b1 = int(input())
b2 = int(input())

area = 0.5 * (base1 + base2) * height

print(area)

#Program to calculate the area of a regular polygon

num_sides = int(input())
side_length = int(input())

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))


print(area)

#Program to calculate the area of a parallelogram

base_length = 5
height = 6

area = base_length * height

print(area)


