import tweepy
from tweepy import OAuthHandler
import csv
import wget
     


class TwitterClient(object):

    def __init__(self):
        #Credentials     
        consumer_key = "uj6SN7IlIWah3ABXMxhTBQd0Q"
        consumer_secret = "dUk5dHNGMxf0lefXjdIPa5tT4zY2bd9JbK9ZrtCuH0LGAiYF7L"
        access_token = "710152588742688768-QUpQrIbb6tHRJmyONn9VUk7ytWammd9"
        access_token_secret = "fYfetPEtyJk5eUZaWC0KLfWmzMkn9sL3MigNTmu9S8XLL"

        try:
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

        except tweepy.TweepError as e:
            print(f"Error: Twitter Authentication Failed \n {str(e)}")


    def get_tweets(self):    
        csvFile = open('./datasets/Raw/raw_tweets3.csv', 'a',newline = "", encoding = "utf-8")
        csvWriter = csv.writer(csvFile)
        media_files = set()
        tweets = tweepy.Cursor(self.api.search,q="#covid19India -filter:retweets",count=15000, tweet_mode = 'extended').items(15000)
        for tweet in tweets:
            if tweet.lang != "en":
                continue
            csvWriter.writerow([tweet.created_at, tweet.full_text, tweet.user.id])                     
        csvFile.close()                      

if __name__ == '__main__':
    Twitter = TwitterClient()
    Twitter.get_tweets()
    
