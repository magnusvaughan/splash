from django.views.generic import ListView, DetailView
from .models import Wordlist, WordTotal, Phrase

class WordlistListView(ListView):
    model = Wordlist
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(WordlistListView, self).get_context_data(**kwargs)
        wordlists = Wordlist.objects.all().order_by('-date', 'newspaper')
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

class PhraseListView(ListView):
    model = Phrase
    template_name = 'phrase.html'
    context_object_name = 'wordtotals'
    ordering = ['phrase']

    def get_context_data(self, **kwargs):
        context = super(PhraseListView, self).get_context_data(**kwargs)
        phrases = Phrase.objects.all()

        wordtotals_object = {}

        for phrase in phrases:
            wordtotals = phrase.wordtotal_set.all()
            count = 0

            for wordtotal in wordtotals:
                count = count + wordtotal.count
                wordtotals_object[phrase.phrase] = count

        import operator

        sorted_wordtotals = sorted(wordtotals_object.items(), key=operator.itemgetter(1), reverse=True)

        context.update(
            {'wordtotals': sorted_wordtotals
        })
                  
        return context

class PhraseDetailView(DetailView):
    model = Phrase
    template_name = 'phrase_detail.html'
    context_object_name = 'phrase'

    def get_context_data(self, **kwargs):
        context = super(PhraseDetailView, self).get_context_data(**kwargs)
        phrase = Phrase.objects.get(id=self.kwargs['pk'])
        wordtotals = phrase.wordtotal_set.all()
        count = 0
        for wordtotal in wordtotals:
            count = count + wordtotal.count
            
        context.update(
            {'wordtotals': {
                phrase.phrase: count
            }
        })
        return context