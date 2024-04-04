#!/usr/bin/env python
# coding: utf-8

# In[1]:


height = int(input("Enter your height "))
weight = int(input("Enter your weight "))
height = height/100.0
bmi = weight / (height**2)
if bmi <= 15.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: Very severly underweight!!"
    print(res)
elif 15.0 < bmi <= 16.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: severly underweight!!"
    print(res)
elif 16.0 < bmi <= 18.5:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: underweight!!"
    print(res)
elif 18.5 < bmi <= 25.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: normal!!"
    print(res)
elif 25.0 < bmi <= 30.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: overweight!!"
    print(res)
elif 30.0 < bmi <= 35.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks:moderately obese!!"
    print(res)
elif 35.0 < bmi <= 40.0:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: Severly obese!"
    print(res)
else:
    res = 'Your BMI is '+ str(bmi) + "\nRemarks: Super obese!!"
    print(res)


# In[ ]:




