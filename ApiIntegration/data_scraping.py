import requests
import json
import tweepy
import re
import numpy as np

#response = requests.get("http://10.20.180.204:129/Tweets/GetTweets")
baseUrl="http://10.20.180.204:129"
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAALkKawEAAAAAJu6WcNamGutOHuGErIhOhd3o0zY%3DXPFNEjBDGWXYISWAnDx8l6no5Eg8nAvYIEmNp7txSsoLPb0CMc")

def getTweets(keyword,lastTweetId):
    kewordText=keyword.get("Variation")
    kewordId=keyword.get("ParentKeywordID")
    last_id=0
    tweet_fields='author_id,created_at,public_metrics,attachments,context_annotations,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,reply_settings,source,withheld'
    for i in range(1,10):
        try:
            if(i==1 and lastTweetId==0):
                tweets = client.search_recent_tweets(query=kewordText,tweet_fields=tweet_fields, max_results=100)
            elif (i == 1 and lastTweetId!=0):
                tweets = client.search_recent_tweets(query=kewordText,tweet_fields=tweet_fields, max_results=100,until_id=lastTweetId)
            elif (i!=1):
                tweets = client.search_recent_tweets(query=kewordText,tweet_fields=tweet_fields, max_results=100,until_id=last_id)
        except:
            pass

        tweets_list = tweets.data
        if tweets_list is not None:
            for tweet in tweets_list:
                last_id = tweet.id
                clean_text=clean_tweet(tweet.text)
                #url = "http://10.20.180.204:129/Tweets/AddTweets?TweetId={TweetId}&TweetText={TweetText}&BaseKeywordID={BaseKeywordID}".format(TweetId=tweet.id, TweetText=tweet.text, BaseKeywordID=2)
                #url = "http://103.119.125.123:129/Tweets/AddTweets?TweetId={TweetId}&TweetText={TweetText}&BaseKeywordID={BaseKeywordID}".format(TweetId=tweet.id, TweetText=tweet.text, BaseKeywordID=kewordId)
                #url = "http://10.20.180.204:129/Tweets/AddTweets?TweetId={TweetId}&TweetText={TweetText}&BaseKeywordID={BaseKeywordID}".format(TweetId=tweet.id, TweetText=tweet.text, BaseKeywordID=kewordId)
                tweet_id=tweet.id
                tweet_text=tweet.text
                created_at=str(tweet.created_at)
                author_id=str(tweet.author_id)
                possibly_sensitive=str(tweet.possibly_sensitive)
                source=tweet.source
                lang=tweet.lang
                reply_settings=tweet.reply_settings
                retweet_count=str(tweet.public_metrics.get("retweet_count"))
                reply_count=str(tweet.public_metrics.get("reply_count"))
                like_count=str(tweet.public_metrics.get("like_count"))
                quote_count=str(tweet.public_metrics.get("quote_count"))

                print('text :'+tweet.text)
                print('created_at :'+str(tweet.created_at))
                print('author_id :'+str(tweet.author_id))
                print('possibly_sensitive :'+str(tweet.possibly_sensitive))
                print('source :'+tweet.source)
                print('lang :'+tweet.lang)
                print('reply_settings :'+tweet.reply_settings)
                print('retweet_count :'+str(tweet.public_metrics.get("retweet_count")))
                print('reply_count :'+str(tweet.public_metrics.get("reply_count")))
                print('like_count :'+str(tweet.public_metrics.get("like_count")))
                print('quote_count :'+str(tweet.public_metrics.get("quote_count")))
                # print('username :'+str(tweet.entities.get("mentions").get("username")))

                url = "http://10.20.180.204:129/Tweets/AddTweets?TweetId={tweet_id}&TweetText={tweet_text}&CleanedText={clean_text}&" \
                      "TweetLanguage={lang}&RetweetCount={retweet_count}&SentimentPercentage=15&BaseKeywordID={kewordId}&KeywordVariationID=2&MobTownID=547&" \
                      "ReplySettings={reply_settings}&ReplyCount={reply_count}&LikeCount={like_count}&QuoteCount={quote_count}&Hashtags=Test Tweet &" \
                      "Mentions=Test Mentions&Source={source}&AuthorId={author_id}&PossiblySensitive={possibly_sensitive}e&Lang={lang}&TweetCreatedAt={created_at}".format(
                    tweet_id=tweet_id, tweet_text=tweet_text,clean_text=clean_text, lang=lang,retweet_count=retweet_count,kewordId=kewordId,
                    reply_settings=reply_settings,reply_count=reply_count,like_count=like_count,quote_count=quote_count,source=source,author_id=author_id,
                    possibly_sensitive=possibly_sensitive,created_at=created_at)
                try:
                    response = requests.post(url)
                except:
                    print('exception')
                    pass

def getKeywordsID(keyword):
    keyword_details=next((item for item in kewordList if item["Variation"] == keyword), False)
    ParentKeywordID=keyword_details.get('ParentKeywordID')
    return ParentKeywordID

kewordList=[]
last_id=0
KeywordUrl="http://10.20.180.204:129/Tweets/GetKeywords"
def LoadKeywords(KeywordUrl):
    response = requests.get(KeywordUrl)
    kewordList = json.loads(response.text)
    return kewordList

def clean_tweet(tweet):
    if type(tweet) == np.float64:
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp)  # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]', ' ', temp)
    temp = re.sub("[^a-z0-9]", " ", temp)
    return temp




#load keyword from api
kewordList=LoadKeywords(KeywordUrl)

#loop all keywords for tweet extration
for keyword in kewordList:
    #extract and save raw tweet to databases through APIs
    getTweets(keyword,lastTweetId=0)

