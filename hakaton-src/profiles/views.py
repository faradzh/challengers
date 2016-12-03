from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm


# def home(request):
#    context = RequestContext(request, {'request': request, 'user': request.user})
#    return render_to_response('sign_up.html', context=context)
#
#
# def profile(request, username):
#     user = User.objects.get(username=username)
#     profile = user.profile
#     if request.user.is_authenticated:
#         return render(request, 'profile.html', {'profile': profile})


# def profile_edit_page(request, username):
#     print("WWWWWWWWWWWWWWW %s" % username)
#     user = User.objects.get(username=username)
#     profile = user.profile
#     return render(request, 'edit_profile.html', {'profile': profile})
#
#
# # @login_required
# # @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('settings:profile')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
