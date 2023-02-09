import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json
app = Flask("Web Translator")

@app.route("/englishToFrench")
def en_fr():
    englishText = input.frenchToEnglish()
    return englishText

@app.route("/frenchToEnglish")
def fr_en():
    frenchText = input.englishToFrench()
    return frenchText

@app.route("/")
def renderIndexPage():
    return render_template ("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
