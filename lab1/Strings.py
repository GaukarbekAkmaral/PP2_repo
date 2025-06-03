print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)


a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)  #True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing
b = "Hello, World!"
print(b[2:5]) #llo

b = "Hello, World!"
print(b[:5])  #Hello


b = "Hello, World!"
print(b[2:])  #llo, World!


b = "Hello, World!"
print(b[-5:-2])  #orl

a = "Hello, World!"
print(a.upper())  #HELLO, WORLD!

a = "Hello, World!"
print(a.lower())  #hello, world!

a = " Hello, World! "
print(a.strip())  #Hello, World!

a = "Hello, World!"
print(a.replace("H", "J"))  #Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

a = "Hello"
b = "World"
c = a + b
print(c)  #HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)  #Hello World

age = 36
txt = f"My name is John, I am {age}"
print(txt)  #My name is John, I am 36

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  #The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt)  #The price is 1180 dollars


txt = "We are the so-called \"Vikings\" from the north."  #We are the so-called "Vikings" from the north.

txt = "Hello\nWorld!"
print(txt)  #Hello
            #World!

txt = "Hello \bWorld!"
print(txt)  #HelloWorld!

txt = "Hello\rWorld!"
print(txt) #World!


#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#find()	Searches the string for a specified value and returns the position of where it was found
#isdigit()	Returns True if all characters in the string are digits
#isnumeric()	Returns True if all characters in the string are numeric
#split()	Splits the string at the specified separator, and returns a list
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#strip()	Returns a trimmed version of the string