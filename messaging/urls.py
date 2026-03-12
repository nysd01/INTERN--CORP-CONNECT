from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('notifications/', views.notifications, name='notifications'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
]