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

def greet(name):
    print("Good Morning", name)


greet("Elijah")
greet("Solomon")

# Passing default arguments
# Default arguments allow a function to be called with fewer arguments than it is defined to accept.


def add_numbers(num1, num2=5):
    return num1 + num2


print(add_numbers(5, 3))  # Output: 15

# A function can also return a value, which can be used later in the code.


def greet(name):
    return f"Good Morning {name}"


print(greet("Elijah"))
print(greet("Solomon"))

with open("greetings.txt", "w") as file:
    file.write(greet("Elijah") + "\n")
    file.write(greet("Solomon") + "\n")

# *args and **kwargs


def add_numbers(*args):
    print(args)  # This will prrint the tuple of arguments passed
    total = 0
    for num in args:
        total += num

    return total


print(add_numbers(1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8))


# **kwargs

def student_data(**kwargs):
    print(kwargs)


student_data(name="Valeri", age=21,
             department="Computer Science", state="Delta")
