from django.urls import path
from . import second
from . import first

urlpatterns = [
path('second/', second.demo),
path('first/', first.demo)
]
