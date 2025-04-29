# Classwork

# Say you have a list value like
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
