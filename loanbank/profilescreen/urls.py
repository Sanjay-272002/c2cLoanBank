from django.urls import path
from .import views

urlpatterns = [
    path('profilescreens', views.profilescreens, name="profilescreens"),
]