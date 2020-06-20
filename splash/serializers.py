from rest_framework import serializers
from .models import Newspaper, Wordlist

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ('id', 'name')

class WordlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordlist
        fields = ('date', 'newspaper')