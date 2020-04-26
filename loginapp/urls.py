from django.conf.urls import url
from loginapp import views
# SET THE NAMESPACE!
app_name = 'loginapp'

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
]