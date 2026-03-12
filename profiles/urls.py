from django.urls import path

from accounts.views import profile_page

urlpatterns = [
    path('profile/', profile_page, name='profile_page'),
]