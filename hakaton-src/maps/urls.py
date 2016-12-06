from django.conf.urls import url
from maps.views import Index, AllChallengesData, AddChallenge, challenge_detail

urlpatterns = (
    url(r'^$', Index.as_view(), name='index'),
    url(r'^challenges-json/$', AllChallengesData.as_view(), name='challenges_json'),
    url(r'^add-challenge$', AddChallenge.as_view(), name='add_challenge'),
    # url(r'^challenges/$', ChallengeView.as_view(), name='challenges')
    url(r'^challenge_detail/(?P<challenge_slug>\S+)/$', challenge_detail, name='challenge_detail'),

)
