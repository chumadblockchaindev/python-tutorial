# Basic Syntax and Control Flow in Python

# age_from_input = int(input("Enter your age: "))

# if age_from_input < 18:
#     print("You're not allpowed to vote.")
# else:
#     print("You can vote!")

# Password Check Example

# correct_password = "password123"

# user_input_password = input("Enter your password: ")

# if user_input_password == correct_password:
#     print("Access granted.")
# else:
#     print("Access denied. Incorrect password.")


# Simple Calculator Example using if-elif-else

num_one = float(input("Enter the first number: "))
num_two = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num_one + num_two
elif operation == "-":
    result = num_one - num_two
elif operation == "*":
    result = num_one * num_two
elif operation == "/":
    result = num_one / num_two

print(f"The result of {num_one} {operation} {num_two} is {round(result, 1)}")
