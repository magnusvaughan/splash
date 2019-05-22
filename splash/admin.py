from django.contrib import admin
from .models import Newspaper, Wordlist, Phrase, WordTotal

admin.site.register(Newspaper)
admin.site.register(Wordlist)
admin.site.register(Phrase)
admin.site.register(WordTotal)