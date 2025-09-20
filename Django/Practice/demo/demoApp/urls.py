from django.urls import path
from demoApp import views

urlpatterns = [
    path("",views.hello,name="hello")
]
