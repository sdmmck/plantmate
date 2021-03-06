from django.contrib import admin
from plantmateApp.models import Business, Plant, PlantImage
from plantmateApp.models import UserProfile
from plantmateApp.models import UserSavedPlants, UserWishlistPlants
from plantmateApp.models import Comment


class BusinessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PlantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Plant, PlantAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(UserProfile)
admin.site.register(PlantImage)
admin.site.register(UserWishlistPlants)
admin.site.register(UserSavedPlants)
admin.site.register(Comment)
