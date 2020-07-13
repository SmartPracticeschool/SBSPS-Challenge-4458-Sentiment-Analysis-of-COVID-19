import pandas as pd
import os 
from datetime import datetime

path = r'BERT/Sadness/'
files = os.listdir(path)
covid_twitter_data = pd.DataFrame(columns=['created_at','text','sadness_output'])
print(covid_twitter_data.head())
def sentencelen(text):
    words = text.split()
    l = sum(len(word) for word in words)
    if(l>512):
        print('Aha')
        # Concat the Twitters data into one-table
for file in files:
    data = pd.read_csv(str(path) + file, engine='python',usecols = ['created_at','text','sadness_output'])
    # data = data[data['text'].map(len) < 512].sample(1500)
    # data['text'].apply(lambda x : sentencelen(x))
    covid_twitter_data = covid_twitter_data.append(data, ignore_index=True)
    print(data.shape)

# df['created_at'] = pd.to_datetime(df['created_at'])
# df['created_at']= df['created_at'].apply(lambda x:x.date().strftime('%m-%d-%Y'))
# covid_twitter_data.index = pd.to_datetime(covid_twitter_data['created_at'])
# covid_twitter_data = covid_twitter_data.drop('created_at', 1)
# covid_twitter_data2 = covid_twitter_data.groupby(by = covid_twitter_data.index).sum().dropna(how='all')
covid_twitter_data.to_csv('BERT/Sadness/Bert_sadness.csv')
print(covid_twitter_data.head(40))
print(covid_twitter_data.shape)
