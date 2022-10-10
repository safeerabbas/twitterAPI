import tweepy
import pandas as pd
#client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAAC0ZwEAAAAAiyG6E8BK7ayHh2hZq7GPp7BVnvI%3DcRTs97kR9UV8H5uktjwhVKlhgGIQsObuN1m8GEY5ZT6QrIep4e")
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAALkKawEAAAAAJu6WcNamGutOHuGErIhOhd3o0zY%3DXPFNEjBDGWXYISWAnDx8l6no5Eg8nAvYIEmNp7txSsoLPb0CMc")


def getTweets(keyword,lastTweetId):
    output = []
    for i in range(1,15):
        global last_id
        if(i==1 and lastTweetId==0):
            #tweets = client.search_recent_tweets(query="sit in OR jaloos OR protest OR ehtijaj", max_results=10)
            tweets = client.search_recent_tweets(query=keyword, max_results=100)
        elif (i == 1 and lastTweetId!=0):
            # tweets = client.search_recent_tweets(query="sit in OR jaloos OR protest OR ehtijaj", max_results=10)
            tweets = client.search_recent_tweets(query=keyword, max_results=100,until_id=lastTweetId)
        else:
            tweets = client.search_recent_tweets(query=keyword, max_results=100,until_id=last_id)

        tweets_list = tweets.data
        if tweets_list is not None:
            for tweet in tweets_list:
                last_id = tweet.id
                print(tweet.text)
                line = {'text': tweet.text, 'Id':tweet.id}
                output.append(line)
        if tweets_list is None:
            return output
    return output

#df = pd.DataFrame(output)
#df.to_csv('jalsa1.csv', mode='a', index=True, header=False)
