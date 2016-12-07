from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from maps.models import Challenge, AcceptedChallenge, CompletedChallenge


class ChallengeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(AcceptedChallenge)
admin.site.register(CompletedChallenge)
