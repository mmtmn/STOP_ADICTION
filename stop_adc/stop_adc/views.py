from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')