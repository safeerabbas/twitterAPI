from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer



df=pd.read_csv('sentiment.csv', encoding='cp1252')
docs = df['tweet']
labels=df['Sentiment']


coun_vect = TfidfVectorizer()
count_matrix = coun_vect.fit_transform(df['tweet'].values.astype('U'))
count_array = count_matrix.toarray()

X_train, X_test, y_train, y_test = train_test_split(count_array, labels, test_size=0.2, random_state=0)

text_classifier = MultinomialNB()
text_classifier.fit(X_train, y_train)


predictions = text_classifier.predict(X_test)

print('---------------------------------MultinomialNB TFIDF-----------------------------------')
print('---------------------------------confusion_matrix-----------------------------------')
print(confusion_matrix(y_test,predictions))
print('---------------------------------classification_report-----------------------------------')
print(classification_report(y_test,predictions))
print('---------------------------------accuracy_score-----------------------------------')
print(accuracy_score(y_test, predictions))
