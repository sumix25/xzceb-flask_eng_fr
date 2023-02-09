
from flask import Flask, render_template, request
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
app = Flask("Web Translator")
apikey = 'Zcyn69axF0Dm3poBCQZXc2Tsm4TKf903Al5NStnu9JRd'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/7969364c-6a5b-40c7-8656-5a0acb79d1f8'
version = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
translator.set_service_url(url)

@app.route("/englishToFrench", methods=["GET", "POST"])
def englishToFrench():
        text = request.args.get("textToTranslate")
        translate_fr = translator.translate(text=text, model_id='en-fr').get_result()
        translated_text = translate_fr['translations'][0]['translation']
        return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
        text = request.args.get("textToTranslate")
        translate_en = translator.translate(text=text, model_id='fr-en').get_result()
        translated_text = translate_en['translations'][0]['translation']
        return translated_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
