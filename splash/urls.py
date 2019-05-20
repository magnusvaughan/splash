from django.urls import path
from .views import WordlistListView, WordlistDetailView

urlpatterns = [
    path('wordlist/<int:pk>/', WordlistDetailView.as_view(), name='wordlist_detail'),
    path('', WordlistListView.as_view(), name='home'),
]
