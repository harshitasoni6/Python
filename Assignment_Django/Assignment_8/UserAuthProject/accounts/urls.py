from django.urls import path,include
from accounts import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('accounts/register/', views.register_request, name='register'),
    path('accounts/login/', views.login_request, name='login'),
    path('accounts/logout/', views.logout_request, name='logout'),
]
