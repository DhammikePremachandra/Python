#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from a Real Website + Pandas

# In[34]:


# Import Libraries

from bs4 import BeautifulSoup
import requests


# In[35]:


# Connect to website and pull in data

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_Kingdom'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[36]:


print(soup)


# In[37]:


# Explore the data

soup.find_all('table')[2]


# In[38]:


# Select table that need to be scraped

table = soup.find_all('table')[2]
print(table)


# In[39]:


# Look at table titles

table_titles = table.find_all('th')
table_titles


# In[40]:


# Extract table titles into a list 

table_column_names = [title.text.strip() for title in table_titles]
print(table_column_names)


# In[41]:


# Import pandas library

import pandas as pd


# In[42]:


# import table titles into a data frame

df = pd.DataFrame(columns=table_column_names)
df


# In[43]:


# Look at column data

column_data = table.find_all('tr')
column_data


# In[44]:


# Import column data into the data frame

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[45]:


df


# In[46]:


# Save scraped data as a csv file 

df.to_csv(r'/Users/user/Documents/Data sets/Companies.csv', index=False)


# In[ ]:





# In[ ]:




