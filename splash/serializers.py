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

class WordTotalSerializer(serializers.ModelSerializer):
    wordlist = WordlistSerializer(required=False, many=False)
    class Meta:
        model = WordTotal
        fields = ['wordlist', 'phrase', 'count']

class PhraseListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    class Meta:
        model = Phrase
        fields = "__all__"

class PhraseSerializer(serializers.ModelSerializer):
    wordtotals = WordTotalSerializer(required=False, many=True)
    class Meta:
        model = Phrase
        fields = ['phrase', 'wordtotals']

class WordtotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordTotal
        fields = ["__all__"]
