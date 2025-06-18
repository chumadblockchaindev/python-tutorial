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

# for number in numbers:
#     print(f"Number: {number}")

# for char in message:
#     print(f"Character: {char}")


# message = "Python Programming"

# for char in message:
#     if char == "P":
#         print(char)

# numbers = range(1, 21)

# for number in numbers:
#     if number % 2 == 0:
#         print(f"Even number: {number}")


# numbers = range(1, 21, 2)

# for number in numbers:
#     print(number+1)

# A for loop is used to iterrate over a sequence (like a list, tuple, or string).

# Assignment

# Study while Loop and Give me Examples while loop and infinite loop

# While Loop Example

# while condition:
#     # Do something

# count = 0

# while count < 10:
#     print(f"Count is: {count}")
#     count += 1


# Infinite Loop Example

while True:
    user_input = input("Type 'exit' to stop the loop: ")
    if user_input.lower() == "exit":
        print("Exiting the loop.")
        break
    else:
        print(f"You typed: {user_input}")
