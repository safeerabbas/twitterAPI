import numpy as np
import pandas as pd
import re
stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from"]
stopwords_roman_urdu=[
        "ai", "ayi", "hy", "hai", "main", "ki", "tha", "koi", "ko", "sy", "woh",
        "bhi", "aur", "wo", "yeh", "rha", "hota", "ho", "ga", "ka", "le", "lye",
        "kr", "kar", "lye", "liye", "hotay", "waisay", "gya", "gaya", "kch", "ab",
        "thy", "thay", "houn", "hain", "han", "to", "is", "hi", "jo", "kya", "thi",
        "se", "pe", "phr", "wala", "waisay", "us", "na", "ny", "hun", "rha", "raha",
        "ja", "rahay", "abi", "uski", "ne", "haan", "acha", "nai", "sent", "photo",
        "you", "kafi", "gai", "rhy", "kuch", "jata", "aye", "ya", "dono", "hoa",
        "aese", "de", "wohi", "jati", "jb", "krta", "lg", "rahi", "hui", "karna",
        "krna", "gi", "hova", "yehi", "jana", "jye", "chal", "mil", "tu", "hum", "par",
        "hay", "kis", "sb", "gy", "dain", "krny", "tou","k"
    ]

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

def removeStopWord_map(tweet):
    if type(tweet) == np.float:
        return ""
    temp = tweet.split()
    temp = [w for w in temp if not w in stopwords_roman_urdu]
    temp = " ".join(word for word in temp)
    return temp

def basicTweetCleaning(file):
    df=pd.read_csv(file)
    df = df.iloc[:, 1].map(clean_tweet)
    #df['tweet']=df['tweet'].map(clean_tweet)
    df.to_csv('./CleanedData/20220622darna-clean.csv',index=False)

def removeRowWithMissingValue(file):
    df = pd.read_csv(file)
    df = df.iloc[:, 1].map(clean_tweet)
    df.replace('', np.nan, inplace=True)
    df.dropna(subset=['tweet'], inplace=True)
    df.to_csv('cleanWithMissingValue.csv',index=False)


def removeStopWord(file):
    df=pd.read_csv(file)
    df = df.iloc[:, 0].map(removeStopWord_map)
    #df['tweet']=df['tweet'].map(removeStopWord_map)
    df.to_csv('removeStopWord.csv',index=False)



#basicTweetCleaning()
#removeRowWithMissingValue('basicTweetCleaning.csv')
#removeStopWord('cleanWithMissingValue.csv')



def removeFloatValues():
    df = pd.read_csv('cleanWithMissingValue.csv')
    df['tweet'] = df.apply(lambda r: r['tweet'] if type(r['tweet'])==str else np.nan, axis=1)
    df.dropna(inplace=True)
    df['tweet'].str.strip()
    df.to_csv('cleanFloattweets.csv', index=False)
#removeFloatValues()

tweets = [
    "Get ready for #NatGeoEarthDay! Join us on 4/21 for an evening of music and celebration, exploration and inspiration https://on.natgeo.com/3t0wzQy.",
    "Coral in the shallows of Aitutaki Lagoon, Cook Islands, Polynesia https://on.natgeo.com/3gkgq4Z",
    "Don't miss our @reddit AMA with author and climber Mark Synnott who will be answering your questions about his historic journey to the North Face of Everest TODAY at 12:00pm ET! Start submitting your questions here: https://on.natgeo.com/3ddSkHk @DuttonBooks"]

#results = [clean_tweet(tw) for tw in tweets]
#print(results)
a='safeer'
print(type(a))
# df=pd.read_csv('cleanFloattweets.csv')
# df['tweet']=df['tweet'].str.strip()
# #df.loc[:, ['A', 'B']]
# df=df.iloc[:,[1]]
# df.to_csv('tweettext.csv', index=False)


basicTweetCleaning("D:\\Python\\nlp\\twitter API\\20220622\\20220622darna.csv")


