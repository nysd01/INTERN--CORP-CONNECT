from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
	return render(request, 'intern_dashboard.html')

def search_internships(request):
	return render(request, 'search_internships.html')
