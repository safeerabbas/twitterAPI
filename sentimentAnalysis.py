from textblob import TextBlob
import pandas as pd

def getPolarity(text):
    if (type(text)==str):
        return TextBlob(text).sentiment.polarity

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getAnalysis(score):
    if score<0:
        return 'Negative'
    elif score==0:
        return 'Neutral'
    else:
        return 'Positive'

def applySubjectivityPolarity(file):
    df=pd.read_csv(file)
    df["Subjectivity"]=df["tweet"].map(getSubjectivity)
    df["Polarity"]=df["tweet"].map(getPolarity)
    #df["Sentiment"]=df["Polarity"].map(getSubjectivity)
    df.to_csv('polarity.csv')
def applySentiment(file):
    df=pd.read_csv(file)
    df["Sentiment"]=df["Polarity"].map(getSubjectivity)
    df.to_csv('sentiment.csv')

applySubjectivityPolarity('CleanedData/cleaneddata.csv')
applySentiment('polarity.csv')

