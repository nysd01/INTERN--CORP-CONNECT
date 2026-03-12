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
	# uploaded_document is deprecated, use ApplicationDocument instead

	def __str__(self):
		return f"{self.applicant} applied to {self.internship}"


# New model for multiple documents per application
class ApplicationDocument(models.Model):
	application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
	file = models.FileField(upload_to='application_docs/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	doc_type = models.CharField(max_length=100, blank=True, help_text="Type of document (e.g. CV, Cover Letter)")

	def __str__(self):
		return f"Document for {self.application}" 
