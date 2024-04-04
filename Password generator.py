#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string 
import random
length = int(input("Enter password length: "))
print('''Choose character set for password from these:
        1. Digits
        2. Letters
        3. Special Characters
        4. Exit''')
characterList = ""
while(True):
    ch = int(input("Pick a number "))
    if(ch==1):
        characterList += string.ascii_letters
    elif(ch==2):
        characterList += string.digits
    elif(ch==3):
        characterList += string.punctuation
    elif(ch==4):
        break
    else:
        print('Please choose a valid option')
password = []
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("Your generated password is "+"".join(password))


# In[ ]:




