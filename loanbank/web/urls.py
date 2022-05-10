from  django.urls import path

from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('profile',views.profile, name="profile"),
    path('askloan',views.askloan, name="askloan"),
    path('status',views.status, name="status"),
   
]