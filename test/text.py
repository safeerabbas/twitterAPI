import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
#file reading
#df=pd.read_csv('sentiment1.csv')
df=pd.read_csv('sentiment1.csv', encoding='cp1252')
labels=df['Sentiment']

print(df.head())
print(df.shape)