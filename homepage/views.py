from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    form = forms.ItemForm()
    return render(request,'homepage/home.html',{'form':form})

def profile(request):
    return HttpResponseRedirect(reverse('user_profile:profile'))

def addpost(request):
    form = forms.ItemForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.ItemForm(data=request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            u = form.save()
            return HttpResponseRedirect(reverse('homepage:home'))
        else:
            print("hbufewewOIAKSMDJV SADKMO;IDFJVAOCMVND KVSL;ASMVDKFJP[VFD KFCMAMSK DFSLDKCA;M NDFVLC;LF VNSDL")


    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",request.method == 'POST')
    form1 = forms.ItemForm()
    return HttpResponseRedirect(reverse('homepage:home'))
    