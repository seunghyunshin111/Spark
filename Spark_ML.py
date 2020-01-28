#!/usr/bin/env python
# coding: utf-8

# # Spark의 머신러닝

# In[23]:


import findspark
findspark.init("/opt/spark")
import pyspark  #SPARK_HOME
from pyspark.sql import SparkSession
pyspark.__version__


# In[4]:


spark = SparkSession.builder.getOrCreate()
#spark = sparkContext()


# In[6]:


df = spark.read.json("/home/lab11/data/simple-ml")
df


# In[7]:


df.show()


# In[8]:


df.orderBy("value2").show()


# In[10]:


df.select("lab").show()


# In[16]:


# lab의 good 만 추출

df.select("lab").filter("lab=='good'").show()


# # 분류 모형

# ### 시험 문제
# ### 교재:635

# In[28]:


### 시험 문제
# 교재:635

bInput = spark.read.format("parquet").load("/home/lab11/data/binary-classification")    .selectExpr("features", "cast(label as double) as label")


# - load(): 로드 형식이 하둡 기반의 데이터를 끌고오기 때문에 이러한 형태를 보이는 것

# In[29]:


bInput


# In[30]:


from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression()

print(lr.explainParams())  # see all parameters
lrModel = lr.fit(bInput)


# In[31]:


bInput.show()


# In[32]:


lrModel.coefficients


# In[33]:


print(lrModel.coefficients)


# In[34]:


print(lrModel.intercept)


# - 스파크는 일반적으로 데이터 전처리까지 많이 쓰인다. 데이터 수집하고 크롤링 걸러내는 것 빠른 속도로 처리해준다.
# - 모형 만드는 것은 혼자서 서버 하나 돌려 놓으면 된다.
# - 분산 모형을 만들어도 되는 것에도 속도가 빠르다. (SVM, 랜덤 포레스트, 파라미터 조정에 따라 결과 보는 것들을 스파크 베이스로 하면 한 번에 여러 가지를 돌려놓을 수 있다.)

# # 스파크 실습 시험 문제!
# ## - 로지스틱 회귀 분석 코드만 작성하면 되는 시험 문제! *Spark (해석X, 사용법만!)

# In[44]:


summary = lrModel.summary

print("summary.areaUnderRoc")
summary.roc.show()
summary.pr.show()


# In[ ]:




