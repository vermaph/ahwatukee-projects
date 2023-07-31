# Python Indentation
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error.
# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") 



# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0



# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"



# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)




# To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Python Numbers
# The main difference between a module and a function is that a 
# Module is a collection of functions that are imported in multiple programs and can do various tasks. 
# A function is a small block of code and separates itself from the entire code and have a fixed functionality
import random

print(random.randrange(1, 10))


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# Strings are Arrays
a = "Hello, World!"
print(a[0])


# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
b.upper()
b.lower()
b.strip()
b.replace()
b.split()

 
# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


txt = "We are the so-called \"Vikings\" from the north."


# -----------------------START: Method examples
txt = " Hello, World "
txt.strip()
print(len(txt))


txt = "Hello World"
txt = txt.upper()
print(txt)


txt = "Hello World"
txt = txt.replace("H", "J")



# LIST - Below commands work only with lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "lemon")
fruits.remove("banana")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # Ascending
thislist.sort(reverse = True) # Descending
thislist.reverse()
mylist = thislist.copy()

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	  Sorts the list


# TUPLE
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


# SET - Below command only works with a SET
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

del fruits

# Dictionary - Below command only works with a Dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
car.clear()




# -----------------------END: Method examples


# Looping Using List Comprehension
# newlist = [expression for item in iterable if condition == True]

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# DICT
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)


# Nested Dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# LOOPS
# With the break statement we can stop the loop before it has looped through all the items:
# With the continue statement we can stop the current iteration of the loop, and continue with the next:


# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x=="banana":
    break


# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="banana":
    break
  print(x)


# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="banana":
    continue
  print(x)











