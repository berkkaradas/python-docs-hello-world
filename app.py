from flask import Flask
app = Flask(__name__)

@app.route("/")
pip install azure-ai-textanalytics

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("dc15ce3d9f5b43578eea933f1c609939")
endpoint="https://cognitive363.cognitiveservices.azure.com/"

text_analytics_client = TextAnalyticsClient(endpoint, credential)

print("pls type your input")
input1=input()

#Burada datayı işleyelim
documents = [
    input1
    #"The food was yummy. :)"
    #"room was clean"
]

response = text_analytics_client.detect_language(documents)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print("Language detected: {}".format(doc.primary_language.name))
    print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
    print("Confidence score: {}\n".format(doc.primary_language.confidence_score))

response = text_analytics_client.analyze_sentiment(documents, language=doc.primary_language.iso6391_name)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))

