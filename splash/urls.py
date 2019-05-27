from django.urls import path
from .views import WordlistListView, WordlistDetailView, PhraseListView, PhraseDetailView

urlpatterns = [
    path('wordlist/<int:pk>/', WordlistDetailView.as_view(), name='wordlist_detail'),
    path('home', WordlistListView.as_view(), name='home'),
    path('phrase/<int:pk>/', PhraseDetailView.as_view(), name='phrase_detail'),
    path('', PhraseListView.as_view(), name='phrase'),
    path('phrase/<newspaper>', PhraseListView.as_view(), name='phrase'),
]
