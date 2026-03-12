
# Chat view for messaging
from django.contrib.auth import get_user_model
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def chat(request, user_id):
	User = get_user_model()
	other_user = User.objects.get(id=user_id)
	# Only allow chat if there is an application relationship
	from applications.models import Application
	if request.user.is_company:
		allowed = Application.objects.filter(internship__company=request.user, applicant=other_user).exists()
	else:
		allowed = Application.objects.filter(applicant=request.user, internship__company=other_user).exists()
	if not allowed:
		return redirect('inbox')
	messages = Message.objects.filter(
		(models.Q(sender=request.user, recipient=other_user) |
		 models.Q(sender=other_user, recipient=request.user))
	).order_by('timestamp')
	return render(request, 'chat.html', {
		'messages': messages,
		'user': request.user,
		'other_user': other_user,
	})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db import models
from .models import Message, Notification
from .forms import MessageForm

User = get_user_model()

from applications.models import Application

@login_required
def inbox(request):
	if hasattr(request.user, 'is_company') and request.user.is_company:
		# Company: show all interns who applied to their internships
		intern_ids = Application.objects.filter(internship__company=request.user).values_list('applicant', flat=True).distinct()
		users = User.objects.filter(id__in=intern_ids)
	else:
		# Intern: show all companies they've applied to
		company_ids = Application.objects.filter(applicant=request.user).values_list('internship__company', flat=True).distinct()
		users = User.objects.filter(id__in=company_ids)
	return render(request, 'inbox.html', {'users': users})


@login_required
def notifications(request):
	notes = Notification.objects.filter(user=request.user).order_by('-timestamp')
	return render(request, 'notifications.html', {'notifications': notes})
