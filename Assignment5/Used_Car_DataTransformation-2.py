#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/CY0218/EN.705.603.82.SP23/blob/main/Used_Car_DataTransformation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


get_ipython().system('unzip "/content/archive (1).zip"')


# In[ ]:


import pandas as pd


# 

# In[ ]:


data = pd.read_csv('/content/cars.csv')


# In[ ]:


data


# In[ ]:


data.info()


# In[ ]:


cols_to_encode = data.select_dtypes('object').columns


# In[ ]:


print(cols_to_encode)


# In[ ]:


from sklearn.preprocessing import OrdinalEncoder


# In[ ]:


oe = OrdinalEncoder()

data[cols_to_encode] = oe.fit_transform(data[cols_to_encode])


# In[ ]:


data


# In[ ]:


data['transmission'].value_counts()


# In[ ]:


data['model_name'].value_counts()


# In[ ]:




