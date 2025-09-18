from django.contrib import admin
from django.urls import path
from AuthenticationApp import views

urlpatterns = [
    path("",views.indexLogin,name = "indexLogin"),
    path("login",views.loginUser,name = "loginUser"),
    path("logout",views.logoutUser,name = "logoutUser")
]
