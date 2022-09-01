from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'first_hello/index.html'
    return render(request, template)


def first_hello(request):
    template = 'first_hello/first_hello.html'
    return render(request, template)