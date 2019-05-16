from django.urls import path
from .views import NewspaperListView

urlpatterns = [
    path('', NewspaperListView.as_view(), name='home'),
]