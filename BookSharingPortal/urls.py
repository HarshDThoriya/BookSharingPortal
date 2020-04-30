from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from loginapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^loginapp/',include('loginapp.urls')),
    url(r'^homepage/',include('homepage.urls')),
    url(r'^user_profile/',include('user_profile.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
