from django.contrib.postgres.fields import JSONField
from django.db import models

class Newspaper(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Wordlist(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    newspaper = models.ForeignKey('Newspaper',on_delete=models.CASCADE,)
    words = JSONField()

    def __str__(self):
        return self.date