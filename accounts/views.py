from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'The user name has been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                                    password=request.POST['password1'],
                                    email = request.POST['email'],
                                    first_name = request.POST['firstname'],
                                    last_name = request.POST['lastname'])

                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')






def logout(request):
    return render(request, 'accounts/logout.html')
