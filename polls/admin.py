from django.contrib import admin

from .models import Guest, PlusOneGuest, Comment

admin.site.register(Guest)
admin.site.register(PlusOneGuest)
admin.site.register(Comment)
