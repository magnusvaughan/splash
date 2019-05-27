from django.contrib.postgres.fields import JSONField
from django.db import models

class Newspaper(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Wordlist(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    newspaper = models.ForeignKey('Newspaper',on_delete=models.CASCADE,)
    
    def __str__(self):
        return str(self.date)

class Phrase(models.Model):
    phrase = models.CharField(max_length=400)

    def __str__(self):
        return str(self.phrase)

class WordTotal(models.Model):
    wordlist =  models.ForeignKey('Wordlist',on_delete=models.CASCADE,)
    phrase = models.ForeignKey('Phrase',on_delete=models.CASCADE,)
    count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.count)