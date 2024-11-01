from django.contrib import admin

from users.models import Message, Profile, Skill


admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Skill)
