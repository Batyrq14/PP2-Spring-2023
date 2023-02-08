#While loop
i = 0
while i < 6:
    i += 1
    if i==4:
        continue
    print(i)
else:
  print("i is no longer less than 6")
  #
  
  cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars[0])

x = len(cars)

for i in cars:
  print(i)

cars.append("Honda")
print(cars)

cars.pop(0)

cars.remove("Volvo")
print(cars)

#dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(type(thisdict))

print(thisdict["brand"])

# As of Python version 3.7, dictionaries are ordered
# dictionaries are changeable, ordered, and does not allow duplicates.

print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#forloop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
else:
    print("Finished.")

for i in range(2, 30, 3):
    print(i)

for x in [0, 1, 2]:
  pass

#list

thislist = ["apple", "banana", False, 25,  "apple", "cherry"]
print(thislist)

print(len(thislist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Set

# Set items are unchangeable, but you can remove items and add new items.
# Set items are unordered, unchangeable, and do not allow duplicate values.

set1 = {"abc", 34, True, 40, "male"}
print(set1)
print(type(set1))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#tuple

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# elements of tuple are unchangeable

print(len(thistuple))

#comma is required to create single element tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", False, 33)) # note the double round-brackets
print(thistuple)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# elements of tuple are unchangeable

print(len(thistuple))

#comma is required to create single element tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", False, 33)) # note the double round-brackets
print(thistuple)
print(type(thistuple))
