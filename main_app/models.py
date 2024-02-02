from django.db import models

# Create your models here.


class Video(models.Model):
    main_video = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'Начално Видео'
        verbose_name_plural = 'Начално Видео'

    def __str__(self):
        return "Начално Видео"


class PersonalInfo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    picture = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'За мен'
        verbose_name_plural = 'За мен'

    def __str__(self):
        return "За мен"


class AdvertisementInfo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    video = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'Рекламна информация'
        verbose_name_plural = 'Рекламна информация'

    def __str__(self):
        return "Рекламна информация"


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    picture = models.ImageField(upload_to="static/images", null=True, blank=True)

    class Meta:
        verbose_name = 'Коментари'
        verbose_name_plural = 'Коментари'

    def __str__(self):
        return f"{self.name}"
