from django.views.generic import ListView, DetailView
from .models import Wordlist, WordTotal

class WordlistListView(ListView):
    model = Wordlist
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(WordlistListView, self).get_context_data(**kwargs)
        wordlists = Wordlist.objects.all().order_by('newspaper')
        context.update({'wordlists': wordlists})
        return context

class WordlistDetailView(DetailView):
    model = Wordlist
    template_name = 'wordlist_detail.html'
    context_object_name = 'wordlistinfo'

    def get_context_data(self, **kwargs):
        context = super(WordlistDetailView, self).get_context_data(**kwargs)
        wordlist = Wordlist.objects.get(id=self.kwargs['pk'])
        wordtotals = wordlist.wordtotal_set.all().order_by('-count', 'phrase')
        context.update({'wordtotals': wordtotals})
        return context