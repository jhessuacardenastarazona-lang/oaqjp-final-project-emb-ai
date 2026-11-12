import json
import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers
    )

    response_data = json.loads(response.text)

    emotion_scores = response_data["emotionPredictions"][0]["emotion"]

    anger_score = emotion_scores["anger"]
    disgust_score = emotion_scores["disgust"]
    fear_score = emotion_scores["fear"]
    joy_score = emotion_scores["joy"]
    sadness_score = emotion_scores["sadness"]

    emotions = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
