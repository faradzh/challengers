from django.conf.urls import include, url
from . import views


urlpatterns = (
   # url(r'^$', views.home, name='home'),

   url(r'^(?P<username>\S+)/$', views.profile, name='profile'),
   url(r'^edit/$', views.update_profile, name='profile_edit'),

)