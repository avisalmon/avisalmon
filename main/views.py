from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {'form':forms.UserCreateForm()})
    else:
        form = forms.UserCreateForm(request.POST)
        print(f'Form::: \n{form.errors}')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            authenticate( username=username,password=raw_password)
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('home')

        else:
            error = form.errors
            return render(request, 'registration/signup.html', {'form':forms.UserCreateForm(), 'error': error})

        # if request.POST['password1'] == request.POST['password2']:
        #     try:
        #         user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        #         user.save()
        #         login(request, user)
        #         return redirect('home')
        #     except IntegrityError:
        #         return render(request,
        #                       'main/signuplocal.html',
        #                       {'form':UserCreationForm(),
        #                        'error':'That username has already been taken. Please choose a new username'})
        # else:
        #     return render(request, 'main/signup_local.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
