from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('currencies')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exists")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, "Logged In successfuly")
            return redirect('currencies')
        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out")
    return render(request, 'users/logout_page.html')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created")
            login(request, user)
            return redirect('currencies')
        
        else:
            messages.error(request, "An error occurred during registration")

    context = {'page' : page, 'form' : form}
    return render(request, 'users/login_register.html', context)
    
