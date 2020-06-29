import pandas as pd
import csv

tweet_df = pd.read_csv('./datasets/Tone_analyzer/emotions_tweets.csv')

df  = pd.DataFrame(tweet_df[['user_id','Tweet','Tweet_punct','Anger','Fear','Sadness','Joy','Analytical']])


df_Anger = pd.DataFrame(tweet_df['Tweet'])
df_Fear = pd.DataFrame(tweet_df['Tweet'])
df_Sadness = pd.DataFrame(tweet_df['Tweet'])
df_Joy = pd.DataFrame(tweet_df['Tweet'])
df_Analytical = pd.DataFrame(tweet_df['Tweet'])
def sorting_emo(emo,threshold):
    if(emo >= threshold):
        return 1
    else:
        return 0

df_Anger['Emotions'] = df['Anger'].apply(lambda x: sorting_emo(x,0.2))
df_Fear['Emotions'] = df['Fear'].apply(lambda x: sorting_emo(x,0.2))
df_Sadness['Emotions'] = df['Sadness'].apply(lambda x: sorting_emo(x,0.2))
df_Joy['Emotions'] = df['Joy'].apply(lambda x: sorting_emo(x,0.2))
df_Analytical['Emotions'] = df['Analytical'].apply(lambda x: sorting_emo(x,0.2))

df_Anger.to_csv('.datasets/Training/Anger_training1.csv')
df_Fear.to_csv('.datasets/Training/Fear_training1.csv')
df_Sadness.to_csv('.datasets/Training/Sadness_training1.csv')
df_Joy.to_csv('.datasets/Training/Joy_training1.csv')
df_Analytical.to_csv('.datasets/Training/Analytical_training1.csv')


