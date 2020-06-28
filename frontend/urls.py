from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ),
]

urlpatterns += [
    # match the root
    path(r'^$', views.index),
    # match all other pages
    path(r'^(?:.*)/?$', views.index),
]