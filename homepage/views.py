from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ItemForm
from .models import itemInfo
from loginapp.models import UserProfileInfo
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
import copy
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

## other views functions are here.... ##

def home(request):
    psts=itemInfo.objects.values()
    posts = filter(request)
    form = forms.ItemForm()
    piclink = UserProfileInfo.objects.filter(user=request.user).values('profile_picture')
    print("piclink is ",piclink[0]['profile_picture'])
    piclink=piclink[0]['profile_picture']
    context={'form':form,'posts':posts,'piclink':piclink}


    if request.method == 'POST' and request.is_ajax():
        ID = request.POST.get('id')
        p = itemInfo.objects.get(pk=ID) 
        e = User.objects.filter(username=str(p.user)).values('email')
        name = p.item_name 
        usr = str(p.user)
        em=str(e[0]['email'])
        t = p.item_type
        if t=='B':
            t='Book'
        elif t=='S':
            t='Stationary'
        else:
            t='Others'
        dt = p.post_datetime
        by = p.item_author
        des = p.item_des
        pic1 = str(p.item_pic1)
        pic2 = str(p.item_pic2)
        return JsonResponse({'p_name':name,'tp':t,'desc':des,'dt':dt,'by':by,'pic1':pic1,'pic2':pic2,'usr':usr,'em':em})
    else:
        return render(request,'homepage/home.html',context)




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

def addpost1(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)

        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user
            #f.user.set([request.user]
            #form.user = User.objects.get(username=request.user.username)
            
            f.save()

            return HttpResponseRedirect(reverse('homepage:myposts'))
    
    return HttpResponseRedirect(reverse('homepage:myposts'))


def myPosts(request):
    psts=itemInfo.objects.values()
    posts = filter1(request)
    form = forms.ItemForm()
    form1 = forms.ItemForm()
    piclink = UserProfileInfo.objects.filter(user=request.user).values('profile_picture')
    print("piclink is ",piclink[0]['profile_picture'])
    piclink=piclink[0]['profile_picture']
    context={'form':form,'posts':posts,'piclink':piclink,'form1':form1}


    if request.method == 'POST' and request.is_ajax():
        ID = request.POST.get('id')
        p = itemInfo.objects.get(pk=ID) 
        name = p.item_name 
        usr = "dddd"
        t = p.item_type
        if t=='B':
            t='Book'
        elif t=='S':
            t='Stationary'
        else:
            t='Others'
        dt = p.post_datetime
        by = p.item_author
        des = p.item_des
        pic1 = str(p.item_pic1)
        pic2 = str(p.item_pic2)
        return JsonResponse({'p_name':name,'tp':t,'desc':des,'dt':dt,'by':by,'pic1':pic1,'pic2':pic2,'usr':usr})
    else:
        return render(request,'homepage/myposts.html',context)


@csrf_exempt
def deletePost(request):
    if request.method == 'POST' and request.is_ajax():
        ID = request.POST.get('p_id')
        print("ID is ",ID)
        p = itemInfo.objects.get(pk=ID) 
        p.delete()
        return HttpResponseRedirect(reverse('homepage:myposts'))

def filter1(request):
    #qs = Journal.objects.all()
    all_posts = itemInfo.objects.all().filter(user=request.user)
    #categories = Category.objects.all()
    title_contains_query = request.GET.get('homesearch')
    book=request.GET.get('book')
    stationary=request.GET.get('stationary')
    others=request.GET.get('others')
    byitemname=request.GET.get('byitemname')
    

    if is_valid_queryparam(title_contains_query):
        all_posts = all_posts.filter(item_name__icontains=title_contains_query)

    return all_posts

#@csrf_exempt
#def edit_post_data(request):
#    if request.method == 'POST' and request.is_ajax():
#        ID = request.POST.get('p_id')
#        p = itemInfo.objects.get(pk=ID) 
#        name = p.item_name 
#        t = p.item_type
#        dt = p.post_datetime
#        by = p.item_author
#        des = p.item_des
#        pic1 = str(p.item_pic1)
#        pic2 = str(p.item_pic2)
#        return JsonResponse({'p_name':name,'tp':t,'desc':des,'dt':dt,'by':by,'pic1':pic1,'pic2':pic2, 'id':ID}) 
    

def edit_post(request,p):
    pt = itemInfo.objects.get(pk=p)
    form = forms.ItemForm(instance=pt)
    piclink = UserProfileInfo.objects.filter(user=request.user).values('profile_picture')
    print("piclink is ",piclink[0]['profile_picture'])
    piclink=piclink[0]['profile_picture']

    if request.method == "POST":
        form = forms.ItemForm(request.POST,request.FILES,instance=pt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage:myposts'))
    else:
        return render(request,'homepage/edit_post.html',{'editform':form,'piclink':piclink})
        
