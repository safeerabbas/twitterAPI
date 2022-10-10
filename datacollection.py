import SingleKeywodScraping as api
import readfile as rf
import time
import pandas as pd
import os


keywordlist= ['jaloos','jalus','jalos','jalsa','ehtejaj','ahtjaj' ,'ehtijaj','ehtajaj','dharna','darna','sit in','protest']
#keywordlist= ['jaloos','ehtijaj']
output = []
for keyword in keywordlist:
    complitefileName=rf.getCompleteFileName(keyword)
    complitefileName=complitefileName+".csv"
    r=os.path.exists(complitefileName)
    if(os.path.exists(complitefileName)):
        lastTweetId = rf.getLastTweetId(complitefileName)
    else:
        lastTweetId=0
    tweets_list=api.getTweets(keyword,lastTweetId)
    if tweets_list is not None:
        for tweet in tweets_list:
            line = {'text': tweet['text'], 'Id': tweet['Id']}
            output.append(line)
    df = pd.DataFrame(output)
    complitefileName=rf.getCompleteFileName(keyword)
    df.to_csv(complitefileName+'.csv', mode='a', index=True, header=False)