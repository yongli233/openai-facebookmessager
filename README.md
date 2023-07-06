Facebook Messenger Chatbot with OpenAI as backend

This code implements a Facebook Messenger chatbot that uses OpenAI's API to generate responses. It includes the following features:

    Language detection using SpaCy
    Intent detection and entity extraction using SpaCy
    Querying OpenAI for responses based on the detected intent (inform, question, unknown)
    Random entity selection for questions
    Error handling
    Support for multiple languages (English, Spanish, French, German, Italian, Dutch)

Setup

Setting up the project:

    Clone this repository

    Obtain OpenAI API keys for your desired languages and add them to OPENAI_API_KEY

    Obtain a Facebook Page Access Token for your page and add it to PAGE_ACCESS_TOKEN

    Run pip install -r requirements.txt to install dependencies

    Run flask run to start the Flask server locally

    Set up a webhook for your Facebook page pointing to {your_server}/webhook

    Your chatbot will now respond to user messages on Messenger!

Customizing Responses

The response templates in RESPONSE_TEMPLATES can be modified as needed. Additional templates can be added for new intents.

The OpenAI API call made for each intent can also be customized by editing the openai_query() function.
Additional Features

Some possible additions to the chatbot include:

    Caching OpenAI responses to reduce API calls
    Storing user context/conversation state
    Handling user personal information and slot-filling
