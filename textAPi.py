import tweepy
import pandas as pd
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAALkKawEAAAAAJu6WcNamGutOHuGErIhOhd3o0zY%3DXPFNEjBDGWXYISWAnDx8l6no5Eg8nAvYIEmNp7txSsoLPb0CMc")
tweets = client.search_recent_tweets(query="imran khan", max_results=10)
tweetarry=[]
for tweet in tweets.data:
    tweetarry.append({'text': tweet.text, 'Id':tweet.id})
    print(tweet.id,tweet.text)
df=pd.DataFrame(tweetarry)
df.to_csv('test.csv')
