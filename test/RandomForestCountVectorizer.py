import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#file reading
df=pd.read_csv('sentiment.csv', encoding='cp1252')
docs = df['tweet']
labels=df['Sentiment']

coun_vect = CountVectorizer()
count_matrix = coun_vect.fit_transform(df['tweet'].values.astype('U'))
count_array = count_matrix.toarray()


X_train, X_test, y_train, y_test = train_test_split(count_array, labels, test_size=0.2, random_state=0)

text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)

predictions = text_classifier.predict(X_test)
print('---------------------------------RandomForest CountVectorizer    -----------------------------------')
print('---------------------------------confusion_matrix-----------------------------------')
print(confusion_matrix(y_test,predictions))
print('---------------------------------classification_report-----------------------------------')
print(classification_report(y_test,predictions))
print('---------------------------------accuracy_score-----------------------------------')
print(accuracy_score(y_test, predictions))

#print(count_matrix.toarray())
#print(y_test.shape)
#print(y_train.shape)
#print(X_train.shape)
#print(X_test.shape)




#print(docs.head(5))
#print(label.head(5))
