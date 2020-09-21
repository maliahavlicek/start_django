from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('Hello!')


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')