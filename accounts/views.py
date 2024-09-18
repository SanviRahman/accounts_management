from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def reginstration(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form=UserCreationForm()

    context={
        'form':form
    }   
    return render(request,'accounts/register.html',context)
