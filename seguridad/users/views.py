from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Credenciales inválidas")
    return render(request, 'users/login.html')

@login_required
def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    logout(request)
    return redirect('login')
