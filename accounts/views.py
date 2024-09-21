from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model= User
        fields= [
            'username',
            'email',
            'password',
            'last_name',
            'first_name',
        ]

def reginstration(request):
    if request.method=="POST":
        form=CustomUserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form=CustomUserCreateForm()

    context={
        'form':form
    }   
    return render(request,'accounts/register.html',context)
