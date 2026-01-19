import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyse le texte et gère les erreurs de saisie vide (Code 400).
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # --- GESTION D'ERREUR (TASK 7) ---
    # Si le statut est 400, on renvoie un dictionnaire rempli de None
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # --- TRAITEMENT SI RÉUSSITE (STATUS 200) ---
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Recherche de l'émotion dominante
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }