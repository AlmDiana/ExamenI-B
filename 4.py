#!/usr/bin/env python
# coding: utf-8

# In[65]:


import requests
page= requests.get("https://www.facebook.com/photo/?fbid=5813038822099392&set=a.188770884526242")


# In[66]:


page


# In[67]:


page.content


# In[68]:


from bs4 import BeautifulSoup


# In[69]:


soup = BeautifulSoup(page.content, 'html.parser')
soup


# In[70]:


soup.find_all('title')


# In[72]:


s1 = soup.find_all('title')[0].get_text()


# In[74]:


s1


# In[75]:


pip install pandas


# In[76]:


import pandas as pd
data = {'texto1': [s1], 'texto2': [s1]}
data


# In[77]:


textospagina = pd.DataFrame(data)


# In[78]:


textospagina.to_csv('textospag2.csv')


# In[ ]:




