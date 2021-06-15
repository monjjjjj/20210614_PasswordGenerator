import random
import string
import numpy as np

# ========================================
# define the length of password
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

ans0 = input("Uppercase, Yes or No:")
if ans0 == "Yes":
    A[0] = 1
elif ans0 == "No":
    A[0] = 0
else:
    print("Please enter Yes or No:")

ans1 = input("Lowercase, Yes or No:")
if ans1 == "Yes":
    A[1] = 1
elif ans1 == "No":
    A[1] = 0
else:
    print("Please enter Yes or No:")

ans2 = input("Number, Yes or No:")
if ans2 == "Yes":
    A[2] = 1
elif ans2 == "No":
    A[2] = 0
else:
    print("Please enter Yes or No:")

ans3 = input("Lowercase, Yes or No:")
if ans3 == "Yes":
    A[3] = 1
elif ans3 == "No":
    A[3] = 0
else:
    print("Please enter Yes or No:")

# ========================================
# use random
temp = random.sample(chars, length)

# ========================================
# create password
password = "".join(temp)

print(f"Password: {password}")
