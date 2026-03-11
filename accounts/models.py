from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	is_company = models.BooleanField(default=False)
	is_intern = models.BooleanField(default=False)


class CompanyProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	website = models.URLField(blank=True)
	photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
	address = models.CharField(max_length=255, blank=True)


class InternProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	domain = models.CharField(max_length=255)
	resume = models.FileField(upload_to='resumes/')
	bio = models.TextField(blank=True)
	photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
	address = models.CharField(max_length=255, blank=True)
