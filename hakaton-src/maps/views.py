from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from maps.models import Challenge, AcceptedChallenge, CompletedChallenge
from profiles.models import Profile


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
                'price': challenge.price,
                'points': challenge.points,
                'photo': challenge.photo_url,
                'geolocation': str(challenge.geolocation)
            })

        return JsonResponse(challenges_json, safe=False)


class AddChallenge(View):

    def post(self, request):
        user_id = request.POST.get("userId")
        marker_id = request.POST.get("markerId")
        try:
            profile = Profile.objects.get(user=user_id)
            challenge = Challenge.objects.get(pk=marker_id)
            AcceptedChallenge.objects.create(challenge=challenge, user=profile)
        except (User.DoesNotExist, Challenge.DoesNotExist):
            pass
        return JsonResponse({"status": "ok"})


def challenge_detail(request, marker_id):
    challenge = Challenge.objects.get(id=marker_id)
    return render(request, 'challenge_detail.html', {'challenge': challenge})


class ChallengeView(TemplateView):
    template_name = "challenge_view.html"

    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        print(user_id)
        context = super(ChallengeView, self).get_context_data(**kwargs)
        accepted_challenges = AcceptedChallenge.objects.filter(user_id=user_id)
        completed_challenges = CompletedChallenge.objects.filter(user_id=user_id)
        context['accepted_challenges'] = accepted_challenges
        context['completed_challenges'] = completed_challenges
        return context


