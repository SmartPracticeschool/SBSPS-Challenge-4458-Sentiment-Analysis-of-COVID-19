import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

data = pd.read_csv('Preprocessed/Preprocessed_Dataset.csv',parse_dates=['created_at'])
df = pd.DataFrame(data['Tweet_punct'])

words_in_tweet = []
def split_words(text):
    words_in_tweet.append(text.split())
def lower_casing(txt):
    txt = txt.lower()
    return txt
df['Tweet_punct'] = df['Tweet_punct'].apply(lambda x:lower_casing(x)) 
df['Tweet_punct'].apply(lambda x:split_words(x))
print(words_in_tweet[:2])

stop_words = set(stopwords.words('english'))
tweets_nsw = [[word for word in tweet_words if not word in stop_words]
              for tweet_words in words_in_tweet]

collection_words = ['covid','RT','rt','corona','coronavirus','virus','get','like','one']
tweets_nsw_nc = [[w for w in word if not w in collection_words]
                 for word in tweets_nsw]
all_words_nsw_nc = list(itertools.chain(*tweets_nsw_nc))

# Create counter of words in clean tweets
counts_nsw_nc = collections.Counter(all_words_nsw_nc)

print(len(counts_nsw_nc))
clean_tweets_ncw = pd.DataFrame(counts_nsw_nc.most_common(15),
                             columns=['words', 'count'])
print(clean_tweets_ncw.head(20))

# fig, ax = plt.subplots(figsize=(8, 8))

# # Plot horizontal bar graph
# clean_tweets_ncw.sort_values(by='count').plot.barh(x='words',
#                       y='count',
#                       ax=ax,
#                       color="purple")

# ax.set_title("Common Words Found in Tweets (Without Stop or Collection Words)")

# plt.show()

clean_tweets_ncw.to_csv('table/common_words.csv')