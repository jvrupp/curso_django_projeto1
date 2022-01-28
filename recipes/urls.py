from django.contrib import admin
from django.urls import path

from recipes.views import contato, home, sobre, temp

urlpatterns = [
    path('', home),
    path('temp/', temp),
    path('contato/', contato),
]
