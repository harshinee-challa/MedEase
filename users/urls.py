from django.urls import path 
from . import views

urlpatterns = [
path('',views.loginUser,name="login"),
path('profiles/',views.profiles,name="profiles"),
path('logout/',views.logoutUser,name="logout"),
path('register/',views.registerUser,name="register"),
]
