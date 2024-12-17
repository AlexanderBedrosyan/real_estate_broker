from django.contrib import admin
from .models import PersonalInfo, AdvertisementInfo, Video, Comment

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementInfo)
class AdvertisementInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass