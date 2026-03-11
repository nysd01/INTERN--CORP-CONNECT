from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_internships, name='list_internships'),
    path('<int:id>/', views.internship_detail, name='internship_detail'),
]