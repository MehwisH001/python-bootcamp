#!/usr/bin/env python
# coding: utf-8

# ## DICTIONARIES
# 

# Dictionaries (or "dicts") are unordered, changeable collections of key-value pairs. They use curly braces {} and colons : to separate keys and values.
# 
# - Why use them? Fast lookups by key, no duplicates in keys.
# - Example: Store student info where "name" is key, "Mehwish" is value.
# - Introduced in Python 3.7+, they keep insertion order.

# Creating Dictionaries
# - Use {} with key-value pairs, or dict() function.
# 

# In[2]:


# Empty dict
empty_dict = {}

# With data
person = {"name": "LIVING", "age": 34, "city": "Delhi"}

# Using dict()
colors = dict(red=1, blue=2, green=3)

print(person) 


# Accessing Dictionary Elements
# - Use square brackets [] with the key, or .get() to avoid errors if key missing.

# In[3]:


person = {"name": "LIVING", "age": 25}

print(person["name"]) 
print(person.get("age"))  
print(person.get("job", "Not found"))  


# Modifying Dictionary Elements
# - Dictionaries are mutable — add, update, or remove items easily.
# 

# In[4]:


person = {"name": "LIVING"}

# Add new
person["age"] = 25

# Update existing
person["age"] = 26

# Remove
del person["age"]

print(person) 


# Dictionary Methods
# 
# Common ones:
# - keys(): Get all keys.
# - values(): Get all values.
# - items(): Get key-value pairs.
# - update(): Merge another dict.
# - clear(): Empty the dict.
# - popitem(): Remove last item.

# In[5]:


person = {"name": "LIVING", "age": 25}

print(person.keys())    
print(person.values())  
person.update({"city": "Delhi"})
print(person) 


# Iterating Over Dictionaries
# - Use loops to go through keys, values, or both.

# In[6]:


person = {"name": "LIVING", "age": 25, "city": "Delhi"}

# Over keys (default)
for key in person:
    print(key)  

# Over values
for value in person.values():
    print(value)  

# Over both
for key, value in person.items():
    print(key, ":", value)  


# Nested Dictionaries
# - Dict inside a dict— like a tree of data.

# In[7]:


students = {
    "student1": {"name": "LIVING", "age": 25},
    "student2": {"name": "Alex", "age": 22}
}

print(students["student1"]["name"])  


# Dictionary Comprehensions
# - Short way to create dicts from loops (like list comprehensions).
# Python

# In[9]:


# Square numbers
squares = {x: x**2 for x in range(1, 4)}
print(squares)  # {1: 1, 2: 4, 3: 9}

# From list
names = ["living", "alex"]
upper_dict = {name: name.upper() for name in names}
print(upper_dict)  


# practice
# 

# In[10]:


phone_book = {"alex": "123-456", "cobe": "789-012"}

# Add contact
name = input("Name: ")
number = input("Number: ")
phone_book[name] = number

# Lookup
search = input("Search name: ")
print(phone_book.get(search, "Not found"))


# Dict Keys/Values to List or Set:

# In[11]:


person = {"name": "living", "age": 25}
keys_list = list(person.keys())  
values_set = set(person.values()) 
print(keys_list, values_set)


# 
