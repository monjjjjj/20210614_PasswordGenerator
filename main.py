import random
import string

# define the length of password
# length = int(input("The length of the password you need:"))
while True :
    length_input = input("The length of the password you need:")
    if not length_input.isnumeric():
        print(f"{length_input} is not a number, try again:")
        continue
    else :
        length = int(length_input)
        print(f"Password length: {length}")
    break

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

# use random
temp = random.sample(chars, length)

# create password
password = "".join(temp)

print(f"Password: {password}")
