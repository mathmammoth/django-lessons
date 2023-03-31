from django.shortcuts import render
from django.http import HttpResponse

def demo(request):

    return HttpResponse("<h4>Привет, почешись</h4>")
