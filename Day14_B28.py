#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to Python functions


# In[ ]:


code reusibility:


# In[ ]:


Functions are named block of code that are designed to one specific job


# In[ ]:


#Defining a function --> Req: to greet user!


# In[ ]:


#whule giving the function name always use small case letters


# In[1]:


def greet_user():
    """Display a simple greeting""" #doc string to explain a function use. Use of docstring for commenting inside a function
    print("Hello")
    


# In[2]:


greet_user() #function call


# In[ ]:


Introduction to parameters and arguments


# In[ ]:


#defining any function --> passing any info to the function--> Parameters passing


# In[3]:


def greet_user(user):
    """Display a simple greeting to the user"""
    print(f"Hello {user.title()}")


# In[4]:


greet_user("pallabi") #argument passing


# In[ ]:


#Understanding the types of arguments


# In[ ]:


1. positional arguments


# In[6]:


def describe_pet(animal_type,pet_name): #order of the params
    """Display information about a pet"""
    print(f"\n I have a {animal_type}")
    print(f" my {animal_type}'s name is {pet_name}")


# In[7]:


describe_pet("cat","zumi")


# In[8]:


describe_pet("dog","jenny")


# In[9]:


describe_pet("jenny","dog")#wrong order


# In[10]:


2. keyword arguments
describe_pet(pet_name = "jenny", animal_type = "cat") #keyword argument where pet_name and animal_type are keywords .


# In[ ]:


3. default arguments
#if the animal type is missing assume it to be dog
#** default params need to be declared at the end of func while defining a func


# In[12]:


def describe_pet(pet_name,animal_type = "dog"): #order of the params
    """Display information about a pet"""
    print(f"\n I have a {animal_type}")
    print(f" my {animal_type}'s name is {pet_name}")


# In[13]:


describe_pet("Jenny")


# In[14]:


describe_pet("Zumi","Cat")


# In[ ]:





# In[ ]:




