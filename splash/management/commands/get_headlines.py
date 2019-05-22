from django.core.management.base import BaseCommand
import json
import requests
from bs4 import BeautifulSoup
import spacy
import json
import pprint
import time
import operator

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # The Mail

        base_url = 'https://www.dailymail.co.uk/home/index.html'

        # Load English tokenizer, tagger, parser, NER and word vectors
        nlp = spacy.load("en_core_web_sm")

        page = requests.get(base_url)

        soup = BeautifulSoup(page.text, 'html.parser')

        headline_wrappers =  soup.findAll(class_='pufftext')

        noun_phrase_list = []

        for headline_wrapper in headline_wrappers:
                headline_bold = headline_wrapper.find('strong')
                if headline_bold is not None:
                    headline_unparsed = headline_bold.text
                    headline_parsed = headline_unparsed.replace("\n", "")
                    headline = headline_parsed.strip()
                    print(headline)
                    doc = nlp(str(headline))
                    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
                    noun_phrase_list = noun_phrase_list + noun_phrases

        noun_phrase_assoc = {}

        for phrase in noun_phrase_list:
            if( phrase in noun_phrase_assoc.keys() ):
                noun_phrase_assoc[phrase] += 1
            else:
                noun_phrase_assoc[phrase] = 1

        print(noun_phrase_assoc)

        # noun_phrase_assoc = {key:val for key, val in noun_phrase_assoc.items() if val != 1}

        from splash.models import Wordlist, Newspaper, Phrase, WordTotal

        newspaper = Newspaper.objects.get(name="The Mail")
        wordlist_record = Wordlist(newspaper=newspaper)
        wordlist_record.save()

        for key, value in noun_phrase_assoc.items():
            if(Phrase.objects.filter(phrase=key).count()):
                phrase = Phrase.objects.get(phrase=key)
                wordtotal_record = WordTotal(wordlist=wordlist_record,phrase=phrase,count=value)
                wordtotal_record.save()
            else:
                phrase_record = Phrase(phrase=key)
                phrase_record.save()
                wordtotal_record = WordTotal(wordlist=wordlist_record,phrase=phrase_record,count=value)
                wordtotal_record.save()

        # # The Guardian

        # base_url = 'https://www.theguardian.com/uk'

        # page = requests.get(base_url)

        # soup = BeautifulSoup(page.text, 'html.parser')

        # headline_wrappers = soup.findAll(class_='js-headline-text')

        # noun_phrase_list = []

        # for headline_wrapper in headline_wrappers:
        #     headline_unparsed = headline_wrapper.text
        #     headline_parsed = headline_unparsed.replace("\n", "")
        #     headline = headline_parsed.strip()
        #     print(headline)
        #     doc = nlp(str(headline))
        #     noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        #     noun_phrase_list = noun_phrase_list + noun_phrases

        # noun_phrase_assoc = {}

        # for phrase in noun_phrase_list:
        #     if( phrase in noun_phrase_assoc.keys() ):
        #         noun_phrase_assoc[phrase] += 1
        #     else:
        #         noun_phrase_assoc[phrase] = 1

        # noun_phrase_assoc = {key:val for key, val in noun_phrase_assoc.items() if val != 1}

        # newspaper = Newspaper.objects.get(name="The Guardian")
        # wordlist_record = Wordlist(newspaper=newspaper, words=noun_phrase_assoc)
        # wordlist_record.save()

        # #The Telegraph

        # base_url = 'https://www.telegraph.co.uk/'

        # page = requests.get(base_url)

        # soup = BeautifulSoup(page.text, 'html.parser')

        # headline_wrappers = soup.findAll(class_='list-of-entities__item-body-headline')

        # noun_phrase_list = []

        # for headline_wrapper in headline_wrappers:
        #     headline_link = headline_wrapper.find('a')
        #     if headline_link is not None:
        #         headline_unparsed = headline_link.text
        #         if headline_unparsed is not None:
        #             headline_parsed = headline_unparsed.replace("\n", "")
        #             headline = headline_parsed.strip()
        #             print(headline)
        #             doc = nlp(str(headline))
        #             noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        #             noun_phrase_list = noun_phrase_list + noun_phrases

        # noun_phrase_assoc = {}

        # for phrase in noun_phrase_list:
        #     if( phrase in noun_phrase_assoc.keys() ):
        #         noun_phrase_assoc[phrase] += 1
        #     else:
        #         noun_phrase_assoc[phrase] = 1

        # noun_phrase_assoc = {key:val for key, val in noun_phrase_assoc.items() if val != 1}

        # newspaper = Newspaper.objects.get(name="The Telegraph")
        # wordlist_record = Wordlist(newspaper=newspaper, words=noun_phrase_assoc)
        # wordlist_record.save()

        # # The Express

        # base_url = 'https://www.express.co.uk/'

        # page = requests.get(base_url)

        # soup = BeautifulSoup(page.text, 'html.parser')

        # headline_wrappers = soup.findAll(['h2', 'h4'])

        # noun_phrase_list = []

        # for headline_wrapper in headline_wrappers:
        #     headline_unparsed = headline_wrapper.text
        #     headline_parsed = headline_unparsed.replace("\n", "")
        #     headline = headline_parsed.strip()
        #     print(headline)
        #     doc = nlp(str(headline))
        #     noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        #     noun_phrase_list = noun_phrase_list + noun_phrases

        # noun_phrase_assoc = {}

        # for phrase in noun_phrase_list:
        #     if( phrase in noun_phrase_assoc.keys() ):
        #         noun_phrase_assoc[phrase] += 1
        #     else:
        #         noun_phrase_assoc[phrase] = 1

        # noun_phrase_assoc = {key:val for key, val in noun_phrase_assoc.items() if val != 1}

        # newspaper = Newspaper.objects.get(name="The Express")
        # wordlist_record = Wordlist(newspaper=newspaper, words=noun_phrase_assoc)
        # wordlist_record.save()