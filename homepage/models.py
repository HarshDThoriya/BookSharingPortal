from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.conf import settings

item_choice = (
   ('B', 'Book'),
   ('S', 'Stationary'),
   ('O','Others'),
)

class itemInfo(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=False)
   #user = models.ManyToManyField(settings.AUTH_USER_MODEL,null=True,blank=False)
   item_pic1 = models.ImageField(upload_to='item_pics',blank=False,null=True)
   item_pic2 = models.ImageField(upload_to='item_pics',blank=False,null=True)
   item_des = models.TextField(blank=True,null=True)
   item_author = models.CharField(max_length=50,blank=False,null=True)
   item_name = models.CharField(max_length=50,blank=False,null=True)
   item_type = models.CharField(choices=item_choice,blank=False,max_length=50,null=True)
   post_datetime = models.DateTimeField(default=datetime.datetime.now(),null=True)