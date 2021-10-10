from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'app/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                messages.success(request,'Registered Successfully!!!')
                fm.save()
                fm = SignupForm()
                return HttpResponseRedirect('/login/')
        else:
            fm = SignupForm()
        return render(request, 'app/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfully!!!')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')