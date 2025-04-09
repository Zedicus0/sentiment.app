#MAKE NEW PROJECT NAMED sentiment-app
#RIGHT CLICK WHERE IT SAYS sentiment-app UNDER PROJECT CLICK NEW, CLICK FILE NAME IT app.py
#INSTALL flask textblob and gunicorn IN THE TERMINAL
#OPEN sentiment-app FOLDER IN FILE EXPLORER
#OPEN NOTEPAD SAVE IT TO DOWNLOADS, NAME IT requirements.txt THEN COPY IT FROM DOWNLOADS INTO THE sentiment-app FOLDER IN FILE EXPLORER
#RIGHT CLICK IN THE sentiment-app FOLDER AND CLICK NEW>FOLDER NAME IT templates
#IN THE FOLDER TEMPLATES CREATE A NEW NOTEPAD FILE NAMED index.html
#COPY AND PASTE THIS CODE INTO index.html
#<!DOCTYPE html>
#<html lang="en">
#<head>
#    <meta charset="UTF-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Sentiment Analysis</title>
#</head>
#<body>
#    <h1>Sentiment Analysis App</h1>
#    <form method="POST">
#        <textarea name="text" rows="4" cols="50" placeholder="Enter your text here"></textarea><br>
#        <button type="submit">Analyze</button>
#    </form>
#    {% if result %}
#        <h2>Result: {{ result }}</h2>
#    {% endif %}
#</body>
#</html>
# OBVIOUSLY REMOVE THE #'S IN THE INDEX FILE
#NOW SAVE THE FILE AND CLOSE IT
#COPY CODE CODE BELOW FROM THE Module 11 - Creation and Deployment of Sentiment Analysis Guide FILE FROM MODULE 11
# THEN RUN IF EVERYTHING WENT WELL THERE SHOULD BE TWO LINKS TO CLICK ON,
# CLICK ON ONE OF THEM, IF A WINDOW ON A SEARCH ENGINGE POPS  UP
# WITH A TEXT WINDOW THAT ALLOWS YOU TO TYPE IN THEN YOUVE DONE GOOD
# NOW REOPEN requirements.txt  AND TYPE
# Flask
# gunicorn
# textblob
#THEN SAVE AND CLOSE
# NOW OPEN GITHUB SIGN IN HIT THE PLUS SIGN AND CREATE A NEW REPOSITORY
#NAME IT sentiment.app
#NOW TYPE cmd INTO YOUR SEARCH BAR AT THE BOTTOM TO OPEN THE COMMAND PROMPT
#OPEN NOTE PAD AND COPY THE PATH FOR sentiment.app IN THE FILE EXPLORER IT SHOULD
#LOOK LIKE THIS: cd C:\Users\shams\PycharmProjects\sentiment-app
#RUN IT THEN TYPE git init
#git add .
#git commit -m "first commit"
#IN ORDER
# IF THIS DOES NOT WORK DOWNLOAD THE GITHUB APP ITS A LITTLE UNSTABLE
#IF THIS WORKED TYPE THIS git remote add origin https://github.com/YOUR_USERNAME/sentiment-app.git
#I ASSUME REPLACE YOUR_USERNAME WITH YOUR ACTUAL USERNAME




# THIS CODE BELOW IS THE CODE FROM MODULE 11
from flask import Flask, request, render_template, jsonify
from textblob import TextBlob

app = Flask(__name__)


# Sentiment analysis function
def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "Happy 😀"
    elif sentiment_score < 0:
        return "Sad 😢"
    else:
        return "Neutral 😐"


# Homepage route (for rendering the web form)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)  # Use our function
        return render_template("index.html", result=result)
    return render_template("index.html", result="")


# API route for JSON requests
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400  # Error if no text

    text = data["text"]
    sentiment = analyze_sentiment(text)  # Use our function

    return jsonify({"sentiment": sentiment})  # Return JSON response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)  # Running with debug mode
