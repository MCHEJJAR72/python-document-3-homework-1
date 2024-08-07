Data Collections 2 (Dictionaries, Sets) and Importing Modules
Tasks Today:
Dictionary
     a) Declaring (key, value)
     b) Accessing Values
     ------ Exercise #1 - Print the eye color of each person in a double nested dict
     c) Adding New Pairs
     d) Modifying Values
     e) Removing Key, Value Pairs
     f) Looping a Dictionary
     g) Looping Only Keys
     h) Looping Only Values
     ------ Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format()
     i) sorted()
     j) Lists with Dictionaries
     k) Dictionaries with Lists
     l) Dictionaries with Dictionaries
     ------ Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, which prints all names and addresses after they're done putting information in...
Dictionaries vs. Lists (over time)
Set
     a) Declaring
     b) .add()
     c) .remove()
     d) .union()
     e) .intersection()
     f) .difference()
     g) Frozen Set
Modules
     a) Importing Entire Modules
     b) Importing Methods Only
     c) Using the 'as' Keyword
     d) Creating a Module
Exercises
     a) Build a Shopping Cart
     b) Create Your Own Module
Dictionary
A collection of data with 'key:value' pairs. Dictionaries are ordered as of Python 3.6

Declaring (key, value)
dict_1 = {}
dict_2 = dict()

dict_3 = {
    'dave': '255 Main Street',
    'sean': '522 1st Steet',
    0: 'This is a value for the key of 0'
}

print(dict_3)
{'dave': '255 Main Street', 'sean': '522 1st Steet', 0: 'This is a value for the key of 0'}
dict_3["dave"]
dict_3[0]
'This is a value for the key of 0'
In-Class Exercise #1 - Print a formatted statement from the dictionary below
The output should be '2018 Chevrolet Silverado'

# use the dict below
truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}

print("{} {} {}".format(truck['year'], truck['make'], truck['model']))
2018 Chevrolet Silverado
Adding New Pairs
dict_3['bob'] = 'Nashville'

dict_3
{'dave': '255 Main Street',
 'sean': '522 1st Steet',
 0: 'This is a value for the key of 0',
 'bob': 'Nashville'}
Modifying Values
dict_3['bob'] = 'From Ohio'

dict_3
{'dave': '255 Main Street',
 'sean': '522 1st Steet',
 0: 'This is a value for the key of 0',
 'bob': 'From Ohio'}
Removing Key, Value Pairs
del dict_3['bob']

dict_3
{'dave': '255 Main Street',
 'sean': '522 1st Steet',
 0: 'This is a value for the key of 0'}
Looping a Dictionary
# .items()
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

for key, value in dict_3.items():
    print(key, value)
dave 255 Main Street
sean 522 1st Steet
0 This is a value for the key of 0
Looping Only Keys
# .keys()

for key in dict_3.keys():
    print(key)
dave
sean
0
Looping Only Values
# .values()

for value in dict_3.values():
    print(value)
In-Class Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format()
Output should be:
Max has blue eyes
Lilly has brown eyes
Barney has blue eyes
etc.

# use the dict below

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}

for key, value in people.items():
    print(key, "has", value, "eyes")
Max has blue eyes
Lilly has brown eyes
Barney has blue eyes
Larney has brown eyes
Ted has purple eyes
sorted()
# sorts variables in order
# sorted(dict.values()) or dict.keys() or dict.items()

print(sorted(people.items()))
print(sorted(people.keys()))
print(sorted(people.values()))
[('Barney', 'blue'), ('Larney', 'brown'), ('Lilly', 'brown'), ('Max', 'blue'), ('Ted', 'purple')]
['Barney', 'Larney', 'Lilly', 'Max', 'Ted']
['blue', 'blue', 'brown', 'brown', 'purple']
List with Dictionaries
names = ['Dave', 'Randy', 'Greg', {'random_guy':'Robert', 'random_girl': 'Barbara'}]

print(names[3]['random_girl'])

for keys in names[3].keys():
    print(keys)
Barbara
random_guy
random_girl
Dictionaries with Lists
# be careful when using numbers as keys in dictionaries, don't confuse them with indexes

random_data = {
    'lsit1': [54, 7, 11],
    '2': ['smith', 'iPod', 'water bottle'],
}

for key in random_data['2']:
    print(key)
smith
iPod
water bottle
Dictionaries with Dictionaries
# to get values, must traverse through keys
food_dict = {
    'ice_cream': {
        'CHO': 2.99,
        'VA': 3.99,
        'Oreo': 5.99,
        'PB': 6.99
    }
}

print(food_dict['ice_cream']['VA'])

for i in food_dict['ice_cream'].items():
    print(i)
3.99
('CHO', 2.99)
('VA', 3.99)
('Oreo', 5.99)
('PB', 6.99)
Dictionaries vs. Lists (over time) Example of RUNTIME
When inputting values in a Dictionary vs List
import time


# generate fake dictionary
d = {}

for i in range(10000000):
    d[i] = 'value'
    

# generate fake list
big_list = [x for x in range(10000000)]
# tracking time for dictionary
start_time = time.time()

print(d[9999999])

end_time = time.time() - start_time

print('Elapsed time for dictionary: {}'.format(end_time))


# tracking time for list
start_time = time.time()

for i in range(len(big_list)):
    if i == 9999999:
        print(i)

end_time = time.time() - start_time

print('Elapsed time for list: {}'.format(end_time))
value
Elapsed time for dictionary: 0.00099945068359375
9999999
Elapsed time for list: 0.8183341026306152
Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, and continues to do so until they choose to 'quit'. Once they quit, the program should print all names and addresses.
Proper steps:
step 1: write a function that takes in information and stores it in a dictionary
step 2: define an empty dictionary to work with
step 3: create our loop, which asks the user for information until they quit
step 4: ask for the information, and store it into variables
step 5: check if the user types quit
step 5a: print out all information
step 5b: break out of the loop
step 6: if they didn't quit, add the information to the dictionary
step 7: invoke the function by calling it

from IPython.display import clear_output


def SignUp():
    info = {}
    name = ""
    address = ""
    if name or address == "Quit":
        return
    else:
        name = input("Name? (type 'Quit' to exit) ")
        if name or address != "Quit":
            address = input("Address? (type 'Quit' to exit) ")
        else: return
    info[name] = address
    for name, address in info.items():
        print(name, address)        
        
        
SignUp()
Quit Quit
Set
A Set is an unordered collection data type that is iterable (loop), mutable, and has no duplicate elements.
Major advantage is that it is highly optimized in checking if something is in the set, as opposed to checking if something is in a list.

Declaring
# set() or {}
# no order {3, 2, 1} outputs as {1, 2, 3}

nums = {4, 1, 6, 4}

print(nums)
{1, 4, 6}
.add()
# set.add()

nums.add(56)

print(nums)
{56, 1, 4, 6}
.remove()
# removes by value
# set.remove()
# nums.remove(56)

nums.remove(56)

print(nums)
{1, 4, 6}
.union()
# Returns a union of two sets, can also use '|' or set.union(set)
# joins all numbers, gets rid of duplicates

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s3 = s1.union(s2)

print(s3)

s4 = s1 | s2
print(s4)
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
.intersection()
# Returns an intersection of two sets, can also use '&'
# only takes similar elements from both sets

s5 = s2 & s1
s6 = s1.intersection(s2)

print(s5)
print(s6)
{3, 4}
{3, 4}
.difference()
# Returns a set containing all the elements of invoking set that are not in the second set, can also use '-'
# only takes values from the first set that are not in the second set
# order matters

s7 = s2 - s1
s8 = s1.difference(s2)

print(s7)
print(s8)
.clear()
# Empties the whole set
# set.clear()
s8 = s1.difference(s2)
s8.clear()
print(s8)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[3], line 3
      1 # Empties the whole set
      2 # set.clear()
----> 3 s8 = s1.difference(s2)
      4 s8.clear()
      5 print(s8)

NameError: name 's1' is not defined
Frozenset
Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.


Unique & Immutable
# frozenset([])
my_frozen_set = frozenset(s3)
print(my_frozen_set)

# my_frozen_set.add(s6)
# wont work
frozenset({1, 2, 3, 4, 5, 6})
Modules
Importing Entire Modules
# import or from 'xxx' import *
# import math

from math import pi
from math import floor
#easier way below

from math import pi, floor

import math
#could be too big

print(pi)
3.141592653589793
3
Importing Methods Only
# from 'xxx' import 'xxx'
# from math import floor

from math import pi
from math import floor
#easier way below

from math import pi, floor

print(floor(pi))
3
Using the 'as' Keyword
# from 'xxx' import 'xxx' as 'xxx' or import 'xxx' as 'xxx'
# from math import floor as f

from math import pi as p, floor as f

print(f(p))
3
Creating a Module
import module

print(module.printName(Obama))
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[38], line 1
----> 1 import module
      3 print(module.printName(Obama))

ModuleNotFoundError: No module named 'module'
Exercises
1) Build a Shopping Cart
You can use either lists or dictionaries. The program should have the following capabilities:

1) Takes in input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, print out all items in the user's list
from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def MakeShoppingList():
    ShoppingList = ["Eggs", "Milk", "Bacon", "Chips"]
    WhatDo = input("Would you like to 'Show', 'Add' to, or 'Delete' and item from the list? (type 'quit' to quit)" )
    while WhatDo != 'quit':
        if WhatDo == "Show":
            return ", ".join(ShoppingList)
        elif WhatDo == "Add":
            AddSL = input("What would you like to add? (type 'quit' to quit) ")
            ShoppingList.append(AddSL)
            if AddSL == "quit":
                ShoppingList.pop()
                print(ShoppingList)
                break
            else:
                continue
        elif WhatDo == "Delete":
            DelSL = input("What would you like to delete? ")
            if DelSL == "quit":
                return ", ".join(ShoppingList)
                break
            else:
                ShoppingList.remove(DelSL)
                continue
        else:
            print("Please type 'Show', 'Add', or 'Delete")
            break
MakeShoppingList()
'Eggs, Milk, Bacon, Chips'
2) Create a Module in VS Code and Import It into jupyter notebook
Module should have the following capabilities:

1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area

2) Has a function to calculate the circumference of a circle

Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage
from math import pi

def Circumference():
    radius = input("What is the radius of the circle? ")
    return 2 * pi * int(radius)

def SquareFoot():
    length = input("What is the length of the house? ")
    width = input("What is the width of the house? ")
    return int(length) * int(width)

# SquareFoot()
Circumference()