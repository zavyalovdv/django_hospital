from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request ,user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, template_name='patient/login/login.html', context={'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
