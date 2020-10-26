from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from authentication.forms import CreateUserFrom
from django.contrib.auth import authenticate, login, logout


def registration(req):
    form = CreateUserFrom(req.POST)
    if req.method == 'POST':

        if form.is_valid():
            form.save()
            messages.success(req, 'Account created successful')
            user = User.objects.get(username=req.POST['username'])

            # context = {
            #     'username': user.id,
            # }
            return redirect('pet create')
    # messages.error(req, form.error_messages.values())
    old_form_errors = form.errors
    form = CreateUserFrom()
    context = {
        'form': form,
        'error': old_form_errors
    }
    return render(req, 'registration/registration.html', context)


def sign_in(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('pet_list')
        else:
            message = messages.error(req, 'Username OR Password is incorrect')
            context = {
                'info': message
            }
            return render(req, 'registration/SignIn.html', context)
    else:
        return render(req, 'registration/SignIn.html')


def logoutuser(req):
    logout(req)
    return redirect('Sign In')