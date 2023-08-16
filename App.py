from flask import Flask, render_template, request
from Model.Website_Output_Requirements import label_sentiment, generate_wordcloud

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    wordcloud_img = None

    if request.method == "POST":
        user_tweet = request.form["user_tweet"]
        
        sentiment_score = analyze_sentiment(user_tweet)
        sentiment_result = label_sentiment(sentiment_score)

        wordcloud_img = generate_wordcloud(user_tweet)

    return render_template("index.html",
                           sentiment_result=sentiment_result,
                           wordcloud_img=wordcloud_img)

if __name__ == "__main__":
    app.run(debug=True)

