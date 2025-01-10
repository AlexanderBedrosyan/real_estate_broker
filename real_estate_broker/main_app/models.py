from django.db import models
from .validators import IsItAPhoneNumber, DateChecker
from .choices import ConsultationChoices

# Create your models here.


class Comments(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    profession = models.CharField(
        max_length=100
    )
    picture_url = models.URLField()
    short_message = models.CharField(
        max_length=1000
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Consultation(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    email = models.EmailField(
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        max_length=100,
        validators=[IsItAPhoneNumber()],
        blank=False,
        null=False
    )
    choices = models.CharField(
        max_length=100,
        choices=ConsultationChoices.choices,
        blank=False,
        null=False
    )
    consultation_datetime = models.DateTimeField(
        blank=False,
        null=False,
        validators=[DateChecker()]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    image = models.URLField()
    date = models.DateTimeField()
    location = models.CharField(
        max_length=300,
        default='Бургас'
    )
    organizer = models.CharField(
        max_length=300,
        default='Стоян Черелов'
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заглавие")
    description = models.TextField(verbose_name="Описание")
    image_url = models.URLField(max_length=500, verbose_name="URL на изображението")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на създаване")

    def __str__(self):
        return self.title
