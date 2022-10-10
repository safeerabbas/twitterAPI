import json

import pandas as pd

cities=[]
areas=[]


def getCitytown(tweet):
    temp = tweet.split()
    temp = [w for w in temp if w in cities]
    temp = " ".join(word for word in temp)
    print(temp)
    return temp
#getCity(tweet)

address=[]
with open('pakistan_areas.json') as f:
    address = json.load(f)

def getCityTown(tweet):
    temp = tweet.split()
    findTown =[]
    foundCity = []
    for keyword in temp:
        for item in address:
            try:
                city = item["city"]
                if (city.lower() == keyword.lower()):
                    foundCity.append(city.lower())
                area=item["area"]
                if(len(area)>=1):
                    for a in area:
                        if(a.lower()==keyword.lower()):
                            findTown.append(a.lower())
            except:
                pass
    foundAddress = {
        'city':foundCity,
        'area':findTown
        }
    return foundAddress

def getCity(tweet):
    temp = tweet.split()
    foundCity = []
    for keyword in temp:
        for item in address:
            try:
                city = item["city"]
                if (city.lower() == keyword.lower()):
                        foundCity.append(city.lower())
            except:
                pass
    return foundCity


tweet='join tomorrow protest at 2 30 pm saturday  be Wazirabad voice Karachi Zhob of hafeez baloch at Abbottabad'
# a=getCityTown(tweet)
# print(a)

import numpy as np
df=pd.read_csv('CleanedData/cleaneddata.csv')
df=df.head(10)

searchfor = ['wazirabad', 'karachi','zhob','abbottabad']
# df=df[df['tweet'].str.contains('|'.join(searchfor),regex=True)]


# s1 = pd.Series(['i', 'live', 'in', 'karachi','and','work','in','wazirabad', np.NaN])

#df=s1.str.contains('|'.join(searchfor),regex=True)
# print(df.head(10))


tweet='join tomorrow protest at 2 30 pm saturday  be wazirabad town voice karachi zhob of hafeez baloch at abbottabad'
searchfor = ['wazirabad town', 'karachi','zhob','multan']
def getCityContains(tweet):
    for item in searchfor:
        try:
            if tweet.find(item) != -1:
                return item
        except:
            pass
for tweet in df:
    print(tweet)
    item=getCityContains(tweet)
    print(item)
# for i in range(1,10):
#     getCityContains
#






