from django.shortcuts import render , redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.http import HttpResponseRedirect
from user_profile.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def user_profile(request):
    args = {'user':request.user}
    return render(request,'user_profile/index.html',args)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            # return reverse('../templates/user_profile/index.html')
            # return redirect("/templates/user_profile/index.html")
            return render(request,'../templates/user_profile/index.html')
           # return reverse('')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request,'../templates/user_profile/edit_profile.html',args)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return render(request,'../templates/user_profile/index.html')
        else:
            return render(request,'../templates/user_profile/change_password.html')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request,'../templates/user_profile/change_password.html',args)
