from django.shortcuts import render
from django.http import HttpResponse

def front_view(request):
    return render(request, 'index.html')

def acerca(request):
    return render(request, 'acerca.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')