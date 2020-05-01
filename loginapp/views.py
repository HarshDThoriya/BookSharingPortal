from django.shortcuts import render
from loginapp.forms import ExtendedUserCreationForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def register(request):
    template = 'loginapp/registration.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExtendedUserCreationForm(request.POST,request.FILES)
        profile_form = UserProfileInfoForm(request.POST,request.FILES)

        if form.is_valid() and profile_form.is_valid():
            
            user = form.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            user.set_password(user.password)
            profile.save()

               
            return HttpResponseRedirect(reverse('loginapp:user_login'))

   
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileInfoForm()

    return render(request, template,{'form':form,
                           'profile_form':profile_form})










def index(request):
    return render(request,'loginapp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage:home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'loginapp/login.html', {})