from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login as auth_login
# Create your views here.
def indexLogin(request):
    if request.user.is_authenticated:
       return render(request, "login.html")
    return render(request, "indexLogin.html")
    
    # return render(request,'indexLogin.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username =username ,password = password)
        if user is not None:
            auth_login(request,user)
            return render(request,'login.html')
        else:
            return render(request,'indexLogin.html',{"error": "Invalid username or password"})
    return render(request, "indexLogin.html")
def logoutUser(request):
    logout(request)
    return redirect("indexLogin")