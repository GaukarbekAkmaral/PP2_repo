thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list

#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)   #['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #return banana


thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #return cherry


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #return ['cherry', 'orange', 'kiwi']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #return ['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #return ['cherry', 'orange', 'kiwi', 'melon', 'mango']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #return ['orange', 'kiwi', 'melon']

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  #['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)   #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)   #['apple', 'blackcurrant', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)   #['apple', 'watermelon']

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   #['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)   #['apple', 'orange', 'banana', 'cherry']

#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)   #['apple', 'banana', 'cherry', 'orange']

#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)   #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)   #['apple', 'banana', 'cherry', 'kiwi', 'orange']

#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  #['apple', 'cherry']

#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  #['apple', 'cherry']

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  #['apple', 'banana']

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  #['banana', 'cherry']

#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist  #error

#The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   #[]

#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)  #apple
#           banana
#           cherry


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]




sum=0
list = [1,2,3,4,5]
for i in list:
    sum+=i
print(sum)
print(max(list))
print(min(list))


list1 = ['apple', 'plane','finall','plese']
list1[1]="updated"
print(list1)