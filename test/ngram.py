import pandas as pd
from nltk.corpus import stopwords
import nltk
from nltk.probability import FreqDist

#nltk.download('punkt')
df=pd.read_csv('sentiment.csv')
docs = df['tweet']

all_words = ' '.join([word for word in df['tweet']])
#tokenized_words = nltk.tokenize.word_tokenize(all_words)
#fdist = FreqDist(tokenized_words)
#print(fdist)



import matplotlib.pyplot as plt
from wordcloud import WordCloud

wordcloud = WordCloud(width=600,
                     height=400,
                     random_state=2,
                     max_font_size=100).generate(all_words)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis('off');


wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=10).generate(all_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()






def generate_N_grams(text,ngram=1):
  words=[word for word in text.split(" ")]
  print("Sentence after removing stopwords:",words)
  temp=zip(*[words[i:] for i in range(0,ngram)])
  ans=[' '.join(ngram) for ngram in temp]
  return ans


#ngram=generate_N_grams(all_words,3)
#print(ngram)