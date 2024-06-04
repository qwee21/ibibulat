from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.template import context
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.utils.text import slugify

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm, ProductForm
from users.models import User
from main.models import Services


def login(request):

    users = User.objects.all()

    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"users": users, "form": form}

    return render(request, "users/login.html", context)


def profile(request):

    context = {"title": "Все для студентов"}

    return render(request, "users/profile.html", context)


@login_required
def edituser(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, instance=request.user, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": "Home - Кабинет",
        "form": form,
    }
    return render(request, "users/editusers.html", context)



def editservice(request):
    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            print(form.cleaned_data)  # Add this line to print out the form data
            product = Services()
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.image = form.cleaned_data['image']
            product.category = form.cleaned_data['category']
            product.subcategory = form.cleaned_data['subcategory']
            product.slug = slugify(form.cleaned_data['name'])
            product.save()
            product.refresh_from_db()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = ProductForm()

    context = {"title": "Все для студентов", "form": form}
    return render(request, "users/editservices.html", context)





def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = UserRegistrationForm()

    context = {"title": "Все для студентов", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
