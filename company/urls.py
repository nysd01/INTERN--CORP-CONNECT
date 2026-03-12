from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='company_dashboard'),
    path('post/', views.post_internship, name='post_internship'),
    path('applications/', views.applications_view, name='company_applications'),
    path('applications/<int:application_id>/documents/', views.application_documents, name='application_documents'),
]