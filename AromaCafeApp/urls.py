from django.urls import path
from . import views

app_name = "AromaCafeApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("cardapio/", views.cardapio, name="cardapio"),
    path("contato/", views.contato, name="contato"),
]
