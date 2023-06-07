from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Clear messages before rendering the form
            storage = messages.get_messages(request)
            storage.used = True
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(
                request, f'Login successful!')
            return redirect('home')
        else:
            messages.error(
                request, f'Login failed. Check your username or password')
            return render(request, 'user/login.html')

    return render(request, 'user/login.html')


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile_page(request):
    user = request.user
    
    return render(request, 'user/profile.html')
