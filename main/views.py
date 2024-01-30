from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'content': 'My name fucking bot',
        'title': 'home'
    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('<h1>About page</h1>')