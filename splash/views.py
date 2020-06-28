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