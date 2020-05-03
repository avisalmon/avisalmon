from django.shortcuts import render

def junk(request):
    return render(request, 'main/junk.html')

def home(request):
    return render(request, 'main/home.html')
