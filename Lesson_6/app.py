# Data Structures
# Lists, Tuples, Sets, Dictionaries, Arrays

# List

numbers = [1, 2, 3, 4]
letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers_and_letters = [1, 2, "a", "b", 4, "z"]
list_of_tuples = [("a", "b"), ("c", "d")]
list_of_dictionaries = [{id: 2, "name": "Ade"}, {id: 3, "name": "Efe"}]
# Accessing index of Lists
# print(numbers[-1])
# print(numbers_and_letters[0:3])
# print(numbers_and_letters[2:])
# print(list_of_tuples)

# Changing values of Lists
# letters[0] = "A"
# print(letters)

# Adding into a List
# letters.append("h")
# print(letters)

# letters.pop(4)
# print(letters)

# Classwork
# upper_letter = []
# for letter in letters:
#     upper_letter.append(letter.upper())
# print(upper_letter)

# numbers_to_20 = list(range(20))
# print(numbers_to_20)

# message = "Hello World"
# print(list(message))

# zeros = [0] * 100
# print(zeros)

# letters = ["a", "b", "c", "d", "e", "f", "g", "c", "f", "c"]

# letters.insert(0, "C")
# letters.insert(5, "-")

# print(letters)

# finding index
# print(letters.index("c"))
# if "z" in letters:
#     print(letters.index("z"))
# print(letters.count("c"))

# for letter in enumerate(letters):
#     print(letter[1])

# index_of_c = []
# for letter in enumerate(letters):
#     if letter[1] == "c":
#         index_of_c.append(letter[0])
# print(index_of_c)

# Printing list in decending order
# numbers_to_50 = list(range(51))
# print(numbers_to_50[::-1])
# # Ai's solution
# print(list(range(50, 0, -1)))

# Finsing Index

# letters = ["a", "b", "c", "d", "e", "f", "g", "c", "f", "c"]

# Unpacking Lists

# first, second, *others, second_to_last, last = letters
# print(first, second)
# print(others)
# print(second_to_last)
# print(last)
