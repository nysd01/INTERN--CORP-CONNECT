
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

def dashboard(request):
	return render(request, 'intern_dashboard.html')

def search_internships(request):
	from internships.models import Internship
	query = request.GET.get('q', '').strip()
	internships = []
	if query:
		internships = Internship.objects.filter(
			models.Q(title__icontains=query) |
			models.Q(description__icontains=query) |
			models.Q(location__icontains=query) |
			models.Q(company__username__icontains=query)
		)
	else:
		internships = Internship.objects.all()
	return render(request, 'search_internships.html', {'internships': internships})
