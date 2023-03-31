from django.urls import path
from . import second
from . import first
from . import views

urlpatterns = [
path('second/', views.dude_coming),
path('first/', first.demo)
]
