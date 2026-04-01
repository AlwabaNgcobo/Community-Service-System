from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("reports:report_issue")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("users:login")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


@login_required(login_url="/users/login/")
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("users:login")
