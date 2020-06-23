from django.conf import settings
from django.urls import include, path
from . import views
from .views import WordlistListView, WordlistDetailView, PhraseListView, PhraseDetailView, PhraseDetailAPIView

urlpatterns = [
    path('wordlist/<int:pk>/', WordlistDetailView.as_view(), name='wordlist_detail'),
    path('home', WordlistListView.as_view(), name='home'),
    path('phrase/<int:pk>/', PhraseDetailView.as_view(), name='phrase_detail'),
    # path('', PhraseListView.as_view(), name='phrase'),
    path('phrase/<newspaper>', PhraseListView.as_view(), name='phrase'),
    path('api/newspaper/', views.NewspaperListCreate.as_view() ),
    path('api/wordlist/', views.WordlistListCreate.as_view() ),
    path('api/phraselist/', views.PhraselistListCreate.as_view() ),
    path('api/wordtotallist/', views.WordTotalListCreate.as_view() ),
    path('api/phrases/<int:pk>', PhraseDetailAPIView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
