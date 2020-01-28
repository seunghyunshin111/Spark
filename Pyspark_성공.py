#!/usr/bin/env python
# coding: utf-8

# In[3]:


import findspark

findspark.init("/opt/spark")


# In[4]:


import pyspark
from pyspark.sql import SparkSession


# In[12]:


pyspark.__version__


# In[13]:


## Spark 2.x

spark = SparkSession.builder.getOrCreate()


# In[14]:


spark

