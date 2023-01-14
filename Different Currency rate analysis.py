#!/usr/bin/env python
# coding: utf-8

# In[10]:


from forex_python.converter import CurrencyRates


# In[16]:


import pandas as pd


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


cr = CurrencyRates()
data = {'USD': [cr.get_rate('USD', 'EUR', date) for date in pd.date_range('2022-01-01', '2022-12-31').tolist()]}
df = pd.DataFrame(data)
df.plot()
plt.show()


# In[19]:


cr = CurrencyRates()
data = {'INR': [cr.get_rate('INR', 'EUR', date) for date in pd.date_range('2022-01-01', '2022-12-31').tolist()]}
df = pd.DataFrame(data)
df.plot()
plt.show()


# In[20]:


cr = CurrencyRates()
data = {'EUR': [cr.get_rate('EUR', 'USD', date) for date in pd.date_range('2022-01-01', '2022-12-31').tolist()]}
df = pd.DataFrame(data)
df.plot()
plt.show()


# In[ ]:




