import pandas as pd
import os
import time

def getLastTweetId(file):
    df=pd.read_csv(file)
    bottom = df.tail(1)
    return bottom.columns[2]
#
keywordlist= ['jaloos','jalus','jalos','jalsa','ehtejaj','ahtjaj' ,'ehtijaj','ehtajaj','dharna','darna','sit in','protest']
for keyword in keywordlist:
    date=time.strftime("%Y%m%d")
    directory=os.getcwd()
    filePath=directory+"\\"+date+keyword
    print(filePath)
# os.path.isdir(os.getcwd()+""+time.strftime("%Y%m%d"))

def getDirectoryPath():
    directory=os.getcwd()
    date = time.strftime("%Y%m%d")
    diretorPath=directory+"\\"+date
    isExit=os.path.isdir(diretorPath)
    if(isExit==False):
        os.makedirs(diretorPath)
    return diretorPath

def getCompleteFileName(keyword):
    fileName = time.strftime("%Y%m%d")+keyword
    directoryPath = getDirectoryPath()
    complitefileName = directoryPath + "\\" + fileName
    return complitefileName
#D:\Python\nlp\twitter API\20220410