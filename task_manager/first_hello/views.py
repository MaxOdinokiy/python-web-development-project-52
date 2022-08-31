from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'first_hello/index.html'
    return render(request, template, context={
        'text': 'Hello! This is my first Django app'
    })