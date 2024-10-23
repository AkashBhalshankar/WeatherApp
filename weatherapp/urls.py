from django.urls import path
from .views import index, summary

urlpatterns = [
    path('', index, name='index'),
    path('summary/', summary, name='summary'),
]
