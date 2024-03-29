import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

import csv

df = pd.read_csv('/content/adipurush_tweets.csv')

df

df.shape

df.columns

df.duplicated().sum()

df = df.drop_duplicates()

df.isnull().sum()

df = df.drop('Source of Tweet', axis = 1)

df

df.info()

df.describe()

df.nunique()

df_sorted = df.sort_values(by='Number of Likes', ascending=False)

df_sorted.head(10)

df['Date Created'] = pd.to_datetime(df['Date Created'])

df

df_sorted_date = df.sort_values('Date Created')
plt.figure(figsize=[15,7])
plt.plot(df_sorted_date['Date Created'],df_sorted_date['Number of Likes'])
plt.xlabel('Date Created')
plt.ylabel('Number of Likes')
plt.title('Number of Likes over Time')
plt.show()

plt.figure(figsize=[15,7])
plt.scatter(df_sorted_date['Date Created'],df_sorted_date['Number of Likes'])
plt.xlabel('Date Created')
plt.ylabel('Number of Likes')
plt.title('Number of Likes over Time')
plt.show()

import plotly.express as px

fig = px.scatter(df_sorted_date, x='Date Created', y='Number of Likes', title = 'Number of Likes over Time')
fig.update_layout(xaxis=dict(title='Date Created'),yaxis=dict(title='Number of Likes'))
fig.show()

import re
import string
from tqdm.notebook import tqdm
from datetime import datetime
import dateutil.parser

pip install spellchecker

pip install spellchecker nltk langdetect

pip uninstall spellchecker nltk langdetect

pip install spellchecker nltk==3.6.2 langdetect==1.0.9

import nltk
from spellchecker import SpellChecker
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

pip install pyenchant

from wordcloud import WordCloud, ImageColorGenerator
from nltk.corpus import stopwords
import random

nltk.download('vader_lexicon')
nltk.download('stopwords')

languages = stopwords.fileids()

print("Number of supported languages:", len(languages))


print("Supported languages:", languages)

from nltk.tokenize import TweetTokenizer

english_stopwords = stopwords.words('english')
hinglish_stopwords = stopwords.words('hinglish')

def clean_tweet(tweet):

    tweet = re.sub(r"http\S+|www\S+|@\w+|#\w+", "", tweet)
    tweet = re.sub(r"[^\w\s]", "", tweet)

    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    tokens = tokenizer.tokenize(tweet)

    tokens = [token for token in tokens if token not in english_stopwords and token not in hinglish_stopwords]

    tokens = [token.translate(str.maketrans('', '', string.punctuation)) for token in tokens]
    tokens = [token.lower() for token in tokens]

    cleaned_tweet = ' '.join(tokens)

    return cleaned_tweet

df['Cleaned_Tweets'] = df['Tweets'].apply(clean_tweet)

df

pip install pyspellchecker

def clean_text(text):
    text = text.lower()
    return text.strip()

df.Cleaned_Tweets = df.Cleaned_Tweets.apply(lambda x: clean_text(x))

def tokenization(text):
    tokens = re.split('W+',text)
    return tokens

df.Cleaned_Tweets = df.Cleaned_Tweets.apply(lambda x: tokenization(x))

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

nltk.download('wordnet')

nltk.download('omw-1.4')

def lemmatizer(text):
    lemm_text = "".join([wordnet_lemmatizer.lemmatize(word) for word in text])
    return lemm_text

df.Cleaned_Tweets = df.Cleaned_Tweets.apply(lambda x: lemmatizer(x))

def remove_digits(text):
    clean_text = re.sub(r"\b[0-9]+\b\s*", "", text)
    return(text)

df.Cleaned_Tweets = df.Cleaned_Tweets.apply(lambda x: remove_digits(x))

def remove_digits1(sample_text):
    clean_text = " ".join([w for w in sample_text.split() if not w.isdigit()])
    return(clean_text)

df.Cleaned_Tweets = df.Cleaned_Tweets.apply(lambda x: remove_digits1(x))

pip install langdetect

from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return None

df['Language'] = df['Cleaned_Tweets'].apply(detect_language)

df

df1 = df.copy()

df1['english_tweets'] = df[df['Language'] == 'en']['Cleaned_Tweets']

df1

df1 = df1.dropna()

df1

df1['Year'] = df1['Date Created'].dt.year
df1['Month'] = df1['Date Created'].dt.month
df1['Day'] = df1['Date Created'].dt.day

df1

df1.nunique()

df1['Time'] = df1['Date Created'].dt.time

df1['Tweet_Length'] = df1['english_tweets'].str.len()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=[15,7])
plt.title('Count Plot for Day')
sns.countplot(x='Day', data=df1, palette='hls')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(15, 6))
counts = df1['Day'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=sns.color_palette('hls'))
plt.title('Day')
plt.show()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(x=df1['Day'].value_counts().index, y=df1['Day'].value_counts())])
fig.update_layout(
        title= 'Day',
        xaxis_title="Categories",
        yaxis_title="Count"
    )
fig.show()

counts = df1['Day'].value_counts()
fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts)])
fig.update_layout(title= 'Day')
fig.show()

plt.figure(figsize=(15,6))
sns.histplot(df1['Tweet_Length'], kde = True, bins = 5, palette = 'hls')
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(15, 6))
sns.boxplot(x=df1['Tweet_Length'], data = df,palette='hls')
plt.xticks(rotation=90)
plt.show()

import plotly.express as px

fig = px.histogram(df1, x='Tweet_Length', nbins=20, histnorm='probability density')
fig.update_layout(title=f"Histogram of Tweet Length", xaxis_title='Tweet Length', yaxis_title="Probability Density")
fig.show()

fig = px.box(df1, y='Tweet_Length')
fig.update_layout(title=f"Box Plot of Tweet Length", yaxis_title='Tweet_Length')
fig.show()

import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def label_sentiment(x:float):
    if x < -0.05 : return 'negative'
    if x > 0.35 : return 'positive'
    return 'neutral'

sia = SIA()

df1['sentiment'] = [sia.polarity_scores(x)['compound'] for x in tqdm(df1['english_tweets'])]
df1['overall_sentiment'] = df1['sentiment'].apply(label_sentiment);

df1

import pandas as pd

df1 = pd.DataFrame(df1)


df1.to_csv('df1.csv', index=False)

df1['overall_sentiment'].unique()

df1['overall_sentiment'].value_counts()

plt.figure(figsize=(15, 6))
sns.countplot(x='overall_sentiment', data=df1, palette='hls')
plt.xticks(rotation=0)
plt.show()

label_data = df1['overall_sentiment'].value_counts()

explode = (0.1, 0.1, 0.1)
plt.figure(figsize=(14, 10))
patches, texts, pcts = plt.pie(label_data,
                               labels = label_data.index,
                               colors = ['blue', 'red', 'green'],
                               pctdistance = 0.65,
                               shadow = True,
                               startangle = 90,
                               explode = explode,
                               autopct = '%1.1f%%',
                               textprops={ 'fontsize': 25,
                                           'color': 'black',
                                           'weight': 'bold',
                                           'family': 'serif' })
plt.setp(pcts, color='white')

hfont = {'fontname':'serif', 'weight': 'bold'}
plt.title('Label', size=20, **hfont)

centre_circle = plt.Circle((0,0),0.40,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.show()

fig = go.Figure(data=[go.Bar(x=df1['overall_sentiment'].value_counts().index, y=df1['overall_sentiment'].value_counts())])
fig.update_layout(
        title= 'Overall Sentiment',
        xaxis_title="Categories",
        yaxis_title="Count"
    )
fig.show()

counts = df1['overall_sentiment'].value_counts()
fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts)])
fig.update_layout(title= 'Overall Sentiment')
fig.show()

df1

df2 = df1[['english_tweets', 'overall_sentiment']]

df2

def clean_text(text):

    cleaned_text = re.sub('[^a-zA-Z]', ' ', text).lower()

    cleaned_text = re.sub('\s+', ' ', cleaned_text).strip()

    words = cleaned_text.split()

    cleaned_text = ' '.join(words)
    return cleaned_text

df2['Cleaned_English_Tweets'] = df2['english_tweets'].apply(clean_text)

df2

df3 = df2[['Cleaned_English_Tweets', 'overall_sentiment']]

df3

non_meaningful_words = ['cr', 'amp', 'rs', 'u', 'l']

def remove_non_meaningful_words(text):
    tokens = text.split()
    filtered_tokens = [token for token in tokens if token not in non_meaningful_words]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

df3['Cleaned_English_Tweets'] = df3['Cleaned_English_Tweets'].apply(remove_non_meaningful_words)

import wordcloud

from wordcloud import WordCloud
data = df3['Cleaned_English_Tweets']
plt.figure(figsize = (20,20))
wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,
               collocations=False).generate(" ".join(data))
plt.imshow(wc)
plt.axis('off')
plt.show()

data = df3[df3['overall_sentiment']=="positive"]['Cleaned_English_Tweets']
plt.figure(figsize = (20,20))
wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,
               collocations=False).generate(" ".join(data))
plt.imshow(wc)
plt.axis('off')
plt.show()

"""from PIL import Image
import numpy as np
data = df3[df3['overall_sentiment'] == "positive"]['Cleaned_English_Tweets']
text = " ".join(data)
wordcloud = WordCloud(max_words=1000, width=1600, height=800, collocations=False).generate(text)
image = wordcloud.to_image()
image_array = np.array(image)
fig = go.Figure(data=go.Image(z=image_array))
fig.update_layout(title_text="Word Cloud - Positive Tweets", width=800, height=600)
fig.show()
"""

data = df3[df3['overall_sentiment']=="negative"]['Cleaned_English_Tweets']
plt.figure(figsize = (20,20))
wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,
               collocations=False).generate(" ".join(data))
plt.imshow(wc)
plt.axis('off')
plt.show()

"""from PIL import Image
import numpy as np
data = df3[df3['overall_sentiment'] == "negative"]['Cleaned_English_Tweets']
text = " ".join(data)
wordcloud = WordCloud(max_words=1000, width=1600, height=800, collocations=False).generate(text)
image = wordcloud.to_image()
image_array = np.array(image)
fig = go.Figure(data=go.Image(z=image_array))
fig.update_layout(title_text="Word Cloud - Negative Tweets", width=800, height=600)
fig.show()
"""

data = df3[df3['overall_sentiment']=="neutral"]['Cleaned_English_Tweets']
plt.figure(figsize = (20,20))
wc = WordCloud(max_words = 1000 , width = 1600 , height = 800,
               collocations=False).generate(" ".join(data))
plt.imshow(wc)
plt.axis('off')
plt.show()

"""import numpy as np
data = df3[df3['overall_sentiment'] == "neutral"]['Cleaned_English_Tweets']
text = " ".join(data)
wordcloud = WordCloud(max_words=1000, width=1600, height=800, collocations=False).generate(text)
image = wordcloud.to_image()
image_array = np.array(image)
fig = go.Figure(data=go.Image(z=image_array))
fig.update_layout(title_text="Word Cloud - Neutral Tweets", width=800, height=600)
fig.show()
"""

df3

x = df3['Cleaned_English_Tweets']
y = df3['overall_sentiment']

print(len(x), len(y))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
print(len(x_train), len(y_train))
print(len(x_test), len(y_test))

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()
vect.fit(x_train)

x_train_dtm = vect.transform(x_train)
x_test_dtm = vect.transform(x_test)

vect_tunned = CountVectorizer(stop_words='english', ngram_range=(1,2), min_df=0.1, max_df=0.7, max_features=100)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()

tfidf_transformer.fit(x_train_dtm)
x_train_tfidf = tfidf_transformer.transform(x_train_dtm)

x_train_tfidf

texts = df3['Cleaned_English_Tweets']
target = df3['overall_sentiment']

from keras.preprocessing.text import Tokenizer

word_tokenizer = Tokenizer()
word_tokenizer.fit_on_texts(texts)

vocab_length = len(word_tokenizer.word_index) + 1
vocab_length

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')

def embed(corpus):
    return word_tokenizer.texts_to_sequences(corpus)

longest_train = max(texts, key=lambda sentence: len(word_tokenize(sentence)))
length_long_sentence = len(word_tokenize(longest_train))

train_padded_sentences = pad_sequences(
    embed(texts),
    length_long_sentence,
    padding='post'
)

train_padded_sentences

import numpy as np

embeddings_dictionary = dict()
embedding_dim = 100


with open('glove.6B.100d.txt', encoding="utf8") as fp:
    for line in fp.readlines():
        records = line.split()
        word = records[0]
        vector_dimensions = np.asarray(records[1:], dtype='float32')
        embeddings_dictionary [word] = vector_dimensions

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

nb.fit(x_train_dtm, y_train)

y_pred_class = nb.predict(x_test_dtm)
y_pred_prob = nb.predict_proba(x_test_dtm)[:, 1]

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_class))

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

pipe = Pipeline([('bow', CountVectorizer()),
                 ('tfid', TfidfTransformer()),
                 ('model', MultinomialNB())])

pipe.fit(x_train, y_train)

y_pred_class = pipe.predict(x_test)

print(metrics.accuracy_score(y_test, y_pred_class))

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

import xgboost as xgb

pipe = Pipeline([
    ('bow', CountVectorizer()),
    ('tfid', TfidfTransformer()),
    ('model', xgb.XGBClassifier(
        learning_rate=0.1,
        max_depth=7,
        n_estimators=80,
        use_label_encoder=False,
        eval_metric='auc',
    ))
])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, y_pred)
print('Test accuracy:', acc)
