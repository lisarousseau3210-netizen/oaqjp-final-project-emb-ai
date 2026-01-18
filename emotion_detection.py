import requests  # Sert à envoyer des messages sur le web
import json      # Sert à lire les réponses de l'IA

def emotion_detector(text_to_analyze):
    # L'adresse de l'IA de Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Le "badge d'accès" exigé par IBM
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # On prépare la phrase que l'utilisateur a tapée
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # On envoie tout ça à Watson
    response = requests.post(url, json=myobj, headers=header)
    
    # On renvoie la réponse brute (on la nettoiera en Task 3)
    return response.text