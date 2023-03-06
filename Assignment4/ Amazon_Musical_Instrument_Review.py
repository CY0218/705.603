#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Musical_instruments_reviews.csv')


# In[3]:


df.head()


# In[4]:


df_sum = df[['summary']]


# In[5]:


df_sum


# In[6]:


# import necessary libraries
import nltk
nltk.download('stopwords') # download stopwords dataset
nltk.download('punkt') # download punkt dataset
nltk.download('wordnet') # download wordnet dataset
nltk.download('omw-1.4')

# import functions from nltk library
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# define function to process text 
def process_text(text):
    # tokenize text into individual words
    tokens = word_tokenize(text.lower())
    
    # remove stop words from tokens
    stop_words = set(stopwords.words('english'))
    filtered_tokens = []
    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)
    
    # perform stemming on tokens
    stemmer = PorterStemmer()
    stemmed_tokens = []
    for token in filtered_tokens:
        stemmed_tokens.append(stemmer.stem(token))
    
    # perform lemmatization on tokens
    lemmatizer = 
    import ()
    lemmatized_tokens = []
    for token in stemmed_tokens:
        lemmatized_tokens.append(lemmatizer.lemmatize(token))
    
    # join tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

# apply process_text function to summary column in df_sum dataframe
df_sum['summary_processed'] = df_sum['summary'].apply(process_text)

# print out processed summary information
print(df_sum['summary_processed'])


# In[ ]:




