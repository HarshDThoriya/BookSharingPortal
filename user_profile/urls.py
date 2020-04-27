from django.conf.urls import url
from user_profile import views
from django.urls import path

app_name = 'user_profile'

urlpatterns = [
    path('user_profile/',views.user_profile,name = 'user_profile'),
]
