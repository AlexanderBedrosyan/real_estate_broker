from django.db import models

# Create your models here.


class Video(models.Model):
    main_video = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'Starting Video'
        verbose_name_plural = 'Starting Video'

    def __str__(self):
        return "Open Video"


class PersonalInfo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    picture = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'FP Personal Information'
        verbose_name_plural = 'FP Personal Information'

    def __str__(self):
        return "My Personal Information"


class AdvertisementInfo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    video = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'FP Adv Information'
        verbose_name_plural = 'FP Adv Information'

    def __str__(self):
        return "My Adv Information"
