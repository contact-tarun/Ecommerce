from django.shortcuts import render
from .forms import *
from .models import *



def home(request):
    return render (request, 'user/home.html')

def registration(request):
    form = Registration_form_validate
    return render(request,'user/registration.html',{"form":form})