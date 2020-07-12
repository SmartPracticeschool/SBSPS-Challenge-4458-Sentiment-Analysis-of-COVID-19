import pandas as pd
import datetime
import csv
import nltk
d1 = pd.read_csv('BERT/Analytical/Bert_analytical.csv',parse_dates=['created_at'])
d0 = pd.read_csv('BERT/Anger/Bert_anger.csv',parse_dates=['created_at'])
d2 = pd.read_csv('BERT/Fear/Bert_fear.csv',parse_dates=['created_at'])
d3 = pd.read_csv('BERT/Joy/Bert_joy.csv',parse_dates=['created_at'])
d4 = pd.read_csv('BERT/Sadness/Bert_sadness.csv',parse_dates=['created_at'])
df = pd.DataFrame(d0[['created_at','anger_output']])
df['analytical_output'] = d1['analytical_output']
df['fear_output'] = d2['fear_output']
df['joy_output'] = d3['joy_output']
df['sadness_output'] = d4['sadness_output']
# df['seg_sentiment'] = df.sum(axis=1)
# df = pd.DataFrame(data[['Date','polarity','subjectivity']])
cols = df.columns.difference(['created_at'])
df[cols] = df[cols].astype(float)
df1 = df.set_index('created_at').groupby(pd.Grouper(freq='d')).sum().dropna(how='all')
df1['anger_output'] = df1['anger_output']*100
df1['analytical_output'] = df1['analytical_output']*100
df1['fear_output'] = df1['fear_output']*100
df1['joy_output'] = df1['joy_output']*100
df1['sadness_output'] = df1['sadness_output']*100
# df1['difference'] = df1.seg_sentiment.diff()
# df1['difference'] = df1['difference']/df1['seg_sentiment']

# #print (df.head(10))
df1.to_csv('table/Number_emotion.csv')
print(df1.head(20))
print(df1.shape)