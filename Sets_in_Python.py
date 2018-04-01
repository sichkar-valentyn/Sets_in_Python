# File: Sets_in_Python.py
# Description: Creating and using Sets in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Creating and using Sets in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Sets_in_Python (date of access: XX.XX.XXXX)


# Creating an empty set
s = set()

# Method to add element in the set
s.add('laptop')
print(s)
print()

# Method to remove element from the set
s.remove('laptop')  # If there is no such element in the set it will show mistake
print(s)
print()

# Method to remove element from the set without mistake even if there is no such element
s.discard('laptop')
print(s)
print()

# Method to clear the set
s.clear()
print(s)

# Function to get the number of elements in the set
print(len(s))
print()

# Creating filled set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# Showing the set. Pay attention that repeated values in the set are not shown
print(basket)  # {'banana', 'apple', 'orange', 'pear'} And they can be in any order
print()

# Asking if something is inside set
print('orange' in basket)  # True
print('python' in basket)  # False
print()

# Using loops for the sets. Pay attention that repeated elements in the set are not shown
for x in basket:
    print(x)
print()

# Implementing the task
# Imput string with elements divided by gaps
# Output theelements and the number they are found in the string
# Algorithm isn't sensitive to upper or lowcase letters
string = input().lower().split()  # Creating the string with low case latters
s = set(string)  # Creating the set with elements from the string but it will not add repeated elements
for x in s:
    print(x, string.count(x))

