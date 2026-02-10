#!/usr/bin/env python
# coding: utf-8

# ## LIST
# 

# Ordered bag you can change
# - Items stay in the order you put them
# - You can add, remove, or change items anytime(mutable)
# 
# Can hold anything mixed together
# - Numbers, strings, booleans, even other lists— all in one list
# - Example: [22, "wish", True, 3.14]

# In[1]:


lst=[]
print(type(lst))


# Creating Lists
# 
# - Empty list: scores= []
# - With values: colors= ["red", "blue", "green"]
# - From other things:
# - list("hello")['h','e','l','l','o']
# - list(range(5))[0,1,2,3,4]
# 
# Using split(): "apple banana mango".split() (list of words)

# Accessing List Elements 
# 
# - Index starts at 0
# - colors[0] first item
# - colors[-1] last item
# - colors[-2] second last
# 
# IndexError if number too big(common beginner mistake)

# Modifying List Elements
# 
# Lists are changeable!
# colors[1] = "yellow"
# colors[0] = 100 (can change type too)
# Very different from strings(strings cannot be changed like this)

# List Methods 
# 
# - .append(x) add one item at end
# - .extend([a,b]) or +=  [a,b]add many items
# - .insert (position, value)
# - .pop() remove & return last item
# - .pop(2) remove item at index 2
# - .remove("apple") remove first "apple"
# - .clear() empty the list
# - .index("blue") find position
# - .count(7) how many times 7 appears
# - .sort() / .reverse()

# Slicing Lists (1–1.5 min)
# 
# - list[start:end] from start to end-1
# - list[1:4] items 1,2,3
# - list[:3] first 3 items
# - list[2:] from index 2 to end
# - list[:] full copy
# - list[::2] every second item
# - list[::-1] reversed list

# In[5]:


#Iterating Over Lists 

fruits=["apple","banana","cherry","kiwi","gauva"]

# Simple way (most common):
for fruit in fruits:
    print(fruit)

#With index:
for i in range(len(fruits)):
    print(i, fruits[i])

#With both index & value:
for idx, item in enumerate(fruits):
    print(idx, item)


# In[7]:


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# List to Set (Remove Duplicates):

# In[1]:


dup_list = ["apple", "banana", "apple"]
unique_set = set(dup_list)  
print(unique_set)


# List to Tuple (Lock It)

# In[2]:


my_list = [1, 2, 3]
locked_tuple = tuple(my_list) 
print(locked_tuple)


# List of Tuples to Dict (Pairing):Python

# In[3]:


pairs = [("name", "living"), ("age", 25)]
person_dict = dict(pairs)
print(person_dict)

