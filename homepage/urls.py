from django.conf.urls import url
from homepage import views
from django.conf.urls.static import static
from django.conf import settings
# SET THE NAMESPACE!
app_name = 'homepage'

urlpatterns=[
    url(r'^home/$',views.home,name="home"),
    url(r'^profile/$',views.profile,name="profile"),
    url(r'^addpost/$',views.addpost,name="addpost"),
    url(r'^myposts/$',views.myPosts,name="myposts"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)