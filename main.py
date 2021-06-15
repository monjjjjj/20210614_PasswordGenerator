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
    ans0 = input("Uppercase, Y/N:")
    if ans0 == "Y":
       chars2 += string.ascii_uppercase
       break
    elif ans0 == "N":
       chars2 = chars2
       break
    else:
        print("Please enter Y/N!")
    continue


while True:
    ans1 = input("Lowercase, Y/N:")
    if ans1 == "Y":
       chars2 += string.ascii_lowercase
       break
    elif ans1 == "N":
       chars2 = chars2
       break
    else:
        print("Please enter Y/N!")
    continue

while True:
    ans2 = input("Number, Y/N:")
    if ans2 == "Y":
       chars2 += string.digits
       break
    elif ans2 == "N":
       chars2 = chars2
       break
    else:
        print("Please enter Y/N!")
    continue

while True:
    ans3 = input("Symbol, Y/N:")
    if ans3 == "Y":
       chars2 += string.punctuation
       break
    elif ans3 == "N":
       chars2 = chars2
       break
    else:
        print("Please enter Y/N!")
    continue

if chars2 == "":
    print("You need to choose one to say yes!")
else:
    chars1 = "".join(chars2)
    temp = random.sample(chars1, length)
    password = "".join(temp)
    print(f"Password: {password}")



