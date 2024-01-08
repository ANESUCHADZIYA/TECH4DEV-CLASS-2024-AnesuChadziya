#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1

# In[3]:


print("+----+")
for i in range(3):
    print("\\   /")
    print("/   \\")
print("+----+")


# # QUESTION 2

# In[4]:


for i in range(5):
    print("**********")


# # QUESTION 3

# # a

# In[5]:


for i in range(1,7):
    print(i)


# # b

# In[6]:


for i in range(1,7):
    print(i*2)


# # c

# In[7]:


for i in range(1,7):
    print(15 * i - 11)


# # d

# In[8]:


for i in range(1,7):
    print(40 - 10 * i)


# # e

# In[9]:


for i in range(1,7):
    print(4 * i - 11)


# # f

# In[10]:


for i in range(1,7):
    print(100 - 3 * i)


# # g

# In[14]:


for i in range(1,7):
    print(i*18 - 22)


# # QUESTION 4

# In[13]:


class Config:
#constant to adjust the number of lines
    LINES = 7  

for i in range(1, Config.LINES + 1):
    print(str(i) * i)


# # QUESTION 5

# In[15]:


def pay(salary, hours):
    if hours <= 8:
        return salary * hours
    else:
        regular_pay = salary * 8
        overtime_pay = salary * 1.5 * (hours - 8)
        return regular_pay + overtime_pay


# # QUESTION 6

# In[16]:


#Area of a circle

import math
#Define area
def area(radius):
    return math.pi * radius ** 2


# # QUESTION 7

# In[17]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0
for i in range(low, high):
    sum += i
print("sum = ", sum)


# # QUESTION 8

# In[18]:


total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))

print("The sum of the numbers is", total)


# # QUESTION 9

# In[19]:


total = 0
number = int(input("Enter a number (-1 to stop): "))

while number != -1:
    total += number
    number = int(input("Enter a number (-1 to stop): "))

print("The sum of the numbers is", total)


# # QUESTION 10

# In[22]:


def rep1(string, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return string * repetitions

# Testing the method
print(rep1("hello", 3)) 


# # QUESTION 11

# In[29]:


def printRange(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i, end=' ')
    elif start > end:
        for i in range(start, end - 1, -1):
            print(i, end=' ')
    else:
        print(start)

# Testing the method
printRange(2, 7) 


# # QUESTION 12

# In[ ]:


#def Largest():
    n = int(input("How many numbers do you want to enter? "))
    numbers = []
    for i in range(1, n + 1):
        num = int(input(f"Number {i}: "))
        numbers.append(num)
    print("Smallest =", min(numbers))
    print("Largest =", max(numbers))

# Testing the method
smallestLargest()
Largest()


# # QUESTION 13

# In[2]:


def printAverage():
    total = 0.0
    count = 0

    while True:
        num = float(input("Enter a number: "))
        if num < 0:
            break
        total += num
        count += 1

    if count > 0:
        average = total / count
        print("Average of all nonnegative numbers: ", average)
    else:
        print("No nonnegative numbers were entered.")

printAverage()


# # QUESTION 14

# In[4]:


def numUnique(a, b, c):
    return len(set([a, b, c]))

# Testing the function
print(numUnique(18, 3, 4))  


# # QUESTION 15

# In[5]:


import random

def roll_dice():
    return random.randint(1, 6)

def simulate():
    roll1 = roll_dice()
    roll2 = roll_dice()
    while roll1 + roll2 != 7:
        print(f"{roll1} + {roll2} = {roll1 + roll2}")
        roll1 = roll_dice()
        roll2 = roll_dice()
    print(f"{roll1} + {roll2} = 7")

simulate()


# In[ ]:




