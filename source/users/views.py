from django.shortcuts import render,redirect
from  django.shortcuts import render 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from  django.shortcuts import redirect
from django.contrib import messages
from django.views import View



def login_view(request):
    if request.method == 'POST':
         login_form = AuthenticationForm(request=request, data=request.POST)
         if login_form.is_valid():
              username = login_form.cleaned_data.get('username')
              password = login_form.cleaned_data.get('password')
              user = authenticate(usename=username,password=password)
              if user is not None:
                 login(request,user)
                 messages.success(
                     request, f'You are now logged in as {username}')
                 return redirect('home')
              else:
                  messages.error(request, f'An error occured trying to login')
         else:
                 messages.error(request, f'An error occured trying to login')
    elif request.method == 'GET':
      login_form =AuthenticationForm()
    return render(request,'views/login.html', {'login_form': login_form})





def register_view(request):
    return render(request,'views/register.html')

def farming_view(request):
    return render(request,'views/farming.html')

def healthcare_view(request):
    return render(request,'views/healthcare.html')

def pollution_view(request):
    return render(request,'views/pollution.html')

def renewable_view(request):
    return render(request,'views/renewable.html')

def private_view(request):
    return render(request,'views/private.html')

def recycle_view(request):
    return render(request,'views/recycle.html')
        
