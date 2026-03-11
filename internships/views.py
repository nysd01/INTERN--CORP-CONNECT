from django.shortcuts import render, get_object_or_404
from .models import Internship

def list_internships(request):
	internships = Internship.objects.all().order_by('-posted_at')
	return render(request, 'list_internships.html', {'internships': internships})

def internship_detail(request, id):
	internship = get_object_or_404(Internship, id=id)
	return render(request, 'internship_detail.html', {'internship': internship})
