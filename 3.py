#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
page= requests.get("https://olympics.com/es/olympic-games")


# In[3]:


page


# In[30]:


page.content


# In[5]:


from bs4 import BeautifulSoup


# In[33]:


soup = BeautifulSoup(page.content, 'html.parser')
soup


# In[35]:


soup.find_all('p')


# In[37]:


s1 = soup.find_all('p')[0].get_text()


# In[38]:


s2 = soup.find_all('p')[1].get_text()


# In[39]:


s1


# In[40]:


s2


# In[44]:


pip install pandas


# In[48]:


import pandas as pd
data = {'texto1': [s1], 'texto2': [s2]}
data


# In[49]:


textospagina = pd.DataFrame(data)


# In[50]:


textospagina.to_csv('textospag.csv')


# In[ ]:




