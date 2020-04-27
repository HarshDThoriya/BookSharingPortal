from django.shortcuts import render
from loginapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'homepage/home.html')

def profile(request):
    return HttpResponseRedirect(reverse('user_profile:profile'))