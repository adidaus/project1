from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.wiki , name='wiki'),
    # path('result', views.result, name='result')
]
