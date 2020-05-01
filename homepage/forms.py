from django import forms
from homepage.models import itemInfo
from django.contrib.auth.models import User


class ItemForm(forms.ModelForm):
    class Meta():
        model = itemInfo
        fields = ('item_name','item_type','item_author','item_des','item_pic1','item_pic2')

        