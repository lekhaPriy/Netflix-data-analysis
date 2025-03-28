#!/usr/bin/env python
# coding: utf-8

# ## Importing python libraries

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## Importing the dataset into python

# In[4]:


#load dataset
ntf = pd.read_csv(r"C:\Users\lekha\Downloads\Compressed\archive_6\netflix_titles.csv")


# ## Data Exploration

# In[6]:


ntf.shape


# In[7]:


# view first few rows
ntf.head() 


# In[8]:


ntf.describe()


# In[9]:


# check column names and missing values
ntf.info()


# In[10]:


ntf.columns


# ## Data cleaning

# In[11]:


# drop missing values
ntf = ntf.dropna()


# In[12]:


# Convert release year to integer
ntf['release_year'] = ntf['release_year'].astype(int)
# Convert 'date_added' to datetime
ntf['date_added'] = pd.to_datetime(ntf['date_added'])
print(ntf.info()) # checking data types again


# ## Data Visualization

# In[13]:


# Count movies by genre
genre_counts = ntf['listed_in'].value_counts().head(10)

# Plot
plt.figure(figsize=(10,5))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="coolwarm")
plt.xlabel("Number of Movies")
plt.ylabel("Genre")
plt.title("Top 10 Most Common Netflix Genres")
plt.show()


# In[14]:


# Count movies by release year
year_counts = ntf['release_year'].value_counts().sort_index()

# Plot
plt.figure(figsize=(12,6))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", color="red")
plt.xlabel("Year")
plt.ylabel("Number of Movies/TV Shows")
plt.title("Netflix Content Over the Years")
plt.grid(True)
plt.show()


# ## Conclusion

# ##### Netflix's content library has expanded significantly in recent years with strong focus on genres like drama, international movies. This project showcases how data analysis can reveal hidden trends in entertainment platforms. 

# In[ ]:




