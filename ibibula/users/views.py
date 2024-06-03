
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse

from django.http import HttpResponseRedirect

from users.forms import  UserLoginForm, UserRegistrationForm, ProfileForm
from users.models import User

def login(request):

    users = User.objects.all()

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'users':users,
        'form':form
    }

    return render(request, 'users/login.html', context)

def profile(request):

    context = {
        'title':'Все для студентов'
    }

    return render(request, 'users/profile.html', context)

def registration(request):

    context = {
        'title':'Все для студентов'
    }

    return render(request, 'users/registration.html', context)

def edituser(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
        

    context = {
        'title': 'Home - Кабинет',
        'form': form,
    }
    return render(request, 'users/edituser.html', context)


def editservice(request):

    context = {
        'title':'Все для студентов'
    }

    return render(request, 'users/editservices.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Все для студентов',
        'form': form
    }
    return render(request, 'users/registration.html', context)


def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))