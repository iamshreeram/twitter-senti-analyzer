################################################
################################################
# TITLE     : SENTIMENT ANALYZER FOR TWEETS
# AUTHOR    : SHREERAM VAIDHYANATHAN
# LICENCED  : APACHE
################################################
################################################

from textblob import TextBlob
import tweepy
import os

def auth():
    #Authentication
    cons_key = os.environ.get('CONSUMER_KEY')
    cons_sec = os.environ.get('CONSUMER_SECRET')
    acces_tk = os.environ.get('ACCESS_TOKEN')
    acces_tk_sec = os.environ.get('ACCESS_SECRET')

    print(cons_key)
    print(cons_sec)
    print(acces_tk)
    print(acces_tk_sec)


    try:
        auth = tweepy.OAuthHandler(cons_key,cons_sec)
        auth.set_access_token(acces_tk,acces_tk_sec)
        api = tweepy.API(auth)
    except:
        print("Error in authentication ")

    return api

def search(api):
    #Searching
    tweets = api.search('Trump')

    for tweet in tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)

def main():
    api = auth()
    search(api)

if __name__=="__main__":
    main()
