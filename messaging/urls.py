from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send_message'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('notifications/', views.notifications, name='notifications'),
]