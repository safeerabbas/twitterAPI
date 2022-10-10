import pandas as pd
import glob
import os
import time
import readfile as rf

def concatCSVs():
    # setting the path for joining multiple files
    date = time.strftime("%Y%m%d")
    diretorPath=rf.getDirectoryPath()
    files = os.path.join(diretorPath,date+"*"+".csv")

    # list of merged files returned
    files = glob.glob(files)

    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    df.to_csv(diretorPath+'\\'+date+'.csv', mode='a', index=False, header=False)

#concatCSVs()
def concatTweetFiles():
    path ="D:/Python/nlp/twitter API/20220410/"

    # 2. creates list with files to merge based on name convention
    file_list = [path + f for f in os.listdir(path)]

    # 3. creates empty list to include the content of each file converted to pandas DF
    csv_list = []

    # 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
    for file in sorted(file_list):
        csv_list.append(pd.read_csv(file).assign(File_Name=os.path.basename(file)))

    # 5. merges single pandas DFs into a single DF, index is refreshed
    csv_merged = pd.concat(csv_list, ignore_index=True)

    # 6. Single DF is saved to the path in CSV format, without index column
    date = time.strftime("%Y%m%d")
    csv_merged.to_csv(path + date+'.csv', index=False)

concatTweetFiles()

