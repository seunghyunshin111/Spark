#!/usr/bin/env python
# coding: utf-8

# In[4]:


import findspark

findspark.init("/opt/spark")


# In[6]:


import pyspark  #SPARK_HOME
from pyspark.sql import SparkSession
pyspark.__version__


# In[8]:


spark = SparkSession.builder.getOrCreate()  # sparkContext


# In[9]:


myRange = spark.range(1000).toDF("number")


# In[10]:


type(myRange)


# In[11]:


myRange.show()


# In[12]:


# 시험문제


# In[14]:


# 스파크 애플리케이션은 SparkSession이라는 드라이버 프로세스로 제어

# spark = SparkSession.builder.getOrCreate()
# spark = SparkContext()

data_path = "/dataSet/01_트위터/twitter_맛집_467147.csv"
sample = spark.read.option("header", "true").csv(data_path)


# In[15]:


type(sample)


# In[16]:


sample.show()


# In[ ]:





# In[ ]:




