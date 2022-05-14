#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import os
working_directory = os.getcwd()
print (working_directory)


# In[18]:


#Load files 
school_data_to_load = working_directory +'/Resources/schools_complete.csv'
student_data_to_load = working_directory +'/Resources/students_complete.csv'


# In[22]:


school_data_df = pd.read_csv(school_data_to_load)
school_data_df.head()


# In[21]:


student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[ ]:




