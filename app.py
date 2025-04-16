# Functions in programming are reusable blocks of code
# designed to perform a specific task.

# def user(first_name, school="Coriftech"):
#     return f"Welcome {first_name}, A student of {school}\n"


# print("successful")

# print(user("Efe", ))
# print(user("Precious", "Cambrige"))
# print(user("Promise", ))
# print(user("Emmanuel", school="Harvard"))


# file = open("users.txt", "w")
# file.write(user("Efe"))
# file.write(user("Chukwuma", "Manchester"))
# file.write(user("Emmanuel", "Havard"))
# file.write(user("Precious", "Cambrige"))


# Default Argument
# def multiply(number, by=2):
#     return number * by


# print(multiply(5, 4))
# print(multiply(5, 5))
# print(multiply(5))

# Keyword Argument
# print(multiply(number=5))
# print(multiply(10, by=3))
# print(multiply(20))


#  xargs
# def multiply(*letters):
#     total = ""
#     for letter in letters:
#         total = f"{letter}"
#     return total


# print(multiply("Hello", "World"))

# xxargs


# def user(**users_details):
#     return users_details


# print(user(id=1, name="Efe", salary="$5000"))
