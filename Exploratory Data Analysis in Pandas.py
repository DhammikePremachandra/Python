#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis in Pandas

# In[2]:


# Import Libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Import data set

df = pd.read_csv(r"/Users/user/Documents/Data sets/world_population.csv")
df


# In[4]:


# Set decimal point like '.00'

pd.set_option('display.float_format', lambda x: '%.2f' % x)
df


# In[5]:


# Explore about Informations hidden in the data set

df.info()


# In[6]:


# Stat of the data set

df.describe()


# In[7]:


# Null values

df.isnull().sum()


# In[8]:


# Unique values

df.nunique()


# In[9]:


# Explore top 10 countries that is contributing to the world population

df.sort_values(by="World Population Percentage", ascending=False).head(10)


# In[17]:


# correlation between numeric values

df.corr(numeric_only=True)


# In[18]:


# Heatmap 

sns.heatmap(df.corr(numeric_only=True), annot = True)

plt.rcParams['figure.figsize'] = (25,10)

plt.show()


# In[20]:


# Groupby according to continent

df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)


# In[27]:


df[df['Continent'].str.contains('Asia')].sort_values(by="Growth Rate", ascending=False)


# In[28]:


# Groupby according to Contnent of population data 

df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
df2


# In[31]:


#transpose columns into rows

df3 = df2.transpose()
df3


# In[32]:


#line graph

df3.plot()


# In[38]:


#Box plot

df.boxplot(figsize=(15,15))


# In[39]:


df.select_dtypes(include='object')


# In[ ]:




