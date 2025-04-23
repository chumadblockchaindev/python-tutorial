# Data Structures
# Lists, Tuples, Sets, Dictionaries, Arrays

# List

numbers = [1, 2, 3, 4]
# letters = ["a", "b", "c", "d", "e", "f", "g"]
numbers_and_letters = [1, 2, "a", "b", 4, "z"]
list_of_tuples = [("a", "b"), ("c", "d")]
list_of_dictionaries = [{id: 2, "name": "Ade"}, {id: 3, "name": "Efe"}]
matrix = [[2, 3], [4, 5]]
message = list("Hello World")
zeros = [0] * 5

# Accessing index of Lists
# print(numbers[0:3])
# print(numbers_and_letters[0:3])
# print(numbers_and_letters[2:])
# print(list_of_tuples)

# Changing values of Lists
# letters[0] = "A"
# print(letters)

# Adding into a List
# letters.append("h")
# print(letters)

# Removing from list
# letters.pop(4)
# print(letters)

# del letters[0:3]

# print(letters)

# letters.clear()
# print(letters)

# Classwork
# upper_letter = []
# for letter in letters:
#     upper_letter.append(letter.upper())
# print(upper_letter)

# Addition of lists
# print(numbers + letters)


# letters = ["a", "b", "c", "d", "e", "f", "g", "c", "f", "c"]

# letters.insert(0, "C")
# letters.insert(5, "-")

# print(letters)

# finding index

# print(letters.index("c"))

# if "x" in letters:
#     print(letters.index("x"))

# counting the occurance of a letter in a list
# print(letters.count("c"))

# letters = ["a", "b", "c", "d", "e", "f", "g", "c", "f", "c"]

# for letter in enumerate(letters):
#     print(letter)

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

# letters = ["a", "b", "c", "d", "e", "f", "g", "c", "f", "c"]

# Unpacking Lists

# first, second, *others, second_to_last, last = letters
# print(first, second)
# print(others)
# print(second_to_last)
# print(last)

# Seperate "Photo and Synthesis from the word "Photosynthesis
# word = "Photosynthesis"
# photo = word[:5]
# syn = word[5:]
# print(photo)
# print(syn)

# Arrange the numbers below in accending order
# numbers = [23, 24, 4, 55, 67, 88, 9, 43, 2, 2, 1, 1, 90, 77]
# print(numbers[::-1])
# print(sorted(numbers, reverse=True))
# numbers.sort()
# print(numbers)

# Seperate "efe" from the word
# numbers_and_letters = ["a", "b", "efe", "z"]

# for value in enumerate(numbers_and_letters):
#     if value[1] == "efe":
#         numbers_and_letters.pop(value[0])


# print(numbers_and_letters)
