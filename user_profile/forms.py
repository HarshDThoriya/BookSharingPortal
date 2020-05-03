from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from loginapp.models import UserProfileInfo

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )

class EditProfileInfoForm(UserChangeForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','phone_number','profile_picture')