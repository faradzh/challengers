from django.conf.urls import url
from maps.views import Index, AllChallengesData

urlpatterns = (
   url(r'^$', Index.as_view(), name='index'),
   url(r'^challenges-json/$', AllChallengesData.as_view(), name='challenges_json')
)