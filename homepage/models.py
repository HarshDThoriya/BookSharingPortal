from django.db import models
from django.utils import timezone
import datetime

item_choice = (
   ('B', 'Book'),
   ('S', 'Stationary'),
   ('C','Coupon')
)

class itemInfo(models.Model):

  
    item_pic1 = models.ImageField(upload_to='item_pics',blank=False)
    item_pic2 = models.ImageField(upload_to='item_pics',blank=False)
    item_name = models.CharField(max_length=50,blank=False)
    item_type = models.CharField(choices=item_choice, max_length=128)

    def __str__(self):
        return self.user.username
