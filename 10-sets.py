#!/usr/bin/env python
# coding: utf-8

# ## SET

# A set is like a bag of unique things with no order and no duplicates.
# - Only keeps unique items (duplicates disappear automatically)
# - Uses curly braces { }

# In[6]:


my_empty_set=set()
print(type(my_empty_set))


# In[7]:


my_set=set([1,2,3,4,5,6])
print(my_set)


# In[3]:


## ERROR
print(fruits[0])         
fruits[1] = "kiwi"       
fruits.append("pear")    


# In[2]:


# Creating a set
fruits = {"apple", "banana", "mango", "apple"}   
print(fruits)         

# Add something
fruits.add("orange")
print(fruits)         

# Remove something
fruits.remove("banana")

# Check if exists (super fast!)
print("mango" in fruits)    
print("grapes" in fruits)    


# In[5]:


# Remove duplicates from list
numbers = [5, 2, 8, 2, 5, 9]
unique = set(numbers)         

# Find common things (intersection)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)        

# Find things in one but not other (difference)
print(a - b)         

# Combine two sets (union)
print(a | b)          

