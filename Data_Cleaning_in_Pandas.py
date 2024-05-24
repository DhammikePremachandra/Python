#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning in Pandas

# In[118]:


# import libraries

import pandas as pd


# In[119]:


# import the data set

df = pd.read_excel(r"/Users/user/Documents/Data sets/Customer Call List.xlsx")

df


# In[120]:


# remove duplicates

df = df.drop_duplicates()

df


# In[121]:


#remove columns that not further necessary 

df = df.drop(columns="Not_Useful_Column") 

df


# In[122]:


df


# In[123]:


# data cleaning on Last_Name column

#df["Last_Name"] = df["Last_Name"].str.lstrip('/')

#df["Last_Name"] = df["Last_Name"].str.lstrip('...')

#df["Last_Name"] = df["Last_Name"].str.rstrip('_')

df.loc[:,"Last_Name"] = df.loc[:,"Last_Name"].str.strip("123._/")

df


# In[124]:


# data cleaning in column 'Phone_Number'

df.loc[:, 'Phone_Number']


# In[125]:


df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('--','')

df


# In[126]:


# Address split into the 3 columns that are Sreet_Address, State, Zip_Code

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', 2, expand=True)

df


# In[127]:


# replace values as Y, N in Paying Customer

df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')

df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')

df


# In[128]:


# replace values as Y, N in Do_Not_Contact

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')

df


# In[129]:


# handling None values

df = df.replace('N/a', '')

df = df.fillna('')

df


# In[130]:


# remove rows that the "Do_Not_Contact" == Y

for x in df.index:
    
    if df.loc[x, "Do_Not_Contact"] == "Y":
        
        df.drop(x, inplace=True)

df        


# In[132]:


# Remove rows where Phone Number is null

#df = df.dropna(subset=["Phone_Number"])

#df

for x in df.index:
    
    if df.loc[x, "Phone_Number"] == "":
        
        df.drop(x, inplace=True)

df    


# In[135]:


# drop unnecessary columns

df = df.drop(columns=["Address", "Zip_Code"])

df


# In[136]:


# reset index

df = df.reset_index(drop=True)

df


# In[ ]:




