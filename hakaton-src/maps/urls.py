from django.conf.urls import url
from maps.views import Index

urlpatterns = (
   url(r'^$', Index.as_view(), name='index'),
)