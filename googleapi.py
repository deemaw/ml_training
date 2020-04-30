import logging
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def gcp_nlp(text):
    logging.info("gcpNLP function")
    logging.info(text)
    # Create a client to access GCP
    client = language.LanguageServiceClient()

    # Testing text(Ignore the language)
    document = language.types.Document(content=text,type='PLAIN_TEXT',)

    # Getting the response for sentiment analysis
    response = client.analyze_sentiment(document=document,encoding_type='UTF32',)

    # Getting respective sentment values
    sentiment = response.document_sentiment

    return sentiment


