from django.contrib import admin
from plantmateApp.models import Business
from plantmateApp.models import UserProfile


class BusinessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Business, BusinessAdmin)
admin.site.register(UserProfile)
