from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def overview(request):
    return render(request, 'overview.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')
