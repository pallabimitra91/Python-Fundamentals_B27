#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to while loops


# In[1]:


current_num = 1
while current_num<=5:
    print(current_num)
    current_num+=1


# In[ ]:


Letting the user choose when to quit:


# In[2]:


prompt = "\n Tell me something and I will repeat it back to you"
prompt+= "\n Enter 'quit' to end the program"


# In[3]:


message = ""
while message != "quit":
    message = input(prompt)
    print(message)


# In[7]:


prompt = "\n Please enter a city you have visited: "
prompt+= "\n (Enter 'quit' when you are finished: )"
while True:
    city = input(prompt)
    if city == 'quit':
        break;
    else:
        print(f"I'd love to go to {city.title()}")


# In[9]:


current_num = 0
while current_num < 10:
    current_num+=1
    if current_num %2 == 0:
        continue
    print(current_num)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




