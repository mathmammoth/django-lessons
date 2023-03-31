from django.shortcuts import render
from django.http import HttpResponse

counter = 0

def demo(request):  
    global counter
    counter += 1
    # now do your stuff
    if counter in range(2,5):
        return HttpResponse(f'Страницу посетили {counter} раза')
    else:
        return HttpResponse(f'Страницу посетили {counter} раз')



