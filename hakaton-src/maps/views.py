from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic import TemplateView
from maps.models import Challenge, AcceptedChallenge


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        return context


class AllChallengesData(View):

    def get(self, request):
        challenges = Challenge.objects.all()
        challenges_json = list()

        for challenge in challenges:
            challenges_json.append({
                'id': challenge.id,
                'title': challenge.address,
                'description': challenge.description,
                'photo': challenge.photo_url,
                'geolocation': str(challenge.geolocation)
            })

        return JsonResponse(challenges_json, safe=False)


class AddChallenge(View):

    def post(self, request):
        user_id = request.POST.get("userId")
        marker_id = request.POST.get("markerId")
        AcceptedChallenge.objects.create(challenge=marker_id, user_id=user_id)
        return HttpResponse(status=201)


class ChallengeView(TemplateView):
    template_name = "challenge_view.html"
    def get_context_data(self, **kwargs):
        try:
            challenges = Challenge.objects.all()
            context = super(ChallengeView, self).get_context_data()
            context['challenges'] = challenges
        except:
            pass

        return context
