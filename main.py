import random
import string
import numpy as np

# ========================================
# define the length of password
length = ""

while True:
    length_input = input("The length of the password you need:")
    if not length_input.isnumeric():
        print(f"{length_input} is not a number, try again:")
        continue
    else:
        length = int(length_input)
    break

# ========================================
# define source of the password
# chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

A = np.array([0, 0, 0, 0])
chars2 = ""

while True:
    ans = input("Uppercase, Y/N:")
    if ans == "Y" or ans == "N":
        if ans == "Y":
            chars2 += string.ascii_uppercase
        break
    else:
        print("Please enter Y/N!")

while True:
    ans = input("Lowercase, Y/N:")
    if ans == "Y" or ans == "N":
        if ans == "Y":
            chars2 += string.ascii_lowercase
        break
    else:
        print("Please enter Y/N!")

while True:
    ans = input("Number, Y/N:")
    if ans == "Y" or ans == "N":
        if ans == "Y":
            chars2 += string.digits
        break
    else:
        print("Please enter Y/N!")

while True:
    ans = input("Symbol, Y/N:")
    if ans == "Y" or ans == "N":
        if ans == "Y":
            chars2 += string.punctuation
        break
    else:
        print("Please enter Y/N!")

if chars2 == "":
    print("You need to choose one to say yes!")
else:
    chars = "".join(chars2)
    temp = random.sample(chars, length)
    password = "".join(temp)
    print(f"Password: {password}")
