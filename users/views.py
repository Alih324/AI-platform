from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import UserEditForm, UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    form = AuthenticationForm(request, data=request.POST or None)
    for field in form.fields.values():
        field.widget.attrs.setdefault('class', 'form-control')

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}.')
            return redirect('profile')
        messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html', {'form': form})


@require_POST
def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})
