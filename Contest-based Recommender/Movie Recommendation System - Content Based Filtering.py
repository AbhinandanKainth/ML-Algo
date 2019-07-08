#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import pandas as pd


# In[62]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[63]:


df = pd.read_csv("movie_dataset.csv")


# In[116]:


#print(df.columns)


# In[67]:


features = ['keywords','cast','genres','director']


# In[90]:


for feature in features:
    df[feature] = df[feature].fillna('')


# In[91]:


def combine_features(row):
    try:
        return row['keywords'] + " " +  row['cast'] + " " + row["genres"] + row["director"]
    except:
        print("error : ",row)


# In[92]:


df['combine_features'] = df.apply(combine_features,axis=1)


# In[115]:


#print(df["combine_features"].head())


# In[102]:


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


# In[103]:


cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combine_features"])


# In[139]:


cosine_sim = cosine_similarity(count_matrix)
movie_user_likes = "Spider-Man"


# In[140]:


movie_index = get_index_from_title(movie_user_likes)


# In[141]:


similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)


# In[142]:


i=0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if(i>10):
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[52]:





# In[53]:





# In[54]:





# In[55]:





# In[ ]:





# In[58]:





# In[ ]:





# In[ ]:




