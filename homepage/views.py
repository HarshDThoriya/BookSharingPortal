from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ItemForm
from .models import itemInfo
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    #qs = Journal.objects.all()
    all_posts = itemInfo.objects.all()
    #categories = Category.objects.all()
    title_contains_query = request.GET.get('homesearch')
    book=request.GET.get('book')
    stationary=request.GET.get('stationary')
    others=request.GET.get('others')
    byitemname=request.GET.get('byitemname')
    

    if is_valid_queryparam(title_contains_query):
        all_posts = all_posts.filter(item_name__icontains=title_contains_query)

    if book == 'on':
        all_posts = all_posts.filter(item_type__in=('Book'))

    elif stationary == 'on':
        all_posts = all_posts.filter(item_type__in=('Stationary'))
    
    elif others == 'on':
        all_posts = all_posts.filter(item_type__in=('Others'))

    if byitemname == 'on':
        all_posts = all_posts.order_by('item_name')
        
    return all_posts

def home(request):
    posts = filter(request)
    form = forms.ItemForm()
    return render(request,'homepage/home.html',{'form':form,'posts':posts})

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

def myPosts(request):
    all_posts = itemInfo.objects.all()
    return render(request,'homepage/myposts.html',{'all_posts':all_posts})

