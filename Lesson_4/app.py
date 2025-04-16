# Assignment
# Write a Passeword protecting system with the following protection

# Assignment
# Attempted one time
# Attempted two times, One Attempt Left
# Attempted three times, Sim Locked

# correct_pass = 1234
# num_of_trials = 1

# while num_of_trials <= 3:
#     user_pass = input("Enter password- ")
#     if int(user_pass) == correct_pass:
#         print("Password Unlock Successful")
#         break
#     elif int(user_pass) != correct_pass:
#         surfix = "s" if num_of_trials > 1 else ""
#         if num_of_trials == 1:
#             print(f"Attempted one time{surfix} Try again")
#         elif num_of_trials == 2:
#             print(f"Attempted two time{surfix}, One Attempt Left")
#         else:
#             print(f"Attempted three time{surfix}, Sim Locked")
#     num_of_trials += 1

# For else Loop
# For else state is different from the normal for loop
# because it has an else statement that executes when the loop has finished
# iterating and there is no exit out of the loop

# successful = False
# for number in range(3):
#     print("Attempt", number)
#     if successful:
#         print("Successful")
#         break
# else:
#     print(f"Attempted {number+1} times and failed")

# Infinite Loop

# Infinite loops would continue to run as long as a condition is true

# while True:
#     entered_ = input(">>> ")
#     if entered_.lower() == "exit":
#         break
#     print(f"{entered_}")


# Be aware of infinte loops because they run forever so have a way
# to jump out of them and this can cause lots of problem because
# if your program consumes lots of memory, it can run out of memory and crash

# Nested Loop
# In nested loops the outer loops run first and the inner loop
# iterates out before control moves over the to the outer loop and it continues like that
# until the outer loop finish executing

# for num1 in range(1, 5):
#     for num2 in range(2):
#         print(f"({num1}, {num2})")
