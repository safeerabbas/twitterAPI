import json

import pandas as pd

cities=[]
areas=[]


addresses=[]
with open('pakistan_areas.json') as f:
    addresses = json.load(f)

# for address in addresses:
#     if(len(address)==3):
#         print(len(address))
#         print(address)


def getLocation(tweet):
    for address in addresses:
        if tweet.find(address["city"].lower()) != -1:
            return address["city"].lower()

def getArea(tweet):
    for address in addresses:
        if(len(address)==3):
            for area in address["area"]:
                if tweet.find(area.lower()) != -1:
                    return area.lower()+", "+address["city"]+", "+address["province"]




#
df=pd.read_csv('CleanedData/cleaneddata.csv')
df=df.head(1000)
df["location"]=df["tweet"].map(getArea)
print(df["location"])