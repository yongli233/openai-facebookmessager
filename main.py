import requests
import json
import spacy
import random
from flask import Flask, request

app = Flask(__name__)

# Your OpenAI API key
OPENAI_API_KEY = "YOUR_API_KEY"
# Your Facebook Page Access Token
PAGE_ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"

# OpenAI API URL
OPENAI_API_URL = "https://api.openai.com/v1/answers"

# Facebook Messenger API URL
FB_MESSENGER_URL = "https://graph.facebook.com/v2.6/me/messages"

# Supported languages
SUPPORTED_LANGUAGES = ["en", "es", "fr", "de", "it", "nl"]
LANGUAGE_MODELS = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "fr": "fr_core_news_md",
    "de": "de_core_news_md",
    "it": "it_core_news_md",
    "nl": "nl_core_news_md",
}

nlp = {lang: spacy.load(model) for lang, model in LANGUAGE_MODELS.items()}

RESPONSE_TEMPLATES = {
    "inform": "Here's the information you requested: {response}",
    "question": "Based on your question, here's my answer: {response}",
    "unknown": "I apologize, I do not understand your intent. Can you rephrase your question?",
}

def detect_language(text):
    # Use SpaCy to detect the language of the text
    detected_language = "en"
    max_score = 0
    for lang, nlp_model in nlp.items():
        doc = nlp_model(text)
        if doc._.language["score"] > max_score:
            detected_language = lang
            max_score = doc._.language["score"]
    return detected_language

def openai_query(question, lang="en"):
    response = requests.post(OPENAI_API_URL,
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        data={"question": question, "language": lang}
    )
    return response.json()["answers"][0]

def fb_message(recipient_id, text):
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text}
    }
    response = requests.post(
        FB_MESSENGER_URL,
        params={"access_token": PAGE_ACCESS_TOKEN},
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    return response.json()

def get_response(message_text, sender_id):
    # Detect the language of the message
    lang = detect_language(message_text)

    # Use SpaCy to detect the intent and entities in the message
    doc = nlp[lang](message_text)
    intent = doc.cats["INTENT"]
    entities = [(e.text, e.label_) for e in doc.ents]

    try:
        # Query OpenAI for a response based on the intent
        if intent == "inform":
            response = openai_query(message_text, lang)
            response_text = RESPONSE_TEMPLATES["inform"].format(response=response)
        elif intent == "question":
            question = random.choice(entities)
            response = openai_query(question, lang)
            response_text = RESPONSE_TEMPLATES["question"].format(response=response)
        else:
            response_text = RESPONSE_TEMPLATES["unknown"]
    except Exception as e:
        response_text = f"An error occurred: {e}. Please try again later."

    # Send the response to Facebook Messenger
    fb_message(sender_id, response_text)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the message data
    data = request.get_json()

    # Get the sender ID and message text
    sender_id = data["sender"]["id"]
    message_text = data["message"]["text"]

    # Get a response for the message
    get_response(message_text, sender_id)

    return "ok"

if __name__ == "__main__":
    app.run(debug=True)