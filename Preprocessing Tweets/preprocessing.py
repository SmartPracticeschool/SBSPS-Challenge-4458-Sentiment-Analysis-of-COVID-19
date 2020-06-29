import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
import nltk 
import string
import re
import csv
import string

def load_data():
    data = pd.read_csv('./datasets/Raw/raw_tweets3.csv',names=['Date','Tweet','user_id'],header = None)
    
    return data
   
tweet_df = load_data()
tweet_df.head()
print('Dataset size:',tweet_df.shape)
print('Columns are:',tweet_df.columns)
tweet_df.info()
df  = pd.DataFrame(tweet_df[['user_id', 'Tweet']])
string.punctuation
def lower_casing(text):
    text = text.lower()
    return text
df['Tweet_lowercase'] = df['Tweet'].apply(lambda x:lower_casing(x))
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

df['Tweet_punct'] = df['Tweet_lowercase'].apply(lambda x: remove_punct(x))
df.head(10)
def tokenization(text):
    text = re.split('W+', text)
    return text

df['Tweet_tokenized'] = df['Tweet_punct'].apply(lambda x: tokenization(x.lower()))
df.head()
stopword = nltk.corpus.stopwords.words('english')
def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text
    
df['Tweet_nonstop'] = df['Tweet_tokenized'].apply(lambda x: remove_stopwords(x))
df.head(1)
ps = nltk.PorterStemmer()

def stemming(text):
    text = [ps.stem(word) for word in text]
    return text

df['Tweet_stemmed'] = df['Tweet_nonstop'].apply(lambda x: stemming(x))
df.head()
wn = nltk.WordNetLemmatizer()

def lemmatizer(text):
    text = [wn.lemmatize(word) for word in text]
    return text

df['Tweet_lemmatized'] = df['Tweet_nonstop'].apply(lambda x: lemmatizer(x))
df.head()
def clean_text(text):
    text_lc = "".join([word.lower() for word in text if word not in string.punctuation]) # remove puntuation
    text_rc = re.sub('[0-9]+', '', text_lc)
    tokens = re.split('xW+', text_rc)    # tokenization
    text = [ps.stem(word) for word in tokens if word not in stopword]  # remove stopwords and stemming
    return text
df[['polarity', 'subjectivity']] = df['Tweet_punct'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
df.to_csv('./datasets/Preprocessed/preprocessed_tweets3.csv')
