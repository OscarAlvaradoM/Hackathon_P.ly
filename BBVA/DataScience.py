#!/usr/bin/env python
# coding: utf-8

# # SCIAN.
# 

# In[207]:


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
print(df_csv) 




# In[174]:


x, y = df_csv.iloc[0:70,0:2].values, df_csv.iloc[0:70,0:2].values  # iloc es para indexar con enteros (integerLocation)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)


# In[175]:


x_train.shape


# In[206]:


'''colors = np.array(['lime','red','black','blue','cyan'])
y = y_train[:,1]
plt.scatter(x_train[:,1],x_train[:,1],c=colors[y.astype(int)],edgecolor='black')'''


# In[ ]:





# In[ ]:





# In[ ]:




