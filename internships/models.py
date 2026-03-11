from django.db import models
from django.conf import settings

class Internship(models.Model):
	company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_internships')
	title = models.CharField(max_length=200)
	description = models.TextField()
	location = models.CharField(max_length=100)
	posted_at = models.DateTimeField(auto_now_add=True)
	required_documents = models.CharField(max_length=255, blank=True, help_text="Comma-separated list of required documents (e.g. CV, Cover Letter)")
	document = models.FileField(upload_to='internship_docs/', blank=True, null=True)

	def __str__(self):
		return f"{self.title} at {self.company}" 
