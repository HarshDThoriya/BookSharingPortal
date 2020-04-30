from django import forms
from homepage.models import itemInfo
from django.contrib.auth.models import User

item_choice = (
   ('B', 'Book'),
   ('S', 'Stationary'),
   ('C','Coupon')
)

class ItemForm(forms.ModelForm):
    class Meta():
        model = itemInfo
        fields = ('item_name','item_type')
        