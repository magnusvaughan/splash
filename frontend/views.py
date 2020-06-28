from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Sum, Count, Q, Prefetch
from splash.models import Wordlist, WordTotal, Phrase, Newspaper
from django.shortcuts import get_object_or_404
from splash.serializers import NewspaperSerializer, WordlistSerializer, PhraseSerializer, PhraseListSerializer, WordtotalSerializer
from rest_framework import generics
from pprint import pprint


def index(request):
    return render(request, 'frontend/index.html')