#!/usr/bin/env python
# coding: utf-8

# # SCIAN INEGI.
# 

# In[2]:


import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

df_csv = pd.read_csv('/home/joiortega1/Descargas/suboriginal.csv')
df_csv.dropna(axis = 0, how = 'any', inplace = True) 
df_csv.to_csv('/home/joiortega1/Descargas/subsector.csv', index = False)
df_csv[1:70] 




# # Datos BBVA

# In[6]:


df_csv = pd.read_csv('/home/joiortega1/Descargas/datosbbva.csv')
df_csv.dropna(axis = 0, how = 'any', inplace = True) 
df_csv.to_csv('/home/joiortega1/Descargas/datosbbva.csv', index = False)
df_csv


# In[ ]:





# 

# 

# 
