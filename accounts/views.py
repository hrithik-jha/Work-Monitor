from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

def signup(request):
    if request.method == 'POST':
        #User will sign up.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['regno'])
                return render(request, 'accounts/signup.html', {'error': 'This Registration Number has already been registered.'}) 
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['regno'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'The passwords don\'t match.'})            
    else:
        #User wants to enter info.
        return render(request, 'accounts/signup.html')

#GIVE AN ERROR IF PASSWORDS DONT MATCH

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['regno'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'The Username or Password is incorrect.'})            
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')