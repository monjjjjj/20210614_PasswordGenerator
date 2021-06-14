import random
import string

length = int(input("The length of the password you need:"))
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

# use random
temp = random.sample(chars, length)

# create password
password = "".join(temp)

print(password)
