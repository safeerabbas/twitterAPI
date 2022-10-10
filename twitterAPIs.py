import tweepy
import pandas as pd
#client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAAC0ZwEAAAAAiyG6E8BK7ayHh2hZq7GPp7BVnvI%3DcRTs97kR9UV8H5uktjwhVKlhgGIQsObuN1m8GEY5ZT6QrIep4e")
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAALkKawEAAAAAJu6WcNamGutOHuGErIhOhd3o0zY%3DXPFNEjBDGWXYISWAnDx8l6no5Eg8nAvYIEmNp7txSsoLPb0CMc")
query = 'machine learning'
# get max. 10 tweets
#tweets = client.search_recent_tweets(query=query,max_results=2)

#client.search_recent_tweets(query="sit in OR jaloos OR protest OR ehtijaj", max_results=10)

output = []
for i in range(1,10):
    global last_id
    if(i==1):
        #tweets = client.search_recent_tweets(query="sit in OR jaloos OR protest OR ehtijaj", max_results=10)
        tweets = client.search_recent_tweets(query="jalsa", max_results=100)
    else:
        tweets = client.search_recent_tweets(query="jalsa", max_results=100,until_id=last_id)

    tweets_list = tweets.data
    if(len(tweets_list)!=0):
        for tweet in tweets_list:
            text = tweet.text
            id= tweet.id
            last_id = tweet.id
            print(tweet.text)
            line = {'text': text, 'Id':id}
            output.append(line)

df = pd.DataFrame(output)
df.to_csv('jalsa1.csv', mode='a', index=True, header=False)
