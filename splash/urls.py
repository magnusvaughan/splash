from django.conf import settings
from django.urls import include, path
from .views import WordlistListView, WordlistDetailView, PhraseListView, PhraseDetailView

urlpatterns = [
    path('wordlist/<int:pk>/', WordlistDetailView.as_view(), name='wordlist_detail'),
    path('home', WordlistListView.as_view(), name='home'),
    path('phrase/<int:pk>/', PhraseDetailView.as_view(), name='phrase_detail'),
    path('', PhraseListView.as_view(), name='phrase'),
    path('phrase/<newspaper>', PhraseListView.as_view(), name='phrase'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

