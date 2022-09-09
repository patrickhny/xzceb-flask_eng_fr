'''Translator.py works includes methods for connecting my code to the Watson Langauge
Translator API. It also includes functions for translating English text to French text
and vice versa '''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# apikey and url are called from the .env file and connect the Watson Language Translator
# API to my code
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''Function that calls on Watson Language Translator API to translate english text into french
    text'''
    if english_text == '':
        return ''
    # in the below line I call the .translate() method from the LanguageTranslatorV3 module
    e2f_translation_result = language_translator.translate(text=english_text, model_id='en-fr') \
        .get_result()
    # what is returned from the above line is a dictionary-like object that has set-like properties
    # so indexing is not available and I pass the result into an indexable list in the below line
    # in order to retireve the translated text
    e2f_list = list(e2f_translation_result.values())
    e2f_translation = e2f_list[0][0].get('translation')
    return e2f_translation


def french_to_english(french_text):
    '''Function that calls on Watson Language Translator API to translate english text into french
    text'''
    if french_text == '':
        return ''
    # same logic as above function
    f2e_translation_result = language_translator.translate(text=french_text, model_id='fr-en') \
        .get_result()
    f2e_list = list(f2e_translation_result.values())
    f2e_transaltion = f2e_list[0][0].get('translation')
    return f2e_transaltion


# testing it in my terminal

'''
english_test = english_to_french('Hello')
french_test = french_to_english('Bonjour')
print(english_test)
print(french_test)
'''