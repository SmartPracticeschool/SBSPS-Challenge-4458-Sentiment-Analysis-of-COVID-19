import pandas as pd
import datetime as dt
df = pd.read_csv('BERT/Anger/Bert_anger.csv')
df['created_at'] = pd.to_datetime(df['created_at'])
df['created_at']= df['created_at'].apply(lambda x:x.date().strftime('%m-%d-%Y'))
df.index = pd.to_datetime(df['created_at'])
# print(df['polarity'].head())
# Lists = [[],[],[]]
# def make_cols(pol):
#     if pol > 0:
#         Lists[0].append(1)
#         Lists[1].append(0)
#         Lists[2].append(0)
#     elif pol<0:
#         Lists[0].append(0)
#         Lists[1].append(1)
#         Lists[2].append(0)
#     else:
#         Lists[0].append(0)
#         Lists[1].append(0)
#         Lists[2].append(1)

# df['polarity'].apply(lambda x: make_cols(x))
# df['Positive'] = pd.Series(Lists[0]).values
# df['Negative'] = pd.Series(Lists[1]).values
# df['Neutral'] = pd.Series(Lists[2]).values
df2 = pd.DataFrame(df[['created_at','anger_output']])
# df3 = pd.DataFrame(df[['created_at','polarity','subjectivity']])
df4 = df2.groupby(pd.Grouper(freq='d')).mean().dropna(how='all')
# df5 = df3.groupby(pd.Grouper(freq='d')).mean().dropna(how='all')
print(df4.head())
print(df4.shape)
# print(df5.head())
df4.to_csv('BERT/Bert_mang_only.csv')
# df5.to_csv('table/avg_pol/avg_pol_apr3.csv')
#print(df3.head())
#df3.to_csv('pos_neg.csv')
#sum_column = df.sum(axis=0)
#print(sum_column)
#Total = df['Positive'].sum()
#print (Total)

