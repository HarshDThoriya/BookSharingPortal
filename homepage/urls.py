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
    url(r'^addpost1/$',views.addpost1,name="addpost1"),
    url(r'^myposts/$',views.myPosts,name="myposts"),
    url(r'^delete/$',views.deletePost,name="delete_post"),
    url(r'^edit_post/(?P<p>.*)/$',views.edit_post,name="edit_post"),
    #url(r'^edit_post_data/$',views.edit_post_data,name="edit_post_data"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)