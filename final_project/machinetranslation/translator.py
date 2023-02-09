import os
import json
import ibm_watson
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ.get('apikey')
url = os.environ.get('url')
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    English to French
    """
    translation = language_translator.translate(
    text = englishText,
    model_id = 'en-fr').get_result()
    frenchText = print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frenchText
    
def frenchToEnglish(frenchText):
    """
    French to English
    """
    translation = language_translator.translate(
    text = frenchText,
    model_id ='fr-en').get_result()
    englishText = print(json.dumps(translation, indent=2, ensure_ascii=False))
    return englishText
