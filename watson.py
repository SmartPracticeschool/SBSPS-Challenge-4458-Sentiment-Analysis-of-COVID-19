from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import pandas as pd

versionIBM = '2020-06-29'
api = '_Nmbca6XuMEqHYd-9Zt33DcVyVPT9icpgeFwVzFLL4Zn'
url = 'https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/87e1d06c-f0ce-4134-a554-bee7f4c3fb16'
authenticator = IAMAuthenticator(api)
tone_analyzer = ToneAnalyzerV3(
    version=versionIBM,
    authenticator=authenticator
)

tone_analyzer.set_service_url(url)

tweet_df = pd.read_csv('./datasets/Preprocessed/preprocessed_tweets1.csv')
df  = pd.DataFrame(tweet_df[['user_id','Tweet_punct']])
emotions = {
        "anger": 0,
        "fear" : 1,
        "sadness": 2,
        "joy" : 3,
        "analytical": 4,
        "confident": 5,
        "tentative" :6
    }
Lists = [[],[],[],[],[],[],[]]

def watson(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    emo = [0 , 0 , 0 , 0 , 0 , 0, 0]
    for i in range(len(tone_analysis['document_tone']['tones'])):
        A =tone_analysis['document_tone']['tones'][i]['tone_id']
        A_score = tone_analysis['document_tone']['tones'][i]['score']
        print('Tweet Processing. DO NOT TOUCH OR STOP IT BY ANY MEANS')
        emo[emotions[A]] = A_score
    for i in range(0,7):
        Lists[i].append(emo[i])


df['Tweet_punct'].apply(lambda x : watson(x))
print(len(Lists[0]))
df['Anger'] = pd.Series(Lists[0]).values
df['Fear'] = pd.Series(Lists[1]).values
df['Sadness'] = pd.Series(Lists[2]).values
df['Joy'] = pd.Series(Lists[3]).values
df['Analytical'] = pd.Series(Lists[4]).values
df['Confident'] = pd.Series(Lists[5]).values
df['Tentative'] = pd.Series(Lists[6]).values
df.to_csv('./datasets/Tone_analyzer/emotions_tweets.csv')
print("Process Complete")

    



    



   

  

    
    

