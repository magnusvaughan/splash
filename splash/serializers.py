from rest_framework import serializers
from .models import Newspaper, Wordlist, Phrase, WordTotal

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ('id', 'name')

class WordlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordlist
        fields = ('date', 'newspaper')

class PhraselistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = "__all__"

class WordtotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordTotal
        fields = "__all__"