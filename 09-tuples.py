#!/usr/bin/env python
# coding: utf-8

# ## TUPLES
# 

# - A tuple is an ordered, immutable(unchangeable) collection of items.
# - Think of it as a locked box— once you put things inside and close it, you cannot add, remove, or change anything.
# 
# - Allows duplicates
# - Can contain mixed data types
# - Uses less memory than lists
# - Very common when data should never change (coordinates, days of week, RGB colors…)

# In[3]:


# Creating Tuples 

person = ("Aisha", 24, "Delhi")              # with parentheses
scores = 85, 92, 78                          # without parentheses 
empty = ()                                   # empty tuple
single = (500,)                              # single item (comma is MUST!)
wrong = (500)                                # this is NOT a tuple, just integer
colors = tuple(["red", "green", "blue"])     # from list
letters = tuple("hello")                     # ('h','e','l','l','o')


# In[4]:


# Accessing Tuple Elements 

Pythonperson = ("Rahul", 19, "Mumbai", True)
print(person[0])     
print(person[-1])    
print(person[1:3])   


# Tuple Operations 
# 
# - Concatenation: t1 + t2
# - Repetition: t1 * 3
# - Membership: "Delhi" in person
# - Length: len(person)
# - Count: person.count("Delhi")
# - Index: person.index(19)
# - Min/Max/Sum (if num): min(scores), sum(scores)

# In[5]:


#Packing and Unpacking Tuples
#Packing = putting values into tuple
#Unpacking = taking values out into variables


# Packing
point = 10, 25           

# Unpacking
x, y = point
print(x, y)             

# Unpacking in one line (very common)
name, age, city = ("wish", 22, "Delhi")

# Using * to collect rest
a, b, *rest = (1, 2, 3, 4, 5)
print(a, b, rest)       

# Swap two variables (classic tuple trick)
x, y = y, x


# In[6]:


# Locked box – you can't change it later
person = ("Wish", 22, "Delhi")

print(person[0])     
print(person[-1])   

# You can read, but you CAN'T do this:
# person[1] = 23     error
# person.append()    error

# Most useful trick
name, age, city = person
print(name, "is", age, "from", city)

