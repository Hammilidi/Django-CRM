from django.shortcuts import render

def home(request):
    render(request, 'home.html', {})