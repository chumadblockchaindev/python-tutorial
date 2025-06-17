# Basic Syntax and Control Flow in Python

# age_from_input = int(input("Enter your age: "))

# if age_from_input < 18:
#     print("You're not allowed to vote.")
# else:
#     print("You can vote!")

# Password Check Example

# correct_password = "password123"

# user_input_password = input("Enter your password: ")
# print(user_input_password == correct_password)/

# if user_input_password == correct_password:
#     print("Access granted.")
# else:
#     print("Access denied. Incorrect password.")


# Simple Calculator Example using if-elif-else

# num_one = float(input("Enter the first number: "))
# num_two = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")

# if operation == "+":
#     result = num_one + num_two
# elif operation == "-":
#     result = num_one - num_two
# elif operation == "*":
#     result = num_one * num_two
# elif operation == "/":
#     result = num_one / num_two
# else:
#     result = None
#     message = f"Invalid operation: {operation}"

# print(message) if result is None else print(
#     f"The result of {num_one} {operation} {num_two} is {round(result, 1)}")

# For and While Loops in Python

# Sequence example
numbers = range(5)  # 0, 1, 2, 3, 4
message = "Hello World!"

# print(len(numbers))  # Length of the sequence
# print(len(message))  # Length of the string

# print(numbers[0])
# print(message[0])

# print(5 in numbers)
# print("world" in message)

# For Loop Example
# for variable in sequence:
# Do something with the variable

for number in numbers:
    print(f"Number: {number}")

for char in message:
    print(f"Character: {char}")

# A for loop is used to iterrate over a sequence (like a list, tuple, or string).

# Assignment

# Study while Loop and Give me Examples while loop and infinite loop
