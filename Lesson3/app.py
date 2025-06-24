# Functions
# A function is a reusable block of code

# Syntax of a function
# def name_of_function (optional_variable):
#   # Do something

# In programming, parameters and arguments are related but distinct concepts:

# Parameters
# Parameters are the variables listed in a function's definition.

# They act as placeholders for the values that will be passed to the function.

# Defined when the function is created.

# Arguments
# Arguments are the actual values passed to the function when it is called.

# They are the real data that replace the parameters during execution.

# def greet(name):
#     print("Good Morning", name)


# greet("Elijah")
# greet("Solomon")

# Passing default arguments
# Default arguments allow a function to be called with fewer arguments than it is defined to accept.


# def add_numbers(num1, num2=5):
#     return num1 + num2


# print(add_numbers(5, 3))  # Output: 15

# A function can also return a value, which can be used later in the code.


# def greet(name):
#     return f"Good Morning {name}"


# print(greet("Elijah"))
# print(greet("Solomon"))

# with open("greetings.txt", "w") as file:
#     file.write(greet("Elijah") + "\n")
#     file.write(greet("Solomon") + "\n")

# *args and **kwargs


# def add_numbers(*args):
#     print(args)  # This will prrint the tuple of arguments passed
#     total = 0
#     for num in args:
#         total += num

#     return total


# print(add_numbers(1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8))


# **kwargs

# def student_data(**kwargs):
#     print(kwargs)


# student_data(name="Valeri", age=21,
#              department="Computer Science", state="Delta")

# Assignment Solution

# initial_deposit = 100000

# def calculate_payment_with_month(time_in_months=24, daily_installment=3000):
#     return (daily_installment * 30 * time_in_months) + initial_deposit


# print("Total payment will be", calculate_payment_with_month())

# CLASS WORK
# Write a function for a loan app that takes in two parameters, the time the person is
# going to pay up in months, and the total amount of loan he took, to return the amount he should pay daily

def apply_interest_with_rate(rate):
    def apply_interest(func):
        def wrapper(*args, **kwargs):
            interest = (rate * kwargs["loan_amount"]
                        * kwargs["time_in_months"]) / 100
            print(interest)
            if kwargs["time_in_months"] > 3:
                message = f"Total Loan amount payable + Interest {func(*args, **kwargs) + interest}"
            else:
                message = "Payment time should be greater than three months"

            return message
        return wrapper
    return apply_interest


loan_amount = int(input("Enter loan amount: "))
time_in_months = int(input("Enter payment time in months: "))


@apply_interest_with_rate(rate=0.002)
def calculate_daily_payment(time_in_months=36, loan_amount=3000000):
    """This function calculates the daily payment for a loan app"""
    total_days = time_in_months * 30 * 1
    daily_payment = loan_amount / total_days
    print(daily_payment)
    return round(daily_payment, 2)


print(calculate_daily_payment(
    time_in_months=time_in_months, loan_amount=loan_amount))


# 1.
# What if we want to add an interest for the payment of our loans so that
# the longer the payup time the higher the interest


# Decorators in Python
# from functools import wraps


# def smartdiv(func):
#     @wraps(func)
#     def wrapper(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return wrapper


# @smartdiv
# def divide(a, b):
#     return a/b


# print(divide(2, 10))
# print(divide.__name__)


# A decorator is just a function that adds extra features
# to another function — without changing its actual code.

# Why Use a Decorator?
# To reuse code (e.g., logging, timing, authentication).

# To modify behavior of functions easily.

# To make your code clean and readable.

# Decorators without paramethers

# from functools import wraps


# def check_login_type(login_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):  # 1
#             # print(f"Before {func.__name__} runs")
#             if login_type == "login":
#                 print(f"{func(*args, **kwargs)}, Welcome back")  # 2
#             elif login_type == "signup":
#                 print(f"{func(*args, **kwargs)}, Welcome to our platfom")  # 2
#             # print(f"After the {func.__name__} runs") # 3
#         return wrapper
#     return decorator


# @check_login_type(login_type="login")
# def greet(name):  # 2
#     return f"Hello! {name}"


# greet("Elijah")
# print(greet.__name__)

# modify = modify_hello(say_hello)
# modify()


# def log_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @log_calls
# def add(a, b):
#     return a + b

# add(3, 5)
# # Output:
# # Calling add with args: (3, 5), kwargs: {}
# # add returned 8

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Alice")
# # Output:
# # Hello Alice
# # Hello Alice
# # Hello Alice


# def singleton(cls):
#     instances = {}
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return wrapper

# @singleton
# class Database:
#     def __init__(self):
#         print("Database created")

# d1 = Database()
# d2 = Database()
# print(d1 is d2)  # True
