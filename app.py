from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Ömer Berk Karadaş ,Ece Akçiçek ,İsmet Sarı,Yağmur "
