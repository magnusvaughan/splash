from django.views.generic import ListView
from .models import Newspaper

class NewspaperListView(ListView):
    model = Newspaper
    template_name = 'home.html'