from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required



def main_view(request):
    return render(request,"views/main.html",{"name":"Jeevanam"})


@login_required
def home_view(request):
    return render(request,"views/home.html")
