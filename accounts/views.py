from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm , SignupForm
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
# Create your views here.



def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                print(user)
                login(request,user)
                return render(request,'index.html')
            else:
                print('Invalid credentials!')
            
                
    form = LoginForm()
    return render(request, 'accounts/login.html',{'form':form})

def signout(request):
    logout(request)
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(
                form.cleaned_data['enter_password']
            )
            user.save()
            login(request,user)
            return render(request, 'index.html')
        else:
            
            
            # messages.error(request,'something is fishy')
            return render(request, 'accounts/signup.html',{'form':form})

        
    sign = SignupForm()
    return render(request, 'accounts/signup.html',{'sign':sign})



