# Classwork

# Say you have a list value like
from pprint import pprint
fruits = ['apples', 'bananas', 'oranges', 'mangoes', 'garri', "rice", 'beans']

# Write a function that takes this list and returns a string with all the letters seperated
# by a comma and a space with "and" inserted before the last item.
# For Examples the above should return "apples, bananas, oranges, and mangoes"

# Solution
# sentence = [str(item) for item in items]
# return ", ".join(sentence)

# new_list = []


# def getString(items):
#     for item in items:
#         new_list.append(f"{item} ,")

#     new_list.insert(len(items) - 1, "and")
#     return " ".join(new_list)


# print(getString(fruits))


# Tuples

# names = ("ade", "bisi")
# numbers = list(range(10))
# [expression for item in items]
# new_numbers = [number for number in numbers if number > 5]
# print(tuple(new_numbers))


# Assignment
# Write a function that adds list(range(20))

# Arrange in Aphabetical order

# products = [('beans', 100), ('garri', 150), ('rice', 50), ('turkey', 200)]


# def get_prices(product):
#     return product[0]


# products.sort(key=get_prices)
# print(products)

# Dictionaries

# people = {'efe': 20, 'emmanel': 25, 'precious': 26, 'cliford': 19}
# print(people['precious'])
# print(people['cliford'])

# Creating a dictionary
# print(dict(one=1, two=2, three=3))

# Adding into a dictionary
# There are two ways to add into a dictionary
# 1. Assignment
# 2. Empting a dictoinary to another

# numbers = {1: 'one', 2: 'two', 3: 'three'}
# numbers[4] = 'four'

# people_and_numbers = {**numbers, **people, "exta": 45}
# print(people_and_numbers)

# first = {'a': 2, 'b': 3}
# second = {'c': 4, 'd': 5}

# combined = {**first, **second, 'e': 6}

# combined['f'] = 7

# del combined['a']

# print(combined)


# students = {'efe': 20, 'emmanel': 25, 'precious': 26, 'cliford': 19}

# while True:
#     print("Enter student's name you want to fetch the age and enter 'Q' to quit")
#     name = input("")

#     if name.upper() == "Q":
#         break

#     if name.lower() in students:
#         print(f"{name} is {students[name.lower()]} years old")
#     else:
#         print(f"{name} does not exist in the database")
#         print(f"What is their birthday? ")
#         birthday = input("")
#         students[name] = birthday  # add into the dictionary
#         print("Birthday Database updated")


# Keys(), Values(), items() method in dictionary

# print(people.keys())
# print(people.values())
# print(people.items())

# for name in people.keys():
#     print(name)

# for age in people.values():
#     print(age)

# for items in people.items():
#     print(items)

# names = people.keys()
# print(list(names))

# age = people.values()
# print(list(age))

# items = people.items()
# print(items)

# Classwork

# people = {'efe': 20, 'emmanel': 25, 'precious': 26, 'cliford': 19}
# print("Unsorted names of students")
# print(people, "\n")

# people_list = list(people.items())
# print(people_list)


# def getAge(x):
#     return x[1]


# people_list.sort(key=getAge, reverse=True)
# print(people_list)

# print("The sorted dictionary of students")
# print(dict(people_list))

# Checking if keys is in dictionary

# people = {'efe': 20, 'emmanuel': 25, 'precious': 26, 'cliford': 19}

# if 'emmanuell' in people:
#     print(people['emmanuellll'])

# print('fred' in people)
# print('fred' in people.keys())
# print(26 in people.values())


# The get() method in dictionary

items = {'eggs': 20, 'fish': 15, 'rice': 2, 'milk': 12}

# if 'chicken' in items:
#     print(items['chicken'])
# else:
#     print("does not exist")

# print(items.get("chicken", "Does not exist"))
# print(items.get("fishh", 0))


# # The setdefault() method in Dictionary
items = {'eggs': 20, 'fish': 15, 'rice': 2, 'milk': 12}


# def checkandadd(key, value):
#     if key not in items:
#         items[key] = value

# checkandadd('beans', 50)
# print(items)

# items.setdefault('beans', 50)
# print(items)

# Classwork
sentence = "The King of the world is Jesus and he is the creator of the universe"
# In the sentence above get the most number of letter occurent

count = {}

for char in sentence:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1
del count[' ']
pprint(count, width=1)

# def getvalue(item):
#     return item[1]


# countitems = list(count.items())
# countitems.sort(key=getvalue, reverse=True)

# print(
#     f"The most number of caracter that exist is {"".join(str(countitems[0]))}")
