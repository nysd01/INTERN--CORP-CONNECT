from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:internship_id>/', views.apply, name='apply'),
    path('status/', views.application_status, name='application_status'),
    path('update_status/<int:application_id>/', views.update_application_status, name='update_application_status'),
    path('resubmit/<int:application_id>/', views.resubmit_documents, name='resubmit_documents'),
]