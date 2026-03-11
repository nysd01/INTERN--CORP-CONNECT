from django.shortcuts import render
from django.http import HttpResponse

def view_profile(request):
	return render(request, 'view_profile.html')

def edit_profile(request):
	return render(request, 'edit_profile.html')
