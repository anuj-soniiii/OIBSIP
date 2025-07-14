import string
import random 

s1 = string.ascii_lowercase
# Used to add lowercase alphabets.

s2 = string.ascii_uppercase
# Used to add uppercase alphabets.

s3 = string.digits
# Used to add digits.

s4 = string.punctuation
# Used to add different symbols.

p_len = int(input("Enter Password Length : \n"))
# Taking input from our user . what is the needed length of password.

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# In last four steps we extend our list.

password = "".join(random.choice(s) for _ in range(p_len))
# Now we generate a random password as user needed.
print(password)
