import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os


apikey = 'Zcyn69axF0Dm3poBCQZXc2Tsm4TKf903Al5NStnu9JRd'
url = 'https://api.us-east.language-translator.watson.cloud.ibm.com/instances/7969364c-6a5b-40c7-8656-5a0acb79d1f8'
version = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
translator.set_service_url(url)

def englishToFrench(englishText):
    text = englishText
    translate_fr = translator.translate(text=text, model_id='en-fr').get_result()
    frenchText = translate_fr['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    text = frenchText
    translate_en = translator.translate(text=text, model_id='fr-en').get_result()
    englishText = translate_en['translations'][0]['translation']
    return englishText

