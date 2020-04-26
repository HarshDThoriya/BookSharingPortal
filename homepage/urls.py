from django.conf.urls import url
from homepage import views
# SET THE NAMESPACE!
app_name = 'homepage'

urlpatterns=[
    url(r'^home$',views.home,name="home"),
]