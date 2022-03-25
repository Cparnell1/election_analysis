#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Add our dependencies.
import csv
import os
import pandas as pd


# In[2]:


# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")


# In[3]:


file_to_load


# In[5]:


pd.read_csv(file_to_load)


# In[6]:


file_path = 'Resources/election_results.csv'


# In[7]:


pd.read_csv(file_path)


# In[ ]:




