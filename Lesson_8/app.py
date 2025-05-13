# Manipulating Strings

message = "Welcom to Coriftech Solutions"

# print(message[:3])
# print(message[-1])
# print(message[3:])

# print("Home" in message)
# print("Welcome" not in message)

# Methods in strings

# uppper(), lower(), isupper(), islower()

# message.upper()
# message.lower()

# print(message.islower())

# phone = "12234a"

# print(phone.isdecimal())
# print(phone.isalnum())

# print(message.istitle())
# print(message.isspace())

# Printing Strings

# print("Ade's mother is a nurse and she told me 'say yes' ")
# print('Ade\'s mother is a nurse and she told me "say yes"')

# print('\n')
# print('\t' + "oven")

# join(), split(),replace(), prefix(), surfix()
# startswith(), endswith()

name = "Mr, Chukwuma, works at, coriftech" \
    "and he's a, good tutor"

# print(name.startswith("Mr"))
# print(name.endswith("tutor"))


new_name = ", ".join(['Ade', "goes", "to", "school"])
# print(new_name)

# print(" ".join(['Ade', "goes", "to", "school"]))

# print(name.join(['Ade', "goes", "to", "school"]))

# split()

sentence = "Ade is a good \n boy and he helps \n he's mom out \n in the kitchen"

# print(sentence.split())
# print(sentence.split("o"))
# print(sentence.split("\n"))

# rjust(), ljust(), center()

# greeting = "hello"

# print(greeting.rjust(20, "*"))
# print(greeting.ljust(20, "."))
# print(greeting.center(20, "-"))


# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# Assignment
# Arrange the phone numbers in the file nameed phonenumbers in one column and put it in a new file

# Methods for removing whitespaces strip(), rstrip(), lstrip()

message = '     Hello World     '
message1 = """      gddgsdg
        ffsgfdg
fbf         dfsgdfghdsh
        sdfg
        gdgd
    fsgdg"""
# print(message.lstrip())
# print(message.rstrip())
# print(message.strip())

message_list = []


def arrangemsg(message1):
    for message in message1.split("\n"):
        message_list.append(message.strip())
    return " ".join(message_list)


print(arrangemsg(message1))
