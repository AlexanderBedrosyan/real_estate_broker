from django.contrib import admin
from .models import PersonalInfo, AdvertisementInfo

# Register your models here.


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementInfo)
class AdvertisementInfoAdmin(admin.ModelAdmin):
    pass