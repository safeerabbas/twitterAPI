
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
#from wordcloud import WordCloud
#Importing Dataset
df = pd.read_csv("android-games.csv")
#Checking the Data
df.head()
#Checking for NaN values
df.isna().sum()
#Removing NaN Values
#df.dropna(inplace = True)
#Creating the text variable
text = " ".join(cat.split()[1] for cat in df.category)
# Creating word_cloud with text as argument in .generate() method
#word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
# Display the generated Word Cloud
#plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
