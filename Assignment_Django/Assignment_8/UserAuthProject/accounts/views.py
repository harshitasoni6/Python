from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Home Page
@login_required
def home(request):
    return render(request, 'accounts/home.html')

# Registration
def register_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in after registration
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_request(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page
