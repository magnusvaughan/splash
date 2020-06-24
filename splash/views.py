from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum, Count, Q, Prefetch
from .models import Wordlist, WordTotal, Phrase, Newspaper
from django.shortcuts import get_object_or_404
from .serializers import NewspaperSerializer, WordlistSerializer, PhraseSerializer, PhraseListSerializer, WordtotalSerializer
from rest_framework import generics
from pprint import pprint

phrases_to_ignore = [
    "he", "she", "i", "it", "they", "Comment", "you", "who", "her", "we", "What", "me",
    "us", "I", "him", "what", "We", "It", "You", "'s", "Gallery"
]

class WordlistListView(ListView):
    model = Wordlist
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(WordlistListView, self).get_context_data(**kwargs)
        wordlists = Wordlist.objects.all().order_by('-date', 'newspaper')
        context.update({'wordlists': wordlists})
        return context

class WordlistDetailView(DetailView):
    model = Wordlist
    template_name = 'wordlist_detail.html'
    context_object_name = 'wordlistinfo'

    def get_context_data(self, **kwargs):
        context = super(WordlistDetailView, self).get_context_data(**kwargs)
        wordlist = Wordlist.objects.get(id=self.kwargs['pk'])
        wordtotals = wordlist.wordtotal_set.all().order_by('-count', 'phrase')
        for phrase_to_ignore in phrases_to_ignore:
            wordtotals = wordtotals.exclude(phrase__phrase=phrase_to_ignore)
        context.update({'wordtotals': wordtotals})
        return context

class PhraseListView(ListView):

    model = Phrase
    template_name = 'phrase.html'
    context_object_name = 'wordtotals'
    ordering = ['phrase']

    def get_context_data(self, **kwargs):
        if('newspaper' in self.kwargs):
            self.newspaper = get_object_or_404(Newspaper, name=self.kwargs['newspaper'].replace('_', ' ').title())
            print(self.newspaper)
        else:
            self.newspaper = None
        context = super(PhraseListView, self).get_context_data(**kwargs)
        phrases = Phrase.objects.all()
        if(self.newspaper != None):
            active_newspaper = self.newspaper.name
            phrases = phrases.filter(wordtotal__wordlist__newspaper__name=self.newspaper)
        else:
            active_newspaper = "All newspapers"
        phrases = phrases.annotate(count=Sum('wordtotal__count'))
        phrases = phrases.exclude(phrase__in=phrases_to_ignore).order_by('-count')
        truncated_phrases = phrases[0:3000]

        context.update({
            'active_newspaper': active_newspaper,
            'phrases': truncated_phrases
        })
                  
        return context

class PhraseDetailView(DetailView):
    model = Phrase
    template_name = 'phrase_detail.html'
    context_object_name = 'phrase'

    def get_context_data(self, **kwargs):
        context = super(PhraseDetailView, self).get_context_data(**kwargs)
        phrase = Phrase.objects.get(id=self.kwargs['pk'])
        wordtotals = phrase.wordtotal_set.all()
        count = 0
        for wordtotal in wordtotals:
            count = count + wordtotal.count
            
        context.update(
            {'wordtotals': {
                phrase.phrase: count
            }
        })
        return context

#DRF API Views

class NewspaperListCreate(generics.ListCreateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer

class WordlistListCreate(generics.ListCreateAPIView):
    queryset = Wordlist.objects.all()
    serializer_class = WordlistSerializer

class PhraselistListCreate(generics.ListCreateAPIView):
    serializer_class = PhraseListSerializer
    queryset = Phrase.objects.all()

    def get_queryset(self):
        return Phrase.objects.prefetch_related('wordtotals').annotate(
            count=Sum('wordtotals__count')
        ).exclude(phrase__in=phrases_to_ignore).order_by('-count')

class PhraseDetailAPIView(generics.RetrieveAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

    def get_queryset(self):
        return Phrase.objects.prefetch_related('wordtotals')

class WordTotalListCreate(generics.ListCreateAPIView):
    serializer_class = WordtotalSerializer

    queryset = WordTotal.objects.all().prefetch_related(
       'phrase',
       'wordlist'
    )