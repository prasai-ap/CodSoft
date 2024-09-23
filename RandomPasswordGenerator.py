import string
import random
characters=string.ascii_letters + string.digits + string.punctuation
length=int(input("Enter a length of password required"))
if length<8:
    print("password must be 8 characters long")
else:
    password=''.join(random.choice(characters) for i in range(length))
print("\n",password)
