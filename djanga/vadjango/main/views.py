from django.shortcuts import render
from .models import joints

def dude_coming(request):
    join = joints.objects.all()
    return render(request, 'main/index.html', {'join': join})