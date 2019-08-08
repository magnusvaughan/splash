from django.views.generic import ListView, DetailView
from django.db.models import Sum, Count
from .models import Wordlist, WordTotal, Phrase, Newspaper
from django.shortcuts import get_object_or_404

phrases_to_ignore = [
    "he", "she", "i", "it", "they", "Comment", "you", "who", "her", "we", "What", "me",
    "us", "I", "him", "what", "We", "It", "You", "'s", "Gallery"
]

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
        for phrase_to_ignore in phrases_to_ignore:
            wordtotals = wordtotals.exclude(phrase__phrase=phrase_to_ignore)
        context.update({'wordtotals': wordtotals})
        return context

class PhraseListView(ListView):
    model = Phrase
    template_name = 'phrase.html'
    context_object_name = 'wordtotals'
    ordering = ['phrase']

    def get_context_data(self, **kwargs):
        if('newspaper' in self.kwargs):
            self.newspaper = get_object_or_404(Newspaper, name=self.kwargs['newspaper'].replace('_', ' ').title())
        else:
            self.newspaper = None
        context = super(PhraseListView, self).get_context_data(**kwargs)
        phrases = Phrase.objects.all().annotate(Count('wordtotal__count')).filter(wordtotal__count__gte=30)
        phrases = phrases.exclude(phrase__in=phrases_to_ignore)

        wordtotals_object = {}

        if(self.newspaper != None):
            active_newspaper = self.newspaper.name
        else:
            active_newspaper = "All newspapers"

        for phrase in phrases:
            # if(phrase.phrase not in phrases_to_ignore):
            wordtotals = phrase.wordtotal_set.all()
            wordtotals_total = wordtotals.aggregate(Sum('count'))

            count = 0

            if(self.newspaper == None):
                wordtotals_object[phrase.phrase] = wordtotals_total['count__sum']
            else:
                for wordtotal in wordtotals:
                    if(self.newspaper != None):
                        if(wordtotal.wordlist.newspaper.name == self.newspaper.name):
                            count+=wordtotal.count
            if(count > 0):
                wordtotals_object[phrase.phrase] = count

        import operator

        sorted_wordtotals = sorted(wordtotals_object.items(), key=operator.itemgetter(0))
        sorted_wordtotals = sorted(sorted_wordtotals, key=operator.itemgetter(1), reverse=True)
        # sorted_wordtotals_truncated = sorted_wordtotals[0:200]

        context.update(
            {'wordtotals': sorted_wordtotals,
            'active_newspaper': active_newspaper,
            'wordtotals_total': wordtotals_total
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