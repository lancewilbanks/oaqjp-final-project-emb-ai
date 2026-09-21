"""
This module detects emotions from a text input.

The server.py handles requests and serves API endpoints.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    The sent_detector function GETs the customer comment
    and feeds it to the emotion_detctor function which 
    returns the emotion scores and the dominant emtion.

    Return: An output message of the emotion scores
    and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    output_txt = f"""For the given statement, the system response is
    'anger': {response['anger']}, 
    'disgust': {response['disgust']}, 
    'fear': {response['fear']}, 
    'joy': {response['joy']} 
    and 'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."""

    return output_txt

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
