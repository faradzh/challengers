from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'birthday', 'created_at', 'phone')
    model = Profile
admin.site.register(Profile, ProfileAdmin)
