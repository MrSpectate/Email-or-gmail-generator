
import random
import string


# length for password
  
# length = int(input("Enter the length : "))
# guessing the character
while True:

 character = (string.ascii_letters + string.ascii_lowercase + string.punctuation )
# now combine all the varaiable

 password = "".join(random.choice(character , k = 8))
# now print password

 Generated_Password = print(f"Generated Password : {password}")




