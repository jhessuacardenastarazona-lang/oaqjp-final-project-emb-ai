import json
from urllib.request import Request, urlopen


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    request_data = json.dumps(input_json).encode("utf-8")
    request = Request(
        url,
        data=request_data,
        headers=headers,
        method="POST"
    )

    with urlopen(request) as response:
        return response.read().decode("utf-8")
