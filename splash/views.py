from django.views.generic import ListView, DetailView
from .models import Wordlist

class WordlistListView(ListView):
    model = Wordlist
    template_name = 'home.html'

class WordlistDetailView(DetailView):
    model = Wordlist
    template_name = 'wordlist_detail.html'