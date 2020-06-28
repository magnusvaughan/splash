from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('newspaper/', views.NewspaperListCreate.as_view() ),
    path('wordlist/', views.WordlistListCreate.as_view() ),
    path('phraselist/', views.PhraselistListCreate.as_view() ),
    path('wordtotallist/', views.WordTotalListCreate.as_view() ),
    path('phrases/<int:pk>', views.PhraseDetailAPIView.as_view()),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
