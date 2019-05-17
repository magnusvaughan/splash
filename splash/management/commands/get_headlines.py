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

        print(noun_phrase_list)
        noun_phrase_assoc = {}

        for phrase in noun_phrase_list:
            if( phrase in noun_phrase_assoc.keys() ):
                noun_phrase_assoc[phrase] += 1
            else:
                noun_phrase_assoc[phrase] = 1

        noun_phrase_assoc = {key:val for key, val in noun_phrase_assoc.items() if val != 1}

        sorted_phrases_count = sorted(noun_phrase_assoc.items(), key=operator.itemgetter(1), reverse=True)

        pp = pprint.PrettyPrinter(depth=6)

        pp.pprint(sorted_phrases_count)

        wordlist_json = json.dumps(sorted_phrases_count)

        from splash.models import Wordlist, Newspaper
        newspaper = Newspaper.objects.get(id=1)
        wordlist_record = Wordlist(newspaper=newspaper, words=wordlist_json)
        wordlist_record.save()
