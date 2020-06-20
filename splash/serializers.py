from rest_framework import serializers
from .models import Newspaper, Wordlist, Phrase

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