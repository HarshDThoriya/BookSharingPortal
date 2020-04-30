from django.conf.urls import url
from loginapp import views
from django.conf.urls.static import static
from django.conf import settings
# SET THE NAMESPACE!
app_name = 'loginapp'

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)