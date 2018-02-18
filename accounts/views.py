from django.contrib.auth import login as auth_login
from accounts.forms import SignUpForm
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account(request):
    if request.user.is_authenticated:
        context = {
            'current_user': request.user
        }
        return render(request, 'account.html', context=context)
    else:
        raise PermissionDenied