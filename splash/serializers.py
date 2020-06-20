from rest_framework import serializers
from .models import Newspaper

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = ('id', 'name')