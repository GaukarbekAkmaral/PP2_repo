x = str("Hello World")	
x = int(20)	
x = float(20.5)	
x = complex(1j)	
x = list(("apple", "banana", "cherry"))	     x = ["apple", "banana", "cherry"]
x = tuple(("apple", "banana", "cherry"))     x = ("apple", "banana", "cherry")
x = range(6)
x = dict(name="John", age=36)	             x = {"name" : "John", "age" : 36}
x = set(("apple", "banana", "cherry"))       x = {"apple", "banana", "cherry"}
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)	
x = memoryview(bytes(5))


x = 1
y = 35656222554887711
z = -3255522

x = 1.10
y = 1.0
z = -35.59

x = 35e3
y = 12E4
z = -87.7e100

x = 3+5j
y = 5j
z = -5j

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'