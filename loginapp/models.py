from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) 
    profile_picture = models.ImageField(upload_to = 'profile_pics')
   
    def __str__(self):
        return self.user.username

