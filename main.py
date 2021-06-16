import random
import string


def get_length():
    while True:
        length_input = input("The length of the password you need:")
        if not length_input.isnumeric():
            print(f"{length_input} is not a number, try again:")
        else:
            return int(length_input)


def check_source(source_name):
    while True:
        ans = input("%s, Y/N:" % source_name)
        if ans == "Y":
            return True
        elif ans == "N":
            return False
        else:
            print("Please enter Y/N!")


# define the length of password
length = get_length()

# define source of the password
chars2 = ""

# 三元判斷式
chars2 += string.ascii_uppercase if check_source("Uppercase") else ''
chars2 += string.ascii_lowercase if check_source("Lowercase") else ''
chars2 += string.digits if check_source("Number") else ''
chars2 += string.punctuation if check_source("Symbol") else ''

if chars2 == "":
    print("You need to choose one to say yes!")
else:
    temp = ''.join(random.choice(chars2) for _ in range(length))
    password = "".join(temp)
    print(f"Password: {password}")