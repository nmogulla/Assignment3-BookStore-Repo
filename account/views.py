from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrationForm
from .models import User
from .forms import *


def dashboard(request):
    return render(request, 'account/user/dashboard.html')


def account_register(request):
    # if request.user.is_authenticated:
    # return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            print("here 1")
            return render(request, 'account/registration/register_done.html', {'new_user': user})
    else:
        registerForm = RegistrationForm()
        print("here 2")
    return render(request, 'account/registration/register.html', {'form': registerForm})


def user_profile(request):
    #user = User.objects.filter(pk=pk)
    #profileForm = ViewProfileForm(request.POST, instance=User.objects.get(pk=pk))
    #return render(request, 'account/registration/profile.html', {'user_form': profileForm})
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('storage:products_list')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
                  'account/registration/profile.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print("username", cd['username'])
            user = User.objects.get(user_name=cd['username'])
            # user = authenticate(request, user_name=cd['username'], password=cd['password'])
            print("user is", user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return redirect('storage:products_list')
                    # return dashboard(request)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login <a href="http://localhost:8000/login/"> login </a>')
    else:
        form = LoginForm()
        print("here 2")
    return render(request, 'account/registration/login.html', {'form': form})
