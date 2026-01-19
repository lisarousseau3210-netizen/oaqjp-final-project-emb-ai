from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # On récupère le texte que l'utilisateur a tapé dans la boîte sur le site
    text_to_analyze = request.args.get('textToAnalyze')

    # On utilise ta fonction de la Task 3
    response = emotion_detector(text_to_analyze)

    # Si l'IA ne renvoie rien (erreur), on affiche un message d'erreur
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Sinon, on affiche le résultat joliment
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    # Cette route affiche simplement ta page d'accueil HTML
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)