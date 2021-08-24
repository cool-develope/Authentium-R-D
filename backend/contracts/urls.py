from django.urls import path
from toolz.dicttoolz import assoc_in

from . import views

app_name = 'contracts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('transact', views.TransactView.as_view(), name='transact'),
]