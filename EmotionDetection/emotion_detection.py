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

    emotions = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if response.status_code == 400:
        return emotions

    response_data = json.loads(response.text)
    emotion_scores = response_data["emotionPredictions"][0]["emotion"]

    emotions["anger"] = emotion_scores["anger"]
    emotions["disgust"] = emotion_scores["disgust"]
    emotions["fear"] = emotion_scores["fear"]
    emotions["joy"] = emotion_scores["joy"]
    emotions["sadness"] = emotion_scores["sadness"]

    emotions_only = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"]
    }

    emotions["dominant_emotion"] = max(
        emotions_only,
        key=emotions_only.get
    )

    return emotions
