from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def reginstration(requenst):
    form=UserCreationForm()
    context={
        'form':form
    }   
    return render(requenst,'accounts/register.html',context)
