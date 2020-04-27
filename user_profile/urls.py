from django.conf.urls import url
from user_profile import views
from django.urls import path

app_name = 'user_profile'

urlpatterns = [
    url(r'^profile/$',views.user_profile,name="profile"),
]