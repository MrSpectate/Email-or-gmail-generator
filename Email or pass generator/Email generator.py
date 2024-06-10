# Generator Email and password !

import random
import string

while True:
# guess the characters of email
 character = "".join(random.choices(string.ascii_lowercase + string.digits , k = 10))

# adding domain
 domain = "@gmail.com"

# combine character and domain
 gmail = print(f"Generated Email : {character}{domain}")









