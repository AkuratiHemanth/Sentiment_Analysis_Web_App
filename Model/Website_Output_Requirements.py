from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    sentiment_score = analysis.sentiment.polarity
    return sentiment_score

def label_sentiment(sentiment_score):
    if sentiment_score < -0.05:
        return "negative"
    if sentiment_score > 0.35:
        return "positive"
    return "neutral"

def generate_wordcloud(text):
    wc = WordCloud(max_words=1000, width=800, height=400, collocations=False, background_color=None).generate(text)
    plt.figure(figsize=(8, 4))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    image_path = "static/wordcloud.png"
    plt.savefig(image_path, transparent=True)  
    plt.close()
    return image_path


