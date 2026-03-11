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
def chat(request, user_id):
	other_user = get_object_or_404(User, id=user_id)
	messages = Message.objects.filter(
		(models.Q(sender=request.user) & models.Q(recipient=other_user)) |
		(models.Q(sender=other_user) & models.Q(recipient=request.user))
	).order_by('timestamp')
	# Mark messages as read
	Message.objects.filter(sender=other_user, recipient=request.user, is_read=False).update(is_read=True)
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			msg = form.save(commit=False)
			msg.sender = request.user
			msg.recipient = other_user
			msg.save()
			# Create notification for recipient
			Notification.objects.create(user=other_user, message=f'New message from {request.user.username}', link=f'/messaging/chat/{request.user.id}/')
			return redirect('chat', user_id=other_user.id)
	else:
		form = MessageForm()
	return render(request, 'chat.html', {'other_user': other_user, 'messages': messages, 'form': form})

@login_required
def send_message(request):
	return render(request, 'send_message.html')

@login_required
def notifications(request):
	notes = Notification.objects.filter(user=request.user).order_by('-timestamp')
	return render(request, 'notifications.html', {'notifications': notes})
