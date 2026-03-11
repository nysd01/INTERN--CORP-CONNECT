from django.shortcuts import render
from messaging.models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notifications(request):
	notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
	# Mark all as read
	notifications.update(read=True)
	return render(request, 'notifications.html', {'notifications': notifications})
