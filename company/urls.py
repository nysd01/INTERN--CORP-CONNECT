from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='company_dashboard'),
    path('post/', views.post_internship, name='post_internship'),
]