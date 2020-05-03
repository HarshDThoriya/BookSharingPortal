from django.shortcuts import render , redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.http import HttpResponseRedirect
from user_profile.forms import EditProfileForm,EditProfileInfoForm
from django.contrib.auth import update_session_auth_hash
from loginapp.forms import ExtendedUserCreationForm,UserProfileInfoForm



# Create your views here.
def user_profile(request):
    if request.method == "POST":
        form = UserProfileInfoForm(request.POST,instance=request.user)
        #phone_number = request.POST.get('phone_number')
        print(form.data)
        phone_number = form.data['phone_number']
        args = {'user':request.user,'form':form,'phone_number':phone_number[0]}
        return render(request,'user_profile/index.html',args)
    else:

        args = {'user':request.user , 
                'phone_number': request.user.userprofileinfo.phone_number,
                'portfolio_site':request.user.userprofileinfo.portfolio_site,
                'profile_picture':request.user.userprofileinfo.profile_picture}
        print('profile_picture : {}'.format(request.user.userprofileinfo.profile_picture))
        return render(request,'user_profile/index.html', args)

def edit_profile(request):
    if request.method == "POST":
        print('In Post')
        #form = EditProfileForm(request.POST, instance = request.user)
        # form1 = EditProfileForm(request.POST, instance = request.user)
        # form2 = EditProfileInfoForm(request.POST, instance = request.user)
        form1 = ExtendedUserCreationForm(request.POST,request.FILES, instance = request.user)
        form2 = UserProfileInfoForm(request.POST,request.FILES,instance=request.user.userprofileinfo)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            # user = form1.save()
            # profile = form2.save(commit=False)
            # profile.user = user
        #     # return reverse('../templates/user_profile/index.html')
            # return redirect("/templates/user_profile/index.html")
            print('near to context')
            # if 'picture' in request.FILES:
            #     profile.profile_picture = request.FILES['picture']
            #     print('Profile_picture',profile.profile_picture)
            # profile.save()
            args = {'user':request.user , 
                'phone_number': request.user.userprofileinfo.phone_number,
                'portfolio_site':request.user.userprofileinfo.portfolio_site,
                'profile_picture':request.user.userprofileinfo.profile_picture}
            print('phone_number : {}'.format(request.user.userprofileinfo.phone_number))
            print('profile_picture : {}'.format(request.user.userprofileinfo.profile_picture))
            return render(request,'../templates/user_profile/index.html',args)
            #return redirect('/user_profile/profile/')
            #return reverse('index')
    else:
        # form1 = EditProfileForm(instance=request.user)
        # form2 = EditProfileInfoForm(instance=request.user)
        # args = {'form1': form1,'form2':form2}
        print('ELSE Edit profile GET')
        form1 = ExtendedUserCreationForm(instance = request.user)
        form2 = UserProfileInfoForm(instance=request.user.userprofileinfo)
        args = {'form1': form1,'form2':form2}
        return render(request,'../templates/user_profile/edit_profile.html',args)
        

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            args = {'user':request.user , 
                'phone_number': request.user.userprofileinfo.phone_number,
                'portfolio_site':request.user.userprofileinfo.portfolio_site,
                'profile_picture':request.user.userprofileinfo.profile_picture}
            print('phone_number : {}'.format(request.user.userprofileinfo.phone_number))
            return render(request,'../templates/user_profile/index.html',args)
            #return redirect('index')
        else:
            print('>>>>>> nahi hua ')
            return render(request,'../templates/user_profile/change_password.html')
            #return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        print('>>> Else hua GET')

        args = {'form': form}
        return render(request,'../templates/user_profile/change_password.html',args)
