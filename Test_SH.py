#!/usr/bin/env python
# coding: utf-8

# ## 서비스 최적화를 위한 Spark/Python 머신러닝 분석 수행평가

# ### 1번 수행평가

# In[36]:


from sklearn.datasets import load_breast_cancer

breast_cancer_data = load_breast_cancer()


# In[42]:


import pandas as pd
df_data = pd.DataFrame(breast_cancer_data.data)
df_labels = pd.DataFrame(breast_cancer_data.target)


# In[43]:


df_labels.head()


# In[44]:


print(breast_cancer_data.target_names)


# In[45]:


df_data.head()


# In[46]:


# 정규화

def min_max_normalize(lst):
    normalized = []
    
    for value in lst:
        normalized_num = (value - min(lst)) / (max(lst) - min(lst))
        normalized.append(normalized_num)
    
    return normalized


# In[47]:


for x in range(len(df_data.columns)):
    df_data[x] = min_max_normalize(df_data[x])
df_data.describe()


# In[48]:


# 데이터 셋 분류하기

from sklearn.model_selection import train_test_split
training_data, validation_data , training_labels, validation_labels = train_test_split(df_data, df_labels, test_size = 0.2, random_state = 100)


# In[49]:


print(len(training_data))
print(len(validation_data))
print(len(training_labels))
print(len(validation_labels))


# In[50]:


# 모델 생성하기

from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 3)


# In[51]:


classifier.fit(training_data, training_labels)


# In[52]:


print(classifier.score(validation_data, validation_labels))


# In[53]:


import matplotlib.pyplot as plt
k_list = range(1,101)
accuracies = []
for k in k_list:
  classifier = KNeighborsClassifier(n_neighbors = k)
  classifier.fit(training_data, training_labels)
  accuracies.append(classifier.score(validation_data, validation_labels))
plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()


# ### 2번 수행평가

# In[28]:


import findspark
findspark.init("/opt/spark")
import pyspark  #SPARK_HOME
from pyspark.sql import SparkSession
pyspark.__version__


# In[29]:


spark = SparkSession.builder.getOrCreate()


# In[83]:


df = spark.read.csv("/dataSet/01_트위터/twitter_맛집_467147.csv")
df


# In[84]:


df.show()


# In[ ]:


# 2번째 방법


# In[86]:


data_path = "/dataSet/01_트위터/twitter_맛집_467147.csv"
sample = spark.read.option("header", "true").csv(data_path)
sample


# In[87]:


type(sample)


# In[92]:


sample.show()

