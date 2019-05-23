from django.contrib import admin
from .models import Newspaper, Wordlist, Phrase, WordTotal


class PhraseAdmin(admin.ModelAdmin):
    ordering = ('phrase',)

admin.site.register(Newspaper)
admin.site.register(Wordlist)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(WordTotal)