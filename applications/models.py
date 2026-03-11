from django.db import models
from django.conf import settings
from internships.models import Internship


class Application(models.Model):
	internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications')
	applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
	status = models.CharField(max_length=30, choices=[
		('pending', 'Pending'),
		('accepted', 'Accepted'),
		('rejected', 'Rejected'),
		('resubmission', 'Resubmission Requested')
	], default='pending')
	date_applied = models.DateTimeField(auto_now_add=True)
	uploaded_document = models.FileField(upload_to='application_docs/', blank=True, null=True)

	def __str__(self):
		return f"{self.applicant} applied to {self.internship}" 
