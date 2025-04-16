correct_pass = 1234
num_of_trials = 1

while num_of_trials <= 3:
    user_pass = input("Enter password- ")
    if int(user_pass) == correct_pass:
        print("Password Unlock Successful")
        break
    elif int(user_pass) != correct_pass:
        surfix = "s" if num_of_trials > 1 else ""
        if num_of_trials == 1:
            print(f"Attempted one time{surfix} Try again")
        elif num_of_trials == 2:
            print(f"Attempted two time{surfix}, One Attempt Left")
        else:
            print(f"Attempted three time{surfix}, Sim Locked")
    num_of_trials += 1
