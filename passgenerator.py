import string
import random 

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

p_len = int(input("Enter Password Length : \n"))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

password = "".join(random.choice(s) for _ in range(p_len))
print(password)
