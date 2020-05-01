from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ItemForm


def home(request):
    form = forms.ItemForm()
    return render(request,'homepage/home.html',{'form':form})

def profile(request):
    return HttpResponseRedirect(reverse('user_profile:profile'))

def addpost(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)

        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            #f.user.set([request.user]
            #form.user = User.objects.get(username=request.user.username)
            
            f.save()

            return HttpResponseRedirect(reverse('homepage:home'))
    
    return HttpResponseRedirect(reverse('homepage:home'))
    