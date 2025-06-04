#i=2
#while i <= 20:
#    print(i)
#    i+=2


#x = 1
#sum=0
#while x <= 50:
#    if x % 3==0:
#        sum+=x
#    x+=1
#print(sum)

a = input()
while a != "admin123":
    print("Write password")
    a=input()

#With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#With the break statement we can stop the loop even if the while condition is true

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#With the continue statement we can stop the current iteration, and continue with the next

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#With the else statement we can run a block of code once when the condition no longer is true