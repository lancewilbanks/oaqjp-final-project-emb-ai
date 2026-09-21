import json
import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 400:
        anger_score = None
        disgust_score = None  
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    else:
        formatted_txt = json.loads(response.text)

        emotion_dict = formatted_txt['emotionPredictions'][0]['emotion']    
    
        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust']  
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }    
