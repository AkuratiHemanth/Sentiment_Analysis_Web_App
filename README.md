**# Sentiment Analysis Web App :speech_balloon: :bar_chart:**

Welcome to the **Sentiment Analysis Web App**! This project allows users to input sentences or tweets and receive an analysis of their sentiment. The app classifies the input as positive, negative, or neutral and displays corresponding graphics.

**## :computer: Technologies Used**

- Python
- Flask (for creating the web app)
- Machine Learning Model (for sentiment analysis)
- HTML/CSS (for front-end)

**## :art: Screenshots**

![Web App Screenshot]![Screenshot (531)](https://github.com/AkuratiHemanth/Sentiment_Analysis_Web_App/assets/129819031/ad716039-b81b-42c6-9d6f-f346ceaf390c)

**## :rocket: How to Use**

1. Clone this repository to your local machine.
2. Set up a virtual environment and install the required dependencies using `pip install flask textblob wordcloud`.
3. Run the Flask app using `python app.py`.
4. Open your web browser and go to `http://localhost:5000`.
5. Enter a sentence or tweet and see the sentiment analysis results!

   ![ML - Success-Kid](https://github.com/AkuratiHemanth/Sentiment_Analysis_Web_App/assets/129819031/38aeb304-d3e9-49ca-8264-42d287884af3)


**## :bulb: Model Details**

The sentiment analysis model classifies input sentences into three categories: positive, negative, and neutral. The classification is based on a threshold-based approach:

- Sentences with polarity < -0.05 are classified as **negative**.
- Sentences with polarity > 0.35 are classified as **positive**.
- Sentences in between are classified as **neutral**.

**## :chart_with_upwards_trend: Results**

The app displays the sentiment analysis result along with an appropriate emoji and corresponding images to enhance the user experience.

To have a look into the model of Sentimental Analysis based on the tweets of **Adipurush Movie**, you can have a look into the following link: https://github.com/AkuratiHemanth/Emotion_Insights_Adipurush_Movie

![ml-Pepperidge-Farm-Remembers](https://github.com/AkuratiHemanth/Sentiment_Analysis_Web_App/assets/129819031/c3c1388e-1e88-4257-8d11-104fa0aa00a4)

To know more about the Machine Learning Techniques: https://github.com/AkuratiHemanth/Machine_Learning_Model_Implementation_Steps

Feel free to contribute and improve the project by submitting pull requests! :sparkles:

---

**Developed by :heart: Akurati Hemanth**

