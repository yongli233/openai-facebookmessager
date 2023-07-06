## ****Facebook Messenger Chatbot with OpenAI as backend****

This code implements a Facebook Messenger chatbot that uses OpenAI's API to generate responses. It includes the following features:

Language detection using SpaCy
Intent detection and entity extraction using SpaCy
Querying OpenAI for responses based on the detected intent (inform, question, unknown)
Random entity selection for questions
Error handling
Support for multiple languages (English, Spanish, French, German, Italian, Dutch)

## Setup

#### Prerequisites:
1. [Download and install Python](https://www.python.org/downloads/) (Version 3.x is recommended).

#### Setting up the project:
1. Clone the GitHub repository: 
```
git clone https://github.com/yongli233/openai-facebookmessager
```
2. Navigate to the project directory:
```
cd openai-facebookmessager
```
3. Obtain OpenAI API keys for your desired languages and add them to OPENAI_API_KEY in main.py
```
OPENAI_API_KEY = "YOUR_API_KEY"
```
4. Obtain a Facebook Page Access Token for your page and add it to PAGE_ACCESS_TOKEN:
```
PAGE_ACCESS_TOKEN = "YOUR_PAGE_ACCESS_TOKEN"
```  
5. Install the required Python packages from `requirements.txt`:
```
pip install -r requirements.txt
```

## Customizing Responses

The response templates in RESPONSE_TEMPLATES can be modified as needed. Additional templates can be added for new intents.

The OpenAI API call made for each intent can also be customized by editing the openai_query() function.
Additional Features

1. Caching OpenAI responses to reduce API calls
2. Storing user context/conversation state
3. Handling user personal information and slot-filling

## Copyright:

This program is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)
