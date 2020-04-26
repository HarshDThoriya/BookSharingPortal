from django import forms
from homepage.models import itemInfo
from django.contrib.auth.models import User

item_choice = (
   ('B', 'Book'),
   ('S', 'Stationary'),
   ('C','Coupon')
)

class UserProfileInfoForm(forms.ModelForm):
    item_type = forms.ChoiceField(choices=item_choice, widget=forms.RadioSelect())
    item_pic1 = forms.ImageField(upload_to='item_pics',blank=False)
    item_pic2 = forms.ImageField(upload_to='item_pics',blank=False)
    item_name = forms.charField(max_length=50,blank=False)
    item_post_date = forms.DateTimeField(default=datetime.now())

    class Meta():
        model = itemInfo
        fields = ('item_pic1','item_pic2','item_name','item_type','item_post_date')