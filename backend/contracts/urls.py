from django.urls import path
from toolz.dicttoolz import assoc_in

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]