from django.contrib import admin
from plantmateApp.models import Business, Plant, PlantImage
from plantmateApp.models import UserProfile


class BusinessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PlantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Plant, PlantAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(UserProfile)
admin.site.register(PlantImage)
