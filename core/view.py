from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def carousel(request):
    return render(request, 'carousel.html')